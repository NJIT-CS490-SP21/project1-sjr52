# **MUSIC DISCOVERY APP: _CS490-PROJECT-#1 MILESTONE-#1_**
***
## Table of Contents
1. Technologies, Frameworks, Libraries and API
2. Structure
3. Creating a Spotify account (API KEY)
4. Setting up - (Main Python File)
5. Setting Up -(HTML File) and (CSS File)
6. Technical Issues
***
# __1.) Technologies, Frameworks, Libraries and API :__
    -__Technologies__ used:
        -AWS Cloud9 IDE - Used for coding in PYTHON, HTML and CSS

    -__Frameworks__ used:
        -Python(Flask): Used for Creating a WEB SERVER
    -__Libraires__ used:
    
        -Requests: Used to send POST and GET request to Spotify.
        -os, dotenv: Used to export hidden .env file which contained API Key. 
        -json: Used for Parsing response recieved from Spotify.
        -random: Used to dynamically fetch and generate random track information on webpage.
        -render_template: Used to pass parameters to HTML file.
        
    -__API__ used:
        -Spotify API: Used to obtain artist name, song name, song picture, and preview link.
***
# __2.) Setting up the Project Structure :__
    Step 1: Creating an __AWS Educate Account and Getting Started with Cloud 9__:
        -[AWS Educate Account](https://aws.amazon.com/education/awseducate/)
        -After you have Created the account, on the top there is a search-bar where you should type cloud9 and it will load cloud9 IDE. 
    
    Step 2: Creating __Project Files__:
        1. Create a Main Working Directory:
            - mkdir directory_name;
            
        2. Go into the directory:
            - cd directory_name
            
        3. Python File Creation:
            * Create a python file, Where you will create the web server.
              - touch main_python_file_name.py
              
        4. HTML File Creation:  
            * Creating a sub-directory and with HTML file inside that sub-directory.
             - mkdir templates // Make sure the name of the sub-directory is templates
             - cd templates
             - touch HTML_File_Name.html
             
        5. CSS File Creation:
           * Creating a sub-directory and with CSS file inside that sub-directory.
            - if you are not in the main working directory, do (cd ..) this will bring you to the main directory 
            - now in the main directory do:
               - mkdir static //Make sure the name of the sub-directory is called static.
               - cd static
               - touch CSS_File_Name.html
***

# __3.) Creating a Spotify account for API Key :__
    Step 1.) Go To (https://developer.spotify.com/dashboard/login):
        - Click on "Sign up" 
        *Once you have Created a Spotify Account:
            - Click on "CREATE AN APP"
            - FILL OUT the FORUM
            - Copy the Client id and Client Secret
            - In cloud9 create a .env file in the main directory, then open it and store the key there exactly like shown below. 
             -ex. export CLIENT_ID ='ENTER THE CLIENT ID OBTAINED FROM SPOTIFY'
             -Do the same for the Client Secret ID
***

# __4.) Setting up - (Main Python File) :__
    Step 1.) Importing Libraries on top of the main python file(Importance of Each library is stated above):
        - import requests
        - import os
        - import json
        - from random import randint
        - from flask import Flask, render_template
        - from dotenv import load_dotenv, find_dotenv
    
    Step 2.) find and load .env file:
        - Type this exactly in your main python file:
            load_dotenv(find_dotenv() //this will import the API Keys to the main python file.
        
        *Authentication Section(Post-Method): 
         -In order to fetch data from spotify we first have to obtain a access token using the requests.post() method.
            
            -The target URL to send the post request to is: 'https://accounts.spotify.com/api/token'
            
            -The Post URL Is built using the following
            ex.
            Auth_Params={
                'grant_type': 'client_credentials',
                'client_id': os.getenv('CLIENT_ID'),
                'client_secret': os.getenv('CLIENT_SECRET')
            }
            
            -After the URL is bulit we can use a post request to send it and in return it will provide us response:
            ex.
                Auth_Response = requests.post(
                    Auth_URL, data=Auth_Params)
            
            -Then we can parse the access_token using Json:
                ex.
                Access_Token = Auth_Response.json()['access_token']
                
        *Fetching Artist Tracks, Track Pics and Track Preview based on Artist ID(GET-Method):
            Step 1: store a list of your Favorite Artist ID. 
                -To obtain the Artist ID go to spotify then search up your favorite artist. After you have done that the URL would look like the:
                ex.https://open.spotify.com/artist/1Xyo4u8uXC1ZmMpatF05PJ
                
                -here the artist id is "1Xyo4u8uXC1ZmMpatF05PJ"
                
            Step 2: Sending a GET Request to get top tracks for a specific artist id:
                -Target URL for Get Request:
                    GET_URL = 'https://api.spotify.com/v1/artists/{ID_OF_Artist}'.format(ID_OF_Artist=Artist_ID[rand_idx])
                        -here the artist id is obtain using a random number generator which generates a index value which is accessed using indexing to obtain artist id.
                - The HEADER is important an part of the GET_URL, without the header we won't be able to fetch the tracks because the header contains the access token.
                    ex.'Authorization': 'Bearer {token}'.format(token=Access_Token) //type this exctly the same.
                    
                -Now We can send a GET Request: 
                  ex.GET_Response_Data = requests.get(https://api.spotify.com/v1/artists/{ID_OF_Artist}'.format(ID_OF_Artist=Artist_ID[rand_idx]) + '/top-tracks?market=US&limit=10', header=GET_Header) 
                  
                 -After we have sent the request we will get a response returning us the data we asked for. Then we can turn that data into Json format and extract the required information that we want.
                 
                 ex.Final_Data = GET_Response_Data.json()  
                 
            Step 3.) Flask set up:
                - Follow the steps exactly:
                1.) app = Flask(__name__)   #//instance of flask named app      
                2.)@app.route('/')         #//End point to load the webpage
                
            Step 4.)Passing Extracted data to HTML:
                -In a function do this:
                    return render_template(PASS ANY EXTRACTED INFO YOU WOULD LIKE TO DISPLAT ON HTML PAGE)      
            Step 5.)Defining Port and IP to run the web app.
                app.run(port=int(os.getenv('PORT', 8080)), host=os.getenv('IP','0.0.0.0')
            )                              
        
***
# __5.) Setting up - (HTML AND CSS File) :__
    Step 1.) To use values that we passed in the render_template in HTML, we have to surround it in double curly brackets.
            ex.  <h1>{{Track Name Picked}}</h1>
    
    Step 2.) We then can link a css file to the html file using the link tag in the header section and do any styling that we want.
***  
# __6.) Technical Issues:__

    Question #1) I was having problems with loading my new version of the CSS file?
    Answer.) app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 
    
    Question #2.) I was not able to use local pictures in the project?
    Answer.) Hosted the picture on a website called cloudinary.com and then imported it using the URL.
    
    Question #3.) I was not able to load the Client id and Client Secret file from .env_secret?
    Answer.) Changed the file name to just .env and was able to load it.
    
    __Problems that still exist:__
    -Sometimes when you try to load the webpage it does not appear, but after you log out of AWS and then log back in and try it would appear.
    
     __Improving the Project in the Future:__
     -Will try to make project more interactive by adding JavaScript.
     
     -Allow users to select their favorite artist and track and load that onto the webpage.
    
            
        
                
    
    

    