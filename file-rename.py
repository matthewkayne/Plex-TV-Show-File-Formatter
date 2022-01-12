import os

def rename(showname,season,filetype):
    
    directory = os.listdir()
    directory.remove("file-rename.py")
    files=len(directory)

    for i in range(files):
        if season < 10:
            seasonString="0"+str(season)
        else:
            seasonString = str(season)
        if i < 10:
            episodeString="0"+str(i+1)
        else:
            episodeString=str(i+1)
            
        filename = f"{showname} - s{seasonString}e{episodeString}{filetype}"
        print(f"Before Renaming: {os.listdir()}")
        os.rename(directory[i], filename)
        print(f"After Renaming: {os.listdir()}")
   
rename("The Simpsons",2,".mp4")



