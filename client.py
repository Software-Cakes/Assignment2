from xmlrpc.client import ServerProxy
import os

#establishing server
server = ServerProxy("http://localhost:8000/RPC2")

#main program
if __name__ == "__main__":
    print("Welcome!\nPlease select an action from the menu.")
    while True:
        print("1) Add a note.\n2) Retrieve data based on a given topic.\n3) Name and append searched terms on Wikepedia API into existing XML file.\n4) Exit program.")
        user_input = input("Enter your input (1-4): ")

        try:
            if user_input == '1':
                topic = input("Enter topic: ")
                note = input("Enter note: ")
                text = input("Enter text: ")
                
                server.process_input(topic, note, text)

                print()
                print("Added Note:\nTopic: " + topic + "\nNote: " + note + "\nText: " + text + "\n")
                
            elif user_input == '2':
                topic = input("Enter topic to retrieve: ")
                print("Combing through the database...\n")
                notes = server.retrieve_contents(topic)
                if notes:
                    for n in notes:
                        print("Note: " + n["name"] + "\nText: " + n["text"] + "\nTimestamp: " + n["timestamp"] + "\n")
                else:
                    print("No notes found for topic " + topic + ".\n")
                
            elif user_input == '3':
                search_term = input("Enter search term for Wikipedia: ")
                artcile_link = server.query_wiki(search_term)
                print("Result from Wikipedia Search: " + str(artcile_link))

                if artcile_link != "Artcile not found.":
                    topic = input("Enter topic to append data to: ")
                    if server.process_input(topic, "Linked Wikipedia Article", artcile_link):
                        print("Data appended successfully.\n")
                    else:
                        print("Data appended unsuccessfully.\n")

            elif user_input == '4':
                print("Thank you for using the program. Exiting...")
                break

            else:
                print("Invalid input. Try again.\n")
        
        except Exception as e:
            print("Error: " + str(e))