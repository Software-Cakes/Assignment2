from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xml.etree.cElementTree as ET
import requests
import os
import datetime 

#create path to XML file
XML_FILE = "notebook.XML"

if not os.path.exists(XML_FILE):
    root = ET.Element("notebook")
    tree = ET.ElementTree(root)
    tree.write(XML_FILE)

#restrict to a particular path
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

#operations 
def process_input(topic, note, text):
    try:
        print("processing input: topic: " + topic + "\nnote: " + note + "\ntext: " + text)

        tree = ET.parse(XML_FILE)
        root = tree.getroot()

        topic_elem = root.find("./topic[@name='" + topic + "']")
        if topic_elem == None:
           topic_elem = ET.Element("topic")
           topic_elem.set("name", topic)
           root.append(topic_elem)
           
        note_elem = ET.Element("note")
        note_elem.set("name", note)
        text_elem = ET.SubElement(note_elem, "text")
        text_elem.text = text
        timestamp_elem = ET.SubElement(note_elem, "timestamp")
        timestamp_elem.text = datetime.datetime.now().strftime("%m/%d/%y - %H:%M:%S")
        topic_elem.append(note_elem)
    
        tree.write(XML_FILE)
        return True
    
    except Exception as e:
        print(str(e))
        return str(e)

def retrieve_contents(topic):
    try:
        print("retrieving conents for " + topic)

        tree = ET.parse(XML_FILE)
        root = tree.getroot()

        topic_elem = root.find(".//topic[@name='" + topic + "']")
        if topic_elem == None:
            return []

        print("found topic: " + topic)

        notes = []
        for note in topic_elem.findall("note"):       
            print("note: " + note.attrib["name"])
            print("text: " + note.find("text").text)
            print("timestamp: " + note.find("timestamp").text)
            notes.append({
                "name": note.attrib["name"],
                "text": note.find("text").text,
                "timestamp": note.find("timestamp").text
            })
            
        print("retrieve_contents: returned " + str(notes))
        return notes
    
    except Exception as e:
        print (str(e))
        return str(e)

def query_wiki(topic):
    try: 
        wiki_api_url = "https://en.wikipedia.org/w/api.php?action=query&format=json&prop=info&generator=allpages&inprop=url&gapfrom=Apple&gaplimit=5"
        parameters = {
            'action': 'opensearch',
            'search': topic,
            'limit': 1,
            'format': 'json'
        }

        return_results = requests.get(wiki_api_url, params=parameters)
        given_data = return_results.json()

        if given_data[1]:
            artcile_link = given_data[3][0]
            process_input(topic, "Linked Wikipedia Article", artcile_link)
            return artcile_link
        else:
            return "Artcile not found."
        
    except Exception as e:
        print(str(e))
        return str(e)

#main program
if __name__ == "__main__":
    with SimpleXMLRPCServer(('localhost', 8000),
                            requestHandler=RequestHandler) as server:
        server.register_introspection_functions()
        server.register_function(process_input, 'process_input')
        server.register_function(retrieve_contents, 'retrieve_contents')
        server.register_function(query_wiki, 'query_wiki')
        print("Server listening on localhost: 8000...")
        server.serve_forever()