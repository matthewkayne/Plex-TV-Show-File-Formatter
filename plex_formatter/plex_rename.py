import os

def rename():
    path = input("Path to folder (Enter if current directory): ")
    showname = input("Show Name: ")
    season = int(input("Season: "))
    filetype = input("File Type: ")

    if path == "":
        directory = [f for f in os.listdir() if not f.startswith('.')]
        directory.remove("file-rename.py")     
    else:  
        directory = [f for f in os.listdir(path) if not f.startswith('.')]
      
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
            
        filename = f"{path}{showname} - s{seasonString}e{episodeString}.{filetype}"
    
        os.rename(f"{path}{directory[i]}", filename)

if __name__ == "__main__":
    rename()