import yt_dlp
from yt_dlp.postprocessor.common import PostProcessor

class MyCustomPP(PostProcessor):
    def run(self, info):
        self.to_screen('Doing stuff')
        return [], info

ydl_opts ={
    'format': 'bestaudio',
    'outtmpl': '%(title)s.%(ext)s',
    'forcefilename': 'True',

    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '0',
        
    }],
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.add_post_processor(MyCustomPP())
    info = ydl.extract_info("https://www.youtube.com/watch?v=7PDUO3l8xiM", download = True)
print(ydl.prepare_filename(info))