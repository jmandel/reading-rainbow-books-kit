# usage: uv run --with faster-whisper --with 'av>=14,<16' python whisper_vtt.py audio_file out.en.vtt
# Local transcription for episodes without YouTube captions: one VTT cue per word (exact word timings for tokens.py).
import sys
from faster_whisper import WhisperModel
audio,out=sys.argv[1:3]
model=WhisperModel('small.en',device='cpu',compute_type='int8',cpu_threads=12)
segs,_=model.transcribe(audio,word_timestamps=True,vad_filter=False,beam_size=5)
ts=lambda t:f"{int(t//3600):02d}:{int(t%3600//60):02d}:{t%60:06.3f}"
with open(out,'w') as f:
    f.write('WEBVTT\n\n')
    for s in segs:
        for w in s.words: f.write(f"{ts(w.start)} --> {ts(w.end)}\n{w.word.strip()}\n\n")
print('wrote',out)
