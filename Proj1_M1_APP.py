#----------Importing Library---------#
import requests
import os
import json
from random import randint
from flask import Flask, render_template
from dotenv import load_dotenv, find_dotenv
#--------------------------------------


#=====================Exporting .env File=====================================
#Locating and Loading .env:                                                 #|    
load_dotenv(find_dotenv())                                                  #|
#=============================================================================


#=====================Spotify:Auth Section and POST Request==========================================================================
#Setting Up the Authentication to obtain the Access Token with Post Method:                                                        #|
Auth_URL = 'https://accounts.spotify.com/api/token'  #//Base url to obtain token                                                   #|
                                                                                                                                   #|
Auth_Params =  {                                                                                                                   #|
        'grant_type': 'client_credentials',     #//Defualt Grant Type                                                              #|
        'client_id': os.getenv('CLIENT_ID'),    #//CLIENT_ID exported from .env                                                    #|
        'client_secret': os.getenv('CLIENT_SECRET'),  #//CLIENT_SECERET_ID exported from .env                                      #|
    }                                                                                                                              #|
                                                                                                                                   #|
Auth_Response = requests.post(     #//Sending a post request                                                                       #|
        Auth_URL,                  #//With Auth_URL and Auth_Params                                                                #|
        data=Auth_Params                                                                                                           #|
        )                                                                                                                          #|
                                                                                                                                   #|
Access_Token = Auth_Response.json()['access_token']   #//Taking the response and turning it into Json and Accessing the token      #|
                                                                                                                                   #|
#print(Access_Token)  #// Printing out the token to be used by the user for access                                                 #|
                                                                                                                                   #|
#====================================================================================================================================

#========================Spotify:Setting up Info For GET Request============================================================================================================
#HardCoded Artist Name and ID                                                                                                                                             #|
Artist_Name=['Marshmello','The Weeknd','Zack Knight','Coldplay','Juice WRLD','Travis Scott']                                                                              #|
Artist_Pics=['https://res.cloudinary.com/ddsomtotk/image/upload/v1612675306/MM_Pic1_zmw0h0.png',                                                                          #|
             'https://res.cloudinary.com/ddsomtotk/image/upload/v1612670597/TW_Pic_omn1ux.jpg',                                                                           #|
             'https://res.cloudinary.com/ddsomtotk/image/upload/v1612675256/ZK_Pic1_wi9y7d.png',                                                                          #|
             'https://res.cloudinary.com/ddsomtotk/image/upload/v1612675243/CM_Pic_b1zert.png',                                                                           #|
             'https://res.cloudinary.com/ddsomtotk/image/upload/v1612674644/JW_pic_ltfx4d.jpg',                                                                           #|
             'https://res.cloudinary.com/ddsomtotk/image/upload/v1612670589/TS_Pic_im3jkd.jpg'                                                                            #|
            ]                                                                                                                                                             #|
Artist_ID=['64KEffDW9EtZ1y2vBYgq8T','1Xyo4u8uXC1ZmMpatF05PJ','7JMBJmGMqw4H33HECyW4QP','4gzpq5DPGxSnKTe4SA8HAU','4MCBfE4596Uoi2O4DtmEMz', '0Y5tJX1MQlPlqiwlOH1tJY']        #|
                                                                                                                                                                          #|
#Randomly using artist                                                                                                                                                    #|
rand_idx=randint(0,5)                                                                                                                                                     #|
                                                                                                                                                                          #|
#Header Section of the GET Request                                                                                                                                        #|
GET_Header = {                                                                                                                                                            #|
       'Authorization': 'Bearer {token}'.format(token=Access_Token)                                                                                                       #|
}                                                                                                                                                                         #|
#Target URL                                                                                                                                                               #|
GET_URL = 'https://api.spotify.com/v1/artists/{ID_OF_Artist}'.format(ID_OF_Artist=Artist_ID[rand_idx])                                                                    #|
                                                                                                                                                                          #|
#Query for top tracks of the artist:                                                                                                                                      #|
GET_Query = '/top-tracks?market=US&limit=10'                                                                                                                              #|
#===========================================================================================================================================================================


#=========================Spotify:Sending the GET Request and Recieving the Response============================================================================
                                                                                                                                                              #|
GET_Response_Data = requests.get(GET_URL+GET_Query, headers=GET_Header)                                                                                       #|
Final_Data = GET_Response_Data.json()                                                                                                                         #|
                                                                                                                                                              #|
                                                                                                                                                              #|
