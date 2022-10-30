# Reads playlist files line by line and notifies if a line is too long.

import glob, os # for file list


def getFileList(playlistFileDirectory):
    playlistFiles = []
    #os.chdir(playlistFileDirectory)
    #for file in glob.glob('*.m3u8'):
    #    playlistFiles.append(file)
        
    for root, dirs, files in os.walk(playlistFileDirectory):
        for file in files:
            if file.endswith(".m3u8"):
                playlistFiles.append(os.path.join(root, file))
            
        
    return playlistFiles
    
    
def checkLines(playlistFiles):
    maxLength = 200
    for playlistFile in playlistFiles:
        with open(playlistFile, encoding="utf8") as file:
            lineNumber = 0
            for line in file:
                lineNumber += 1
                if len(line.strip()) >= maxLength:
                    print(f"Playlist: {file.name}")
                    print(f"Line #  : {lineNumber} longer than {maxLength}")
                    print(line.rstrip())
                    print("\n")


def main():
    playlistFileDirectory = "./Master/320"
    playlistFiles = getFileList(playlistFileDirectory)
    checkLines(playlistFiles)

   
if __name__=="__main__":
    main()