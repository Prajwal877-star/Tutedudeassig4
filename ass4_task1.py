


try:
    file = open('sample.txt', 'r')
    reading_file1= file.readline()
    reading_file2 = file.readline()
    print('Line 1:', reading_file1.strip())
    print('Line 2:', reading_file2)
    file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")







