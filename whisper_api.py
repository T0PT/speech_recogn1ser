import whisper
import converter

def workflow(input: str, model: str):
    converter.m4a_to_wav(input, "temp.wav")

    # Load the Whisper model (choose a model size: tiny, base, small, medium, large)
    model = whisper.load_model(model)

    # Specify the path to your .WAV file
    audio_file = "temp.wav"

    # Transcribe the audio
    result = model.transcribe(audio_file)

    # Extract segments with timestamps
    segments = result["segments"]

    # Write the transcription with timestamps to a .txt file
    output_file = "temp.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        for segment in segments:
            start = format_time(segment["start"])
            end = format_time(segment["end"])
            text = segment["text"]
            f.write(f"[{start} - {end}] {text}\n")

    print(f"Transcription saved to {output_file}")

def format_time(seconds):
    minutes, seconds = divmod(int(seconds), 60)
    return f"{minutes:02}:{seconds:02}"

workflow("lengle.m4a", "medium")