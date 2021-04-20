from zipfile import ZipFile

file_name = '11.FIA1___Creating_with_Code___Investigation_Finale39.zip'
with ZipFile (file_name, 'r') as zip:
    zip.printdir()
   
    zip.extractall('marking_folder')
    