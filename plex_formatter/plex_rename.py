"""Plex Rename"""
import os


def rename():
    """Rename"""
    path = input("Path to folder (Enter if current directory): ")
    show_name = input("Show Name: ")
    season = int(input("Season: "))
    file_type = input("File Type: ")

    if path == "":
        directory = [f for f in os.listdir() if not f.startswith('.')]
        directory.remove("file-rename.py")
    else:
        directory = [f for f in os.listdir(path) if not f.startswith('.')]

    files = len(directory)

    for i in range(files):
        if season < 10:
            season_string = "0"+str(season)
        else:
            season_string = str(season)
        if i < 10:
            episode_string = "0"+str(i+1)
        else:
            episode_string = str(i+1)

        file_name = f"{path}{show_name} - s{season_string}e{episode_string}.{file_type}"

        os.rename(f"{path}{directory[i]}", file_name)


if __name__ == "__main__":
    rename()
