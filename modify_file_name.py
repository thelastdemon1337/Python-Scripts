import os

FOLDER_PATH = r'C:\\Users\\Tarun\\Desktop\\RENAME_TEST_SUBJECTS'

def rename_files(dir):
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        old_name = FOLDER_PATH + "\\" + fileName
        new_name = old_name + ".mp4"
        print(old_name)
        if os.path.exists(FOLDER_PATH + "\\" + fileName):
            os.rename(old_name,new_name)

if __name__ == '__main__':
    rename_files(FOLDER_PATH)