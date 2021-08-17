import os
import shutil 
def Folders():
          original_path = source+"Folders/"+ f
          sources=source+f
          shutil.move(sources,original_path)
def zipfile():
         original_path = source+"Zip_file/"+ f
         sources=source+f
         shutil.move(sources,original_path)
def Appfile():
         original_path = source+"Application/"+ f
         sources=source+f
         shutil.move(sources,original_path)
if __name__ == "__main__":
   path = 'C:/Users/nithin/Downloads'
   source = r'C:/Users/nithin/Downloads/'
   files = os.listdir(path)
   for f in files:
       if (("." in f)==False)and(f!="Folders")and(f!="Zip_file")and(f!="Application"):
          Folders()
       elif f.endswith('.zip'):
           zipfile() 
       elif f.endswith('.exe'):
           Appfile() 
          
      