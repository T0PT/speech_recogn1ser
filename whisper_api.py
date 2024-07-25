import whisper

def transcribe(modelname):
    if modelname not in ["tiny", "small", "base", "medium"]: modelname = "tiny"
    try:
        model = whisper.load_model(modelname)
        result = model.transcribe("temp.wav")
        text = str(result["text"])

        with open("temp.txt", mode="w+", encoding="utf-8") as f:
            f.write(text)

        return True
    except Exception as e:
        print(e)
        return False