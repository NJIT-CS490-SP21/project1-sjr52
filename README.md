# **MUSIC DISCOVERY APP: _CS490-PROJECT-#1_**
***
## Table of Contents

1. Technologies, Frameworks, Libraries and API
2. Structure and Location of directory and files
3. Creating (Spotify and Genius Account) and (Hiding API KEYS) 
4. Setting up - Python File
5. Setting Up - HTML and CSS File
6. Heroku Deployment
7. Technical Issues and Solutions

***
# __1.) Technologies, Frameworks, Libraries and API :__

  ## -Technologies:
        -AWS Cloud9 IDE: Used for coding in PYTHON, HTML and CSS
        
  ## -Frameworks:
        -Python(Flask): Used for Creating a WEB SERVER
        
  ## -Libraires:
        -Requests: Used to send POST and GET request to Spotify and Genius.
        -os and dotenv: Used to export hidden .env file which contained API Key. 
        -json: Used for Parsing response recieved from Spotify and Genius.
        -random: Used to dynamically fetch and generate random track information on webpage.
        -render_template: Used to pass parameters to HTML file.
        
  ## -API:
        -Spotify API: Used to obtain artist name, song name, song picture, and preview link.
        -Genius API: Used to obtain lyrics of a song
***

# __2.) Project Structure :__

  ## Step 1: Creating a AWS Educate Account and Getting Started with Cloud 9:
  
        -AWS Educate Account (https://aws.amazon.com/education/awseducate/)
        
        -After you have created the account, on the top there is a search-bar where you should type cloud9 and it will load cloud9 IDE. 
        
  ## Step 2: Creating Project Files:
  
        1.) Create a Main Working Directory:
            - command: `mkdir directory_name`
            
        2.) Go into the directory:
            - command: `cd directory_name`
            
        3.) Python File Creation:
            - Create a python file, Where you will create the web server.
            - command: `touch (main_python_file_name).py`
              
        4.) HTML File Creation: 
            - Creating a sub-directory called templates with HTML file inside that sub-directory.
             - command: `mkdir templates` // Make sure the name of the sub-directory is templates
             - command: `cd templates`
             - command: `touch (HTML_File_Name).html`
             
        5.) CSS File Creation:
           - Creating a sub-directory and with CSS file inside that sub-directory.
              - if you are not in the main working directory, do (cd ..) this will bring you to the main directory 
              - now in the main directory do:
                 - command: `mkdir static`  //Make sure the name of the sub-directory is called static.
                 - command: `cd static`
                 - command: `touch CSS_File_Name.html`
***

