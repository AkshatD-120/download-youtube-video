# download-youtube-video
Allows to search and download YouTube video.

**How to use:**  
1.Installation:  
  >Download the project and open cmd or shell inside project and run  
  >`pip install -r requirements.txt` #This will download all the required necessary packages  
    
2.Run:  
  >Run the main.py file and just follow the prompts
   
 **NOTE: ** By defualt, It will download .mp4 videos. Currently, there is no option to choose which format to download except for to edit the code and select "format" :  
>`myStream = vidId.streams.filter(file_extension = "<YOUR FORMAT ENTER HERE>",res=resolution).first()`
 
![image](https://user-images.githubusercontent.com/98334833/208937224-1043899e-feb0-4d02-88c7-0771b0c26e63.png)
