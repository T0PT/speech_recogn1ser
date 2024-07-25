# def mp4_to_wav(video_path, output_path):
#     import subprocess
#     from moviepy.editor import VideoFileClip
#     if not video_path.endswith('.mp4'):
#         return False
#         #raise ValueError("Input file must be a MP4 video.")
#         # Open video with MoviePy
#     command = ["ffmpeg", "-i", video_path, "-vn", output_path]
#   # Execute the ffmpeg command using subprocess
#     try:
#         subprocess.run(command, check=True)
#         return True
#     except subprocess.CalledProcessError as e:
#         raise RuntimeError(f"FFmpeg failed to convert the file: {e}") from e
#   # Assuming these methods exist for proper resource management
#         return True
#     except Exception as e:
#         print(f"Error converting file: {e}")
#         return False

def mkv_to_wav(video_path, output_path):
    import subprocess
    print("processing")
    if not video_path.endswith('.mkv'):
        return False
        raise ValueError("Input file must be a MKV video.")
    try:        
        # Use subprocess to call ffmpeg for efficient encoding
        command = f"ffmpeg -y -i {video_path} -vn {output_path}"

        # Run the command
        subprocess.run(command, shell=True, check=True)
        return True
    except Exception as e:
        print(f"Error converting file: {e}")
        return False
    
def m4a_to_wav(input_path, output_path):
    print("processing")
    from pydub import AudioSegment
    if input_path.endswith('.m4a'):
        try:
            song = AudioSegment.from_file(input_path, format="m4a")
            song.export(output_path, format="wav")
            return True
        except Exception as e:
            print(f"Error converting file: {e}")
            return False               
    else:
        return False
    
# # Replace 'video.mkv' with your actual file path
# video_path = 'video.mkv'
# # Replace 'audio.wav' with your desired output filename (including extension)
# output_path = 'audio.wav'

# # Open video with MoviePy
# video = VideoFileClip(video_path)
# audio = video.audio

# # Use subprocess to call ffmpeg for efficient encoding
# command = f"ffmpeg -i - -vn {output_path}"  # '-' for piped input

# # Pipe audio data to ffmpeg process
# process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE)
# process.stdin.write(audio.read_bytes())  # Send audio data to ffmpeg
# process.wait()  # Wait for ffmpeg to finish

# # Clean-up (optional)
# video.close()
# audio.close()  # Assuming these methods exist for proper resource management
