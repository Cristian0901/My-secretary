from PIL import Image
import os

download_folder = "/home/cristian/Downloads/"
music_folder = "/home/cristian/Music/"
images_folder = "/home/cristian/Pictures/"
documents_folder = "/home/cristian/Documents/"
videos_folder = "/home/cristian/Videos/"

if __name__ == "__main__":
    for filename in os.listdir(download_folder):
        name, extension = os.path.splitext(download_folder + filename)
        
        #print(name, extension)
        
        #Images able to compress
        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(download_folder+filename)
            picture.save(images_folder + "compressed_" + filename, optimize=True, quality=60)
            os.remove(download_folder + filename)
            print(name + ":" + extension)
        
        #Images not able to compress
        if extension in [".gif", ".svg"]:
            os.rename(download_folder + filename, images_folder + filename)
            os.remove(download_folder + filename)
            print(name + ":" + extension)
        
        #Documents
        elif extension in [".pdf", ".epub", ".txt", ".md", ".doc", ".docx"]:
            os.rename(download_folder + filename, documents_folder + filename)
            os.remove(download_folder + filename)
            print(name + ":" + extension)
        
        #Music
        elif extension in [".mp3", ".flac", ".wav", ".aiff", ".aac", ".wma", ]:
            os.rename(download_folder + filename, music_folder + filename)
            os.remove(download_folder + filename)
            print(name + ":" + extension)
            
        #Video
        elif extension in [".mp4", ".mkv", ".webm", ".mov", ".avi", ".flv"]:
            os.rename(download_folder + filename, videos_folder + filename)
            os.remove(download_folder + filename)
            print(name + ":" + extension)

print("All is done!...")