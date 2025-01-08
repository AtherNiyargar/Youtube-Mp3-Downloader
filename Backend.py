import yt_dlp
import ffmpeg
import os

class Backend:

    title = ""
    def __init__(self, url):
        self.url = url
        self.y_downloader = yt_dlp.YoutubeDL({'quiet' : True, 'listformats' : False})

    def title_provider(self) -> str:
        return self.y_downloader.extract_info(self.url, download = False).get('title', None)

    def downloader(self, title):
        options = {
            'format' : 'bestaudio/bestaudio',
            'outtmpl' : './youtube_mp3s/%(title)s.%(ext)s'
        }
        yt_dlp.YoutubeDL(options).download([self.url])
        
        input_file = f"./youtube_mp3s/{title}.webm"
        print(title+".webm")
        output_file = f"./youtube_mp3s/{title}.mp3"
        try:
            (
                ffmpeg
                .input(input_file)
                .output(output_file)
                .run()
            )
            print(f"Conversion successful! Audio saved as '{output_file}'")
        except:
            print(f"An error occurred!")
        finally:
            os.remove(f"./youtube_mp3s/{title}.webm")
            
if __name__ == "__main__":
    backend = Backend("https://youtu.be/yKNxeF4KMsY?feature=shared")
    print(backend.title_provider())
