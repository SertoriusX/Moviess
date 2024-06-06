# myapp/utils.py
import pysrt
import os
from pathlib import Path

def convert_srt_to_vtt(srt_path):
    encodings = ['utf-8', 'iso-8859-1', 'windows-1252']
    
    for encoding in encodings:
        try:
            print(f"Trying encoding: {encoding}")
            subs = pysrt.open(srt_path, encoding=encoding)
            break
        except UnicodeDecodeError:
            print(f"Failed with encoding: {encoding}")
            continue
    else:
        raise ValueError("Unable to decode the subtitle file with the given encodings.")

    vtt_content = 'WEBVTT\n\n'

    for sub in subs:
        start = sub.start.to_time()
        end = sub.end.to_time()
        vtt_content += f'{start.hour:02}:{start.minute:02}:{start.second:02}.{start.microsecond // 1000:03} --> '
        vtt_content += f'{end.hour:02}:{end.minute:02}:{end.second:02}.{end.microsecond // 1000:03}\n'
        vtt_content += f'{sub.text}\n\n'

    vtt_path = Path(srt_path).with_suffix('.vtt')
    with open(vtt_path, 'w', encoding='utf-8') as vtt_file:
        vtt_file.write(vtt_content)

    print(f"VTT file created at: {vtt_path}")
    return vtt_path
