#add your files in Pdfs Folder
import subprocess
from os import listdir,mkdir,getcwd, system
from os.path import isfile, join,exists
from PyPDF2 import PdfFileMerger,PdfFileReader,PdfFileWriter
from cv2 import split




def PDFsplit(pdf):
    #this fun filter the duplicate value from list 
    def Filter(sdict,pages):
        vdict=[val for val in sdict if val <= pages]
        return list(set(vdict))
    #if total pages is 8 you put 2 then it slice 0-2 and 3-8
    pages = list(map(int,input("Enter the Index of the Pdf : ").split()))
    # reading the file
    pdfFileObj = open(pdf, 'rb')
     
    # creating pdf reader object
    pdfReader = PdfFileReader(pdfFileObj)

    splits=Filter(pages,pdfReader.numPages)
    # starting index of first slice
    start = 0
     
    # starting index of last slice
    end = splits[0]
    splits.append(pdfReader.numPages)
    for i in splits:
        # creating pdf writer object for (i+1)th split
        pdfWriter = PdfFileWriter()
        # output pdf file name
        outputpdf = pdf.split('.pdf')[0] +'_'+ str(i) + '.pdf'
        print(outputpdf)
        # adding pages to pdf writer object
        for page in range(start,end):
            pdfWriter.addPage(pdfReader.getPage(page))
         
        # writing split pdf pages to pdf file
        with open(outputpdf, "wb") as f:
            pdfWriter.write(f)
 
        # interchanging page split start position for next split
        start = end
        try:
            # setting split end position for next split
            end = splits[i+1]
        except IndexError:
            # setting split end position for last split
            end = pdfReader.numPages
         
    # closing the input pdf file object
    pdfFileObj.close()


def PDFmerge(pdffiles):
    resultFile=input("Enter the name of the result file : ")
#Input the name of the result file
    if '.pdf' not in resultFile:
        resultFile += '.pdf'
    # quit()
#Append the pdf files
    merger = PdfFileMerger(strict=False)
    for pdf in pdffiles:
        merger.append(path+'/'+pdf)

#If the Output directory does not exist then create one
    if not exists(path+'/Output'):
        mkdir(path+'/Output')

#Write the merged result file to the Output directory
    merger.write(path+'/Output/'+resultFile)
    merger.close()

#Launch the result file
    print('\n'+resultFile,'Successfully created!!! at ',path+'Output/')
    filepath=path+'Output/'+resultFile
    system(filepath)
    # subprocess.Popen(["open",filepath])
def switch(x,pdffiles):
    print(' ')
    path = getcwd()+'/Pdfs/'
    if(x=='1'):
        PDFmerge(pdffiles)
    elif(x=='2'):
        for i in pdffiles:
            PDFsplit(path+i)
    else :
        print("Enter the valid value or ctrl+c to exit")
      
#Input file path and print the pdf files in that path
if __name__ == "__main__":
    print('''
    1.PDFMERGE
    2.PDFSPLIT
    ''')
    choice = input("Enter the Choice : ")
    path = getcwd()+'/Pdfs/'
    pdffiles = [f for f in listdir(path) if isfile(join(path, f)) and '.pdf' in f]
    print('\nList of PDF Files:\n')
    for file in pdffiles:
        print(file)
    switch(choice,pdffiles)