# __3.) Creating a Spotify and Genius Account for API Keys :__

  ## Step 1.) Creating a Spotify Account :
        - Go To (https://developer.spotify.com/dashboard/login):
        - Click on "Sign up" 
        
        -Once you have created a Spotify Account:
            - Click on "CREATE AN APP"
            - FILL OUT the FORUM
            - Copy the Client id and Client Secret
            - In cloud9 create a .env file in the main directory, then open it and store the key there exactly like shown below. 
              - **ex. export CLIENT_ID ='ENTER THE CLIENT ID OBTAINED FROM SPOTIFY'**
              - **ex. export CLIENT_SECRET='ENTER THE CLIENT SECRET OBTAINED FROM SPOTIFY'**
             
  ## Step 2.) Creating a Genius Account :
        - Go To (https://genius.com/developers):
        - Click on "Sign up" 
        
        -Once you have created a Genius Account:
            - Click on "All API CLIENTS"
            - Click on "CLIENT ACCESS TOKEN"
            - In cloud9 open the same .env file that was created to store the spotify token and store the key there exactly like shown below. 
              - **ex. export Genius_Token ='ENTER ACCESS TOKEN OBTAINED FROM GENIUS'**
          
***

# __4.) Setting up - (Main Python File) :
  
  ## Step 1.) Importing Libraries on top of the main python file(Importance of Each library is stated earlier):
        - import requests
        - import os
        - import json
        - from random import randint
        - from flask import Flask, render_template
        - from dotenv import load_dotenv, find_dotenv
        
  ## Step 2.) finding and loading .env file:
        - Type this exactly in your main python file:
            - `load_dotenv(find_dotenv()` //this will import the API Keys to the main python file.
        
  ## Step 3.) Setting up Flask App:  
        - Follow the steps exactly:
            1.) ` app = Flask(__name__)`  #//instance of flask named app      
            2.) `@app.route('/')`         #//End point to load the webpage
            
  ## Step 4.) Create a Function Called `Display_Content()` and inside that function follow these steps below:
        
        ## !!! DO STEPS 1-3 INSIDE THE FUNCTION !!!
        
        ## - Authentication from Spotify using Post Method: 
        
            - In order to fetch data from Spotify we first have to obtain a access token using the requests.post() method.
            
            - The target URL to send the post request to is: `https://accounts.spotify.com/api/token`
            
            - The Post URL Is built using the following Parameter below :
            
                ex. `Auth_Params={
                
                        'grant_type': 'client_credentials',
                        'client_id': os.getenv('CLIENT_ID'),
                        'client_secret': os.getenv('CLIENT_SECRET')
                    }`
            
            - After the URL is bulit we can send a post request and in return it will provide us with response as shown below:
                ex. `Auth_Response = requests.post(Auth_URL, data=Auth_Params)``
            
            - Then we can parse the Access Token using Json:
                 ex. `Access_Token = Auth_Response.json()['access_token']`
                 
                
        ## - Fetching Artist Tracks, Track Pics and Track Preview based on Artist ID using GET Method:
        
          ## Step 1.) Store a list of your Favorite Artist IDs:
            
                 - To obtain the Artist ID go to Spotify then search up your favorite artist. After you have done that the URL would look similar to the one below:
                     ex. 'https://open.spotify.com/artist/1Xyo4u8uXC1ZmMpatF05PJ'
                     
                 - Here the artist id is "1Xyo4u8uXC1ZmMpatF05PJ"
                 
                 - Store these artist ids in a python list which will later be used to fetch songs from a specific artist
                 
                
          ## Step 2.) Sending a GET Request to get top tracks for a specific artist id:
            
                - Target URL for Get Request:
                 
                    GET_URL = 'https://api.spotify.com/v1/artists/{ID_OF_Artist}'.format(ID_OF_Artist=Artist_ID[rand_idx])
                    
                     - Here the artist id is obtained using a random number generator which generates a index value which is used to accesse the artist id from the artist id list which was created earlier.
                     
                        
                - The HEADER is an important part of the GET request, without the header we won't be able to fetch the tracks for a specific artist because the header contains the access token which allows a user to fetch tracks. Write the header exactly as shown below:
                
                    ex.'Authorization': 'Bearer {token}'.format(token=Access_Token) 
                    
                    
                - Now We can send a GET Request which is shown below: 
                
                    ex. `GET_Response_Data = requests.get(https://api.spotify.com/v1/artists/{ID_OF_Artist}'.format(ID_OF_Artist=Artist_ID[rand_idx]) + '/top-tracks?market=US&limit=10', header=GET_Header)`
                    
                  
                - After we have sent the request we will get a response returning data we asked for, we can then convert that data into json format and extract the required information. 
                 
                   ex. `Final_Data = GET_Response_Data.json()` 
                 
        
          ## Step 3.) Passing Extracted data to HTML:
            
                -In the function do the following:
                
                    `return render_template(PASS ANY EXTRACTED INFO YOU WOULD LIKE TO DISPLAY ON HTML PAGE)`
                    
        ## !!!DO Step 4 OutSide the function!!!
                    
            
          ## Step 4.) Defining Port and IP to run the web app. Copy the below stated code exactly the same:
            
                ex. `app.run(port=int(os.getenv('PORT', 8080)), host=os.getenv('IP','0.0.0.0')`
               
***

# __5.) Setting up - HTML AND CSS Files :__
 
  ## Step 1.) To use values that we passed in the render_template of the python file in HTML
        ex.  `<h1>{{Track Name Picked}}</h1>`
                
        -For the structure of the web page you can design it however you like!
            
  ## Step 2.) We then can link a CSS file to the html file using the link tag in the header section:
        ex.  `<link href={{url_for('static', filename='Name_OF_CSS_File')}} rel="stylesheet" />`
                
        -For the styling of the web page you can design it however you like!
***  
# __6.) Heroku Deployment :__
    
  ## Step 1.) Installing Heroku via your AWS terminal :
        ex. Command: `npm install -g heroku`
                
  ## Step 2.) Creating a Heroku Account:
  
        -Go to `https://signup.heroku.com/`
        -Sign up by inputing the information
    
  ## Step 3.) Creating `requirements.txt` and `Procfile`:
  
        -In your root directory do the following to create requirements.txt file:
            1.) command: `touch requirements.txt`         //Will create a requirements.txt file
            2.) command: `pip freeze > requirements.txt`  //Will copy all the packages used in project creation into requirements.txt file      
          
        -In your root directory do the following to create Procfile:
            1.) command: `touch Procfile`   //Will create a requirements.txt file
            2.) command: `c9 Procfile`      //Will open the Procfile
            3.) Inside the Procfile write the following command: //Will tell heroku to run the following command when deploying the webpage on web
                ex. `web: python (Your_Python_File_Name.py)`
            
  ## Step 4.) Launching the Web App with Heroku:
        
        Step 1.) Log into Heroku via Command line:
        
            - Type the following command in the cloud-9 terminal:
                ex. command: `heroku login -i`
                
            - Enter the username and password  used when signing up for the heroku:
        
            
        Step 2.) Pushing the code onto heroku:
        
            - Type the following command in the cloud-9 terminal:
                ex. command: `git push heroku main`
                
            - Now do `heroku open` this will provide you with a link the the terminal to open your web app but it will not run because heroku does not have the access to secret client ids as well as the access token.
       
        
        Step 3.) Configuring Client IDs and Access Token In the Heroku App:
            
            - Open Heroku and click on the name given to your app by heroku
            
            - Click on settings tab
            
            - Scroll down to Config Vars and click on Reveal Config Vars
            
            - Click add and copy the exact key and value pair that we have in the .env file  //Most Important
            
        -Now Your APP HAS BEEN DEPLOYED TO HEROKU!
            
