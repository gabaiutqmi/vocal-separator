import subprocess
import os

def separate_audio(file_path):
    output_dir = file_path.replace(".mp3", "")
    command = f"demucs --two-stems=vocals -o ./separated \"{file_path}\""
    subprocess.run(command, shell=True)

    vocals_path = os.path.join("separated", "htdemucs", os.path.basename(output_dir), "vocals.wav")
    instr_path = os.path.join("separated", "htdemucs", os.path.basename(output_dir), "no_vocals.wav")
    return vocals_path, instr_path
