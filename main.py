from pytube import YouTube
from pytube import Search

def clear_screen():
    """
    clear the screen in the command shell
    works on windows (nt, xp, Vista) or Linux
    Note: This was recommended by ZZucker. Thanks!
    """
    import os
    os.system(['clear','cls'][os.name == 'nt'])

def GetTitle(s,index):
    return s.results[index].title

def Download(vidId):
    filePath = input("Enter, where to save video(eg: C:\Somefile): ")
    resolution = input("Enter video resolution (360p,480p,720p => Always works,1080p): ")  
    print("Getting Video files...")
    myStream = vidId.streams.filter(file_extension = "mp4",res=resolution).first()
    
    """
	Failed ETA Timer but tells people not to close
	Will fix in future hopefully :D
    """
    print("Downloading video...")
    myStream.download(filePath)
    
def main():
    decision = int(input("Enter Decision(1 = Search Video by Name, 2 = Download video direct by link): " ))
    if decision == 1:
        searchVal = input("Search: ")
        search = Search(searchVal)
        clear_screen()
        print("You searched for " + searchVal + ", Here are the results: " + '\n')
        for i in range(5):
            print( str(i+1) + ". " + GetTitle(search,i))
        select = int(input("\n\nEnter the video number to download: "))
        vid = search.results[select-1] 
        Download(vid)
        clear_screen()
        print("Download Complete...")
    else:
        yturl = YouTube(input("Enter Link: ")) 
        Download(yturl)
        clear_screen()
        print("Download Complete...")
        
    print(quit)
    quit()
#
#Main Function call to run program exec
main()
