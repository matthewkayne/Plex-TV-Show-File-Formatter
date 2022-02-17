import os

def rename(showname,season,filetype,path):
    if path == "":
        directory = os.listdir()
        directory.remove("file-rename.py")     
    else:  
        directory = os.listdir(path)   
      
    files = len(directory)

    for i in range(files):
        if season < 10:
            seasonString="0"+str(season)
        else:
            seasonString = str(season)
        if i < 10:
            episodeString="0"+str(i+1)
        else:
            episodeString=str(i+1)
            
        filename = f"{path}{showname} - s{seasonString}e{episodeString}{filetype}"
    
        os.rename(f"{path}{directory[i]}", filename)

    print(f"Before Renaming: {directory}")
    print(f"After Renaming: {os.listdir(path)}")

inPath = input("Path for Shows (Enter for current directory): ")
inShowName = input("Show Name: ")
inSeason = int(input("Season: "))
inFileType = "."+input("File Type: ")

rename(inShowName,inSeason,inFileType,inPath)