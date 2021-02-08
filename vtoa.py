import moviepy.editor as mp

clip = mp.VideoFileClip('.\sample.mp4')
clip.audio.write_audiofile('ans.mp3')