#modules
import os
from PIL import Image

#function for compress the image
def compresstheimage(filename,quality,fileformat):
	filepath = os.path.join(os.getcwd(),
							filename)
	picture = Image.open(filepath)
	picture.save("Compressed_"+filename,
				str(fileformat),
				optimize = True,
				Quality = int(quality))
				#dir name is to find file path of parent
	return os.path.dirname(filepath)+"/Compressed_"+filename

def main():
	# to rectifiy the error
	while True:
		try:
			Filepath=input("Enter image path :")
			imgpath=Image.open(Filepath)
			break
		except FileNotFoundError:
			print("file Not found in this path....")
			continue
		except:
			print("Enter Valid Image Format.....")
			continue
	while True:
		try:
			Quality=int(input("Quality of image enter between 10 to 100: "))
			if ( Quality<10 or Quality>100 ):
				raise Exception("Enter between 10 to 100")
			break
		except:
				print("Enter the Valid Number.....")
				continue
#to find last name of the filepath
	Filename = os.path.basename(Filepath)
	print('compressing', Filename)
	print(f'Image Stored at the path of {compresstheimage( Filename,Quality,imgpath.format)}')

# Driver code
if __name__ == "__main__":
	main()
