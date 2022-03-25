from pytube import YouTube
url = "https://youtu.be/n7xF4UYrkq8"
yt = YouTube(url)
yt.streams.first().download()

#result>>>: '/Users/linyuci/康士坦的變化球 KST－美好的事可不可以發生在我身上 Lucky As You （Official Music Video）.3gpp'
