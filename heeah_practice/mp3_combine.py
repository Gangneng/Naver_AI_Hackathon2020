from pydub import AudioSegment

sound1 = AudioSegment.from_file("D:/Heeah/네이버 해커톤/sound1.mp3")
sound2 = AudioSegment.from_file("D:/Heeah/네이버 해커톤/sound2.mp3")

combined = sound1.overlay(sound2)

combined.export("combined.mp3", format="mp3")

