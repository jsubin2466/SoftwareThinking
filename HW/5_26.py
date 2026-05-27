import os

def get_files(path):

    files = []
    for entry in os.scandir(path):
        if entry.is_file():
            files.append(entry)
    return files

def compare(files1, files2):

    #파일 수 비교
    if len(files1) != len(files2):
        print("길이 다름")
        return 0
    
    #파일 이름 비교
    names1 = [entry.name for entry in files1]
    names2 = [entry.name for entry in files2]

    if names1 != names2:
        print("이름 다름")
        return 0
    
    #파일 크기 비교
    size1 = [entry.stat().st_size for entry in files1]
    size2 = [entry.stat().st_size for entry in files2]

    if size1 != size2:
        print("파일크기 다름")
        return 0

    #파일 내용 비교
    contents1 = []
    contents2 = []
    for entry1, entry2 in zip(files1, files2):
        with open(entry1.path, "r") as f:
            contents1.append(f.read())
        with open(entry2.path, "r") as f:
            contents2.append(f.read())

    if contents1 != contents2:
        print("내용 다름")
        return
    
    print("같다")

base1 = input()
base2 = input()

files1 = get_files(base1)
files2 = get_files(base2)

compare(files1, files2)
