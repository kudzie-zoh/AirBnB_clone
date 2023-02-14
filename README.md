
# 0x00. AirBnB clone - The console
## Project Description
- The goal of the project is to deploy on our servers a simple copy of the AirBnB website. 
- By the end of the project, it will be complete web application composed by:

	 - &ensp; A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
	 - &emsp; A website (the front-end) that shows the final product to everybody: static and dynamic
	 - &emsp; A database or files that store data (data = objects)
	 - &emsp; An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)
## The command Interpreter(console)
- The command interpreter provides an interface between the user and the kernel and executes commands(shell). it enables us to manage the objects of our project:
	- Create a new object (ex: a new User or a new Place)
	- Retrieve an object from a file, a database etc…
	- Do operations on objects (count, compute stats, etc…)
	- Update attributes of an object
	- Destroy an object
### The command interpreter Execution
- The command interpreter should work on both interactive and non-interactive modes.
- **In interractive mode, the shell should work like**:  
	
> 	$ ./console.py  
>	(hbnb) help  
>	  
> 	Documented commands (type help <topic>):  
> 	\=======================================  
>	EOF  help  quit  
>	  
> 	(hbnb)  
> 	(hbnb)  
> 	(hbnb) quit  
> 	$

- **In non -interactive mode**:
>	echo "help" | ./console.py  
>	(hbnb)  
>	  
>	Documented commands (type help <topic>):  
>	\=======================================  
>	EOF  help  quit  
>	(hbnb)  
>	$  
>	$ cat test_help  
>	help  
>	$  
>	$ cat test_help | ./console.py  
>	(hbnb)  
>	  
>	Documented commands (type help <topic>):  
>	\=======================================  
>	EOF  help  quit  
>	(hbnb)   
>	$  
