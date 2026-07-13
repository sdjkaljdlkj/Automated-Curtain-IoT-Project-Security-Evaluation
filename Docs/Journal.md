# Entry 1:

## Tasks Completed:

### Drew a System Overview Diagram
I hand-drew a diagram encompassing how the entire project is projected to look, giving me a big picture of how everything is going to connect to each other. Labelled "Diagram of System Overview Pre-Implementation.jpg" in the Diagrams folder within the repository.

### Prepared the Raspberry Pi
I started by flashing the Pi OS onto the Raspberry Pi using a Micro-SD card and chose a headless setup using SSH over WiFi. Once I had connected to the Raspberry Pi using SSH from my laptop, I installed the GPIO libraries necessary for interacting with the hardware.

### Set up VS Code Remote-SSH
I set up the Remote-SSH function in VS Code and connected it remotely to the Raspberry Pi so I can develop the software in this project on my laptop rather than editing these files on a terminal. This gives me the capabilities of an IDE (such as: syntax highlighting, auto-completing and an integrated terminal) to help make the coding process as efficient as possible. This also mirrors real IoT development practices where I code on a more usable platform then test my code against the real hardware.

## Problems and their solutions:
While trying to SSH to the Raspberry Pi on my laptop I was having difficulties connecting because I couldn't resolve the hostname. This was because I didn't know the IP address of it. So I scanned my local subnet using nmap and found it, then I connected to the Pi via SSH using the IP address directly rather than the hostname.

## What did I learn:
- How to set up a Raspberry Pi using headless setup.
- How to use nmap to discover different devices on a network.
- How to draw and annotate diagrams to represent the general architecture of IoT projects.
- How to set up Remote-SSH on VS Code.

## What's next:
- Complete the rest of the diagrams (one more focused on the electronics of the project and another on the mechanical side of the project and finally a diagram of these 2 systems integrated).
- Learn how to set up the wiring of the project and test the mechanical components to see if they are suitable for the project (provided the components have arrived).

# Entry 2:

## Tasks Completed:

- Created a Requirements specification for the project. Defines both the functional and non-functional requirements of the system. Labelled "Requirements Specification.md" in the Docs folder within the repository.
- Created a diagram of the mechanical aspect of the project including the motor and the wheel that rotates the curtain cord. It encompasses all the moving parts of the system. Labelled "Diagram of Mechanical Drive Assembly.jpg" in the Diagrams folder within the repository.
- Created a diagram of the electrical aspect of the project including all aspects of the system that require electrical wiring and power. Labelled "Diagram of Electrical Wiring.jpg" in the Diagrams folder within the repository.
- Created a Threat Model document using commercially used frameworks and methodologies (OWASP Threat Modeling Process and the STRIDE methodology to identify threats). Labelled "Threat Model.md" in the Docs folder within the repository.

## Problems and their solutions:

- Had issues understanding the GPIO pins of the Raspberry-Pi and so I did some research and learnt what each one represents on pinout.xyz.
- Had issues understanding the purpose of the ground pins on the L298N and the Raspberry-Pi so I did some research online to gain a better understanding of their uses and purpose.

## What's next:

- Test the components ordered once they have arrived.
- Write the motor control class for the curtain control application in python using the GPIOZero library.



