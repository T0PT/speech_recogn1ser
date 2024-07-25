So, this is a small program I made for my mum.
She needed to transcribe a lot of text from video and do it locally, so here it is.
It uses whisper from OpenAI as a working model, you can also choose the appropriate size for you.
Right now it works with mkv, wav, mp3 and flec, I didn't spend lots of time on it yet, so don't judge too hard :)

You can download and give it a shot, here is a small instruction on how to do that:
1. You have to have python installed, I guess every version from 3.8 should work.
2. You have to have Chocolatey installed.
3. Clone this repository to your machine.
4. Run setup.bat as an admin(for chocolatey) - it will download and install all neccessary dependencies. You have to do this step only once.
5. You have to have torch version 2.3.1 or any other, that would work, 2.4.0 doesn't work :(
6. You have to have numpy version 1.26.4 or any other, that would work, 2.0.1 doesn't work :(
7. After that you can just run start.bat and you have it going
