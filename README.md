# Assignment2
A XML-RPC integrated server and client programs to enable end-users encode personal input into an XML file. 

## Table of Contents
- [Installation](#installation)
- [Technologies Used](#technologies-used)
- [Solutions to Design Challenges](#solutions-to-design-challenges)
- [Demonstration Video](#demonstration-video)

## Installation 

**How to Install Server.py and Client.py**:

- Download repository ZIP.
- Run files on local rich text editor. \


## Technologies Used
To create Remote Procedure Calls (RPCs), XML-RPC was implemented and utilized in server.py and client.py. XML-RPC, defined by XML-RPC website, is a remote procedure calling that utilizes HTTP as its primary transport mechanism and XML to encode inputs. 


## Solutions to Design Challenges
1. Heterogeneity: The developed source code utilized XML-RPC. Since it is a set of implementations that enable software running on disparate oeprating systems, running in different environments to make procedure calls over the Internet, the provided codes can be written in different languages as long as they retain the fundamental operations. 
2. Openness: The server and client based on the presented code communicate via HTTP, a standard and open protocol. Since XML-RPC protocol is widely supported by various systems, it thus facilitates interoperability between different systems as long as the codes are in use. 
3. Security: While the developed source code for the given assignment has weak security, the implementation of if-else serves as simple authentication and verification of the given inputs from the client.
4. Scalability: While the presented codes do not cover scalability, the non-functional requirement can be implemented in future iterations of the program to support large quantities of clients silmultaneously. 
5. Failure Handling: To ensure the program, especially for the server, to handle failures, the os module was implemented. Try and except are utilized throughout both source codes for server and client to handle invalid inputs. When an error occurs, an error message with elucidation on the occurred failure is printed to the client’s device. 
6. Transparency: The program achieves transparency, albeit at a simplistic level, by abstracting the remote procedure calls with the XML-RPC protocol. Thus, clients are unaware that they are calling procedures on a remote server when interacting with the system. 


## Demonstration Video