#===============================================================================================================================================================     


#======================Spotify:Extracting the info From Response================================================================================================
#Picking Random Track:                                                                                                                                        #|
Pick_Rand_Track=randint(0,9)                                                                                                                                  #|
                                                                                                                                                              #|
#Getting Artist Name:                                                                                                                                         #|
Artist_Name_Picked=Artist_Name[rand_idx]                                                                                                                      #|
#Artist_Name=Final_Data['tracks'][Pick_Rand_Track]['artists'][0]['name']                                                                                      #|
                                                                                                                                                              #|
Artist_Pic_Picked=Artist_Pics[rand_idx]                                                                                                                       #|
                                                                                                                                                              #|
#Getting Track Name:                                                                                                                                          #|
Track_Name=Final_Data['tracks'][Pick_Rand_Track]['name']                                                                                                      #|
Track_Name_Modify=Track_Name.split('(')                                                                                                                       #|
Track_Name_Picked=Track_Name_Modify[0]                                                                                                                        #|                                                                                                                                    
                                                                                                                                                              #|
#Getting Album Pic:                                                                                                                                           #|
Album_Pic_Picked=Final_Data['tracks'][Pick_Rand_Track]['album']['images'][0]['url']                                                                           #|
                                                                                                                                                              #|
#Getting Album Preview_URL:                                                                                                                                   #|
Track_Preview_Picked=Final_Data['tracks'][Pick_Rand_Track]['preview_url']                                                                                     #|
                                                                                                                                                              #|
                                                                                                                                                              #|                                                                                                      
#===============================================================================================================================================================


#========================GENIUS:Setting up Info For GET Request=================================================================================================
Genius_Token = os.getenv('Genius_Token')                                                                                                                      #|
                                                                                                                                                              #|
Genius_GET_URL='https://api.genius.com/search'                                                                                                                #|
                                                                                                                                                              #|
Genius_GET_Header = {                                                                                                                                         #|                                                          
      'Authorization': 'Bearer {genius_token}'.format(genius_token=Genius_Token)                                                                              #|                                          
}                                                                                                                                                             #|
Genius_Params =  {                                                                                                                                            #|             
         'q': Track_Name_Picked + ' ' + Artist_Name_Picked                                                                                                    #|
}                                                                                                                                                             #|
                                                                                                                                                              #|
Genius_GET_Response_Data = requests.get(Genius_GET_URL, data=Genius_Params, headers=Genius_GET_Header)                                                        #|
                                                                                                                                                              #|
Genius_Data=Genius_GET_Response_Data.json()                                                                                                                   #|
                                                                                                                                                              #|
try:                                                                                                                                                          #|
    Track_Lyrics_Link = Genius_Data['response']['hits'][0]['result']['url']                                                                                   #|
    Track_Lyrics_Check=True                                                                                                                                   #|
except (IndexError):                                                                                                                                          #|
    Track_Lyrics_Link = "Lyrics Link Not Able"                                                                                                                #|                                                                                                                                 #|
                                                                                                                                                              #|
#===============================================================================================================================================================


#==================Creating FLASK===============================================================================================================================
app = Flask(__name__)   #//instance of flask named app                                                                                                        #|
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0                                                                                                                   #|
@app.route('/')         #//End point to load the webpage                                                                                                      #|
#===============================================================================================================================================================                                                                                       

#===================Display Content Section(HTML AND CSS)==================================================
def Display_Content():                                                                                   #|
                                                                                                         #|
    return render_template(                                                                              #|
        "Proj1M1_HTML.html",                                                                             #|
        Artist_Name_Picked=Artist_Name_Picked,                                                           #|
        Artist_Pic_Picked=Artist_Pic_Picked,                                                             #|
        Track_Name_Picked=Track_Name_Picked,                                                             #|
        Album_Pic_Picked=Album_Pic_Picked,                                                               #|
        Track_Preview_Picked=Track_Preview_Picked,                                                       #|
        Track_Lyrics_Check=Track_Lyrics_Check,                                                           #|
        Track_Lyrics_Link=Track_Lyrics_Link                                                              #|
    )                                                                                                    #|
#==========================================================================================================
#==================Running the webpage on a specific port and ip addresss=============
app.run(                                                                            #|
port=int(os.getenv('PORT', 8080)),                                                  #|
host=os.getenv('IP','0.0.0.0'),                                                     #|
debug=True                                                                          #|
)                                                                                   #|
#=====================================================================================