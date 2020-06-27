import os
import sys
import getpass
import shutil


def createDirectory(folder, path):
    directory = path + folder + "/"
    if not os.path.exists(directory):
        os.mkdir(directory)
        print(directory + " Created successfully.")

    return directory


def move(path, name, directoryType):
    src = path + name
    dest = directoryType + '/' + name
    shutil.move(src, dest)
    logString = "Moved " + name + " to " + directoryType
    print(logString)


def analyzeFolder(folderPath):
    # TODO: check for the contents of the folder recursively and try to figure out the type of folder this is.
    return


def organizeFolders(rootDir):
    directory = os.listdir(rootDir)

    # TODO: move to a data-driven solution using json
    # contains folders and things that couldn't be categorized
    folderDir = createDirectory("Misc Folders", rootDir)

    ignoreList = ["Images", "Documents", "Videos", "ZipArchives",
                  "Installer", "Code", "App", "Misc"]
    directory = list(set(directory).difference(set(ignoreList)))
    print(type(directory))
    for name in directory:
        if '.' in name:
            continue
        else:
            move(rootDir, name, folderDir)
    return


def organize(rootDir):
    organizeFiles(rootDir)
    organizeFolders(rootDir)


def organizeFiles(rootDir):
    # ignore folders for now
    files = os.listdir(rootDir)

    imagesDir = createDirectory("Images", rootDir)
    docsDir = createDirectory("Documents", rootDir)
    videoDir = createDirectory("Videos", rootDir)
    zipDir = createDirectory("ZipArchives", rootDir)
    dmgDir = createDirectory("Installer", rootDir)
    codeDir = createDirectory('Code', rootDir)
    appDir = createDirectory("App", rootDir)
    # contains folders and things that couldn't be categorized
    folderDir = createDirectory("Misc", rootDir)

    # TODO: move to a data-driven solution using json
    for name in files:
        # TODO: Extension check should be more robust.
        if '.png' in name or '.jpg' in name or '.tiff' in name or '.jpeg' in name:
            move(rootDir, name, imagesDir)
        elif '.pdf' in name or '.docx' in name or '.pptx' in name or '.txt' in name or '.csv' in name:
            move(rootDir, name, docsDir)
        elif '.mp4' in name or '.mkv' in name:
            move(rootDir, name, videoDir)
        elif '.zip' in name or '.rar' in name or '.tar' in name or '.7z' in name:
            move(rootDir, name, zipDir)
        elif '.dmg' in name or '.pkg' in name:
            move(rootDir, name, dmgDir)
        elif '.m' in name or '.sh' in name or '.py' in name:
            move(rootDir, name, codeDir)
        elif '.psd' in name or '.sketch' in name:
            move(rootDir, name, docsDir)
        elif '.app' in name:
            move(rootDir, name, appDir)


def main(rootDir):
    if(rootDir == 'pwd'):
        rootDir = os.getcwd()
    elif(rootDir == 'Downloads'):  # most messy folder
        # make user specifc
        rootDir = "/Users/" + getpass.getuser() + "/Downloads/"
    elif(rootDir == 'Desktop'):
        rootDir = "/Users/" + getpass.getuser() + "/Desktop/"
    if not os.path.exists(rootDir):
        print("Error: Path not found. " + rootDir + " is invalid!")
        print("argument should be an absolute path or one of the suggested shortcuts")
        print("Terminating program")
        exit()

    organize(rootDir)

    print("Organized successfully.")


if __name__ == "__main__":
    try:
        rootDir = sys.argv[1]
    except Exception:
        print("Try to run the command with arguments")
        print("Current list of arguments: Downloads, pwd")
        print("\tEg: bash organize.sh Downloads")
        exit()

    main(rootDir)
