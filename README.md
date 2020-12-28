# Chatbot

This project has been contributed by the following :-

Preyansh Rastogi, Shivam Shanker, Abhishek Rajgaria and Anuj Verma.

## Application Code

The following shows the two screens of the android application.

![Chatbot](https://user-images.githubusercontent.com/44090539/103181753-bb6cde80-48ca-11eb-9cae-6c9e227412a5.png)

### Images

It contains all the images that were used in the android application.

### MainActivity.java

It handled the login functionality of the first page of the application.

### SecondActivity.java

It handled the query handling of the user by contacting with the server in the 
backend on the second page of the application.

### XML files

They were used in designing the various components of the application.

## Backend Code

### server.py 
This file contains the code for connection between server and client
and it is a local server and we are sending and receiving data through this.

### backend.py
In this file we are connecting through the MySQL server on local computer 
and after connection we are fetching the data from the database and giving the 
desired result by making assiging the user's query among the given project options
by using nltk pos-tags after processing the user's text.

### chatbot_tools.sql
It contains all the tools for the specific project

### chatbot_keyword_table.sql
It contains the keyword for the different projects

### chatbot_description_table.sql
It contains the description of the projects
