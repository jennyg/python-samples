#!/usr/bin/python3

#script for 7 word story processing :)
#these were formatted like Firstname Lastname: Seven word quote**
#output cleaned up version with just the seven word quote formatted to add
#to javascript array
   
def strip_attributions(line):
   #strips attributions, found before colon, from given string
   if ":" in line:
      stripped_line = line.split(": ")[1]
   else:
      stripped_line = line
   return stripped_line
   
def remove_chars(line):
   #strips asterisk and newline character(s)
   stripped_line = line.replace("*","");
   stripped_line = stripped_line.replace("\n","")
   return stripped_line

#read from annoying file, write to fixed file

source_file = open("7word.txt", "r")

#this empty string will be added to and written to the new file
to_write = ""

for line in source_file:
   fixed_line = remove_chars(line)
   fixed_line = strip_attributions(fixed_line)
   #formats with quotation marks and newline
   to_write += "\"" + fixed_line + "\","  + "\n"
   
output_file = open("fixed7words.txt", "w")

output_file.write(to_write)

output_file.close()
