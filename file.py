''' file handling '''

try:
    file1 = open("file.txt", '+r')

except FileNotFoundError:
    print("There was a error finding file")

else:
    fileReading = file1.read()
    print(fileReading)
    print("hello")

    file1.write("There have been many instances where I have been disturbed"
                "\n")

finally:
    file1.close()