*** 

# __7.) Technical Issues and Solutions:__
   
    ## Fixed Problems:
        
        Problem #1) I was having problems reflecting the changes I made to CSS file display onto the webpage, I checked everything from CSS syntax to filename being correctly referenced in the HTML file, but the problem was that the old CSS file was being cached. I even tried to do a hard refresh but it didn't work. For the Temporaray, I was changing the CSS filename so that each time a new css filename was cached. After Trying out many things the problem still remained and after few days into the project the (TA: DAVID) shared with us a single line of code which solved the problem: `app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0`.
        
        Problem #2.) I was trying to make my project more creative and more appealing but for that I needed to download pictures on my computer and style them myself. After styling and finalizing all the pictures I hit a road block when I tried to access the pictures loacted on my computer from cloud 9. I also tried to upload the pictures into the cloud 9 enviorment but still it did not let me use the pictures. I spent a whole day figuring out how I would inculcate the custom pictures into my webpage and then I thought of hosting a picture on cloudinary.com and using them via adding a source attribute in the image tag.
        
        Problem #3.) I was not able to load the Client id and Client Secret id  from my .env file. I tried changing the variable names inside the file but it still didn't work I even tried changing the name of the .env file to .env_one and etc. but it still didn't work. Then I thought it might be cloud 9 problem and after restarting it, the .env file started working.
        
        Problem #4.) When I recieved the data and turned it into Json form, I was having alot of problem extract information and it would always give me some sort of an error such as a index error and many more. In order to solve this problem I copied the Json format from the terminal and used an online JSON Formatter & Validator.
        
        Problem #5.) Another problem which I faced was that most of the times I was not gettting a response from the request I was sending to Genius, I often recieved a response 401 or response 403 error, to solve this I printed out the track names and then I found out that many times the track name was accompanied by parentheses which had other information inside it such as feat... and much more, this was messing up my search, so I used a split function and extracted only the track name and now about 90 percent of the tracks have a accurate lyrics.
        
    
    ## Problems Unsolved:
        
        -Sometimes when you try to load the webpage it does not appear, but after you log out of AWS and then log back in and try again it would appear.
        
        -One Problem with my project is that sometimes if the track name is long it overflows a little.
    
    
    ## Further Improvement On Project:
        
        -I am planning on adding a recommended songs list for a specific artist as well as planning on adding other artist who may have traits similar to the current artist that might be playing.
        
        -I am also planning on making the webpage interactive by adding a favorite list, where the user can store there favorite artist and a list of their tracks which they like.
        
        -I would also like to improve the webpage by making different UI and allowing users to choose those UI's based on their liking.
    
***         
        
                
    
    

    