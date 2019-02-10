# Read files content with 'read' function on Microsoft Windows

file = open('C:\practice_1.txt')
file = file.read()
file

# Read files content with 'readlines' function on Microsoft Windows

file = open('C:\practice_1.txt')
file = file.readlines()
file

# Writing to files with write 'w' on Linux

bacon_File_1 = open('/home/jpromano/Documents/firstwrite.ods', 'w')
bacon_File_1 = open('/home/jpromano/Documents/firstwrite.txt', 'w')
bacon_File_1.write('Hello human!')
bacon_File_1.close()

# Writing files with append 'a' on Linux

bacon_File_1 = open('/home/jpromano/Documents/firstwrite.ods', 'a')
bacon_File_1.write('Hello human!\n')
bacon_File_1.close()
