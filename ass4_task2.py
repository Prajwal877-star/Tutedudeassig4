

file = open('output.txt','w')
a = input('Enter text to write to the file: ')
writing_file = file.write(a+'\n')
print('Data successfully written to output.txt.\n')
file.close()

b = input('Enter additional text to append:\n')
file = open('output.txt','a')
appending_file = file.write(b+'\n')
print('Data  successfully appended\n')
file.close()

print('Final content of output.txt:')
file = open('output.txt','r')
reading_file1 = file.read()
print(reading_file1)
file.close()

