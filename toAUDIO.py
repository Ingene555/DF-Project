""" 
This library will be used for conversion into audio
A class per file type will be defined
"""

import mainFunctions as mf
import os
from datetime import datetime as dt
import librosa
import numpy as np
import soundfile as sf
from pydub import AudioSegment
from pydub.effects import normalize
from scipy.signal import butter, lfilter
from moviepy import VideoFileClip

TEMPCACHES = "tempcaches"

def normalize(data):
    return data / np.max(np.abs(data))


def a_convert(pathF, pathT=None, modify={}):
    if not pathT:pathT = f"{TEMPCACHES}/tc-{dt.now()}.wav".replace(":", "")
    """
    modify={
        "interval":[0, "end"],
        "reverse":False,
        "echo":0,
        "reverb":0,
        "flanger":0,
        "chorus":0,
        "basse":0,
        "ampli":1,
        "volume":1,
        "speed":1,
        "pitch":0,
        "balance":0,
        "fadein":0,
        "fadeout":0,
        "bits":16,
        "ext":"mp3",
        "stereo":True
        }"""
    """
    - interval (list): ["start", "end"]
    - Définir une plage temporelle de l'audio. 
    - "start": temps de début en secondes (par défaut 0).
    - "end": temps de fin en secondes ou "end" pour la fin du fichier (par défaut "end").

    - reverse (bool): False
    - Inverser l'audio si activé (par défaut False).
    - Valeurs possibles : True ou False.

    - echo (float): 0
    - Ajouter un effet d'écho, valeur entre 0 et 1 (par défaut 0).

    - reverb (float): 0
    - Ajouter un effet de réverbération, valeur entre 0 et 1 (par défaut 0).

    - flanger (float): 0
    - Ajouter un effet flanger, valeur entre 0 et 1 (par défaut 0).

    - chorus (float): 0
    - Ajouter un effet chorus, valeur entre 0 et 1 (par défaut 0).

    - basse (float): 0
    - Ajouter un effet de basse (filtrage des basses fréquences), valeur entre 0 et 1 (par défaut 0).

    - ampli (float): 1
    - Amplification de l'audio, valeur par défaut 1 (aucune amplification).
    - Valeurs possibles : de 0 (silence total) à une valeur élevée sans limite théorique (amplification élevée pouvant provoquer de la distorsion).

    - volume (float): 1
    - Réglage du volume global, valeur par défaut 1.
    - Valeurs possibles : de 0 (silence total) à une valeur élevée, avec distorsion possible à des valeurs trop élevées.

    - speed (float): 1
    - Modifier la vitesse de lecture de l'audio (par défaut 1).
    - Valeurs possibles : de 0.01 (très lent) à aucune limite théorique pour des vitesses élevées.

    - pitch (int): 0
    - Modifier le pitch de l'audio (hauteur tonale). Valeur entre -12 et 12 (par défaut 0).

    - balance (float): 0
    - Modifier l'équilibre gauche/droit. 
    - Valeurs possibles : de -1 (tout à gauche) à 1 (tout à droite), 0 pour une balance égale (par défaut 0).

    - fadein (float): 0
    - Durée en secondes pour un fondu en entrée (par défaut 0).
    - Valeurs possibles : de 0 à la durée totale de l'audio.

    - fadeout (float): 0
    - Durée en secondes pour un fondu en sortie (par défaut 0).
    - Valeurs possibles : de 0 à la durée totale de l'audio.

    - bits (int): 16
    - Profondeur en bits du fichier exporté, par défaut 16.
    - Valeurs possibles : de 8 (qualité inférieure) à 32 (qualité supérieure).

    - ext (str): "mp3"
    - Format de fichier de sortie (par défaut "mp3").
    - Valeurs possibles : "mp3", "wav", "flac", "aac", "m4a", etc.

    - stereo (bool): True
    - Définir l'audio en stéréo ou mono (par défaut True).
    - Valeurs possibles : True (stéréo) ou False (mono).
    """
    interval = modify.get("interval", [0, "end"])
    reverse = modify.get("reverse", False)
    echo = modify.get("echo", 0)
    reverb = modify.get("reverb", 0)
    flanger = modify.get("flanger", 0)
    chorus = modify.get("chorus", 0)
    basse = modify.get("basse", 0)
    ampli = modify.get("ampli", 1)
    volume = modify.get("volume", 1)
    speed = modify.get("speed", 1)
    pitch = modify.get("pitch", 0)
    balance = modify.get("balance", 0)
    fadein = modify.get("fadein", 0)
    fadeout = modify.get("fadeout", 0)
    bits = modify.get("bits", 16)
    outputExt = modify.get("ext", "mp3")
    audiostereo = modify.get("stereo", True)
    pathF = os.path.abspath(pathF)
    pathT = os.path.abspath(pathT)
    data, sr = librosa.load(pathF, sr=None, offset=interval[0], duration=interval[1] - interval[0] if interval[1] != "end" else None)
    if reverse:
        data = data[::-1]
    if echo > 0:
        delay_samples = int(echo * sr)
        echo_audio = np.pad(data, (delay_samples, 0), mode='constant', constant_values=0)
        data = data + echo_audio[:len(data)] * 0.6
    if reverb > 0:
        data = normalize(data)
    if flanger > 0:
        delay_samples = int(0.01 * sr)
        data = np.roll(data, delay_samples) * flanger + data * (1 - flanger)
    if chorus > 0:
        delay_samples = int(0.03 * sr)
        data = np.roll(data, delay_samples) * chorus + data * (1 - chorus)
    if basse > 0:
        cutoff_freq = 250
        b, a = butter(5, cutoff_freq / (0.5 * sr), btype='low')
        data = lfilter(b, a, data)
    if ampli != 1:
        data = data * ampli
    if volume != 1:
        data = data * volume
    if speed != 1:
        data = librosa.effects.time_stretch(data, rate=speed)
    if pitch != 0:
        data = librosa.effects.pitch_shift(data, sr=sr, n_steps=pitch)
    if balance != 0:
        left_channel = data[::2]
        right_channel = data[1::2]
        if len(left_channel) != len(right_channel):
            min_len = min(len(left_channel), len(right_channel))
            left_channel = left_channel[:min_len]
            right_channel = right_channel[:min_len]
            left_channel *= (1 - balance)
            right_channel *= balance
            data = np.column_stack((left_channel, right_channel))
    if fadein > 0:
        fadein_samples = int(fadein * sr)
        fadein_effect = np.linspace(0, 1, fadein_samples)
        data[:fadein_samples] *= fadein_effect
    if fadeout > 0:
        fadeout_samples = int(fadeout * sr)
        fadeout_effect = np.linspace(1, 0, fadeout_samples)
        data[-fadeout_samples:] *= fadeout_effect
    if bits == 16:
        data_int = np.int16(data / np.max(np.abs(data)) * 32767)
        sample_width = 2
    elif bits == 32:
        data_int = np.int32(data / np.max(np.abs(data)) * 2147483647)
        sample_width = 4
    elif bits == 64:
        data_int = np.int64(data / np.max(np.abs(data)) * 9223372036854775807)
        sample_width = 8
    if audiostereo:
        data_int = np.column_stack((data_int, data_int))
    output_file = f"{pathT}"
    if outputExt != "wav":
        temp = f"{TEMPCACHES}/tc-{dt.now()}.wav".replace(":", "")
        audio_segment = AudioSegment(
            data_int.tobytes(),
            frame_rate=sr,
            sample_width=sample_width,
            channels=2 if audiostereo else 1
        )
        audio_segment.export(temp, format="wav")
        d, s = sf.read(temp)
        if outputExt == "aif":outputExt = "aiff"
        if outputExt in ["", "aac", "m4a"]: outputExt = "wav"
        sf.write(output_file, d, s, format=outputExt)
    else:
        audio_segment = AudioSegment(
            data_int.tobytes(),
            frame_rate=sr,
            sample_width=sample_width,
            channels=2 if audiostereo else 1
        )
        audio_segment.export(output_file, format="wav")
    return output_file


def v_convert(pathF, pathT=None):
    if not pathT:pathT = f"{TEMPCACHES}/tc-{dt.now()}.wav".replace(":", "")
    video = VideoFileClip(pathF)
    audio = video.audio
    temp = pathT.replace(":", "")
    audio.write_audiofile(temp, codec='pcm_s16le')
    return temp


class AudioToAudio:

    def __init__(self, file):
        self.file = file if type(file) == list else [file]
        self.stop = False
        self.progressShow = None

    def toAUDIO(self, path, modify={}):
        path = path if type(path) == list else [path]
        modify = modify if type(modify) == list else [modify]
        while len(modify) < len(path):
            modify.append({})
        _ = list()
        for xx, ww in enumerate(self.file):
            if not self.stop:
                ext = mf.getExtension(path[xx])
                ext = mf.Return(ext).getValues(0) if mf.Return(ext).getSucced() else "mp3"
                modify[xx]["ext"] = ext
                try:
                    a_convert(ww, path[xx], modify[xx])
                    _.append(mf.setReturn(True, [type(path[xx])], [path[xx]]))
                except Exception as e:
                    _.append(mf.setReturn(False, [type(e)], [e]))
                if self.progressShow:
                    self.progressShow(int(xx * 100 / len(path)))
            else:
                for i in _:
                    try:
                        os.remove(mf.Return(i).getValues(0))
                    except:pass
                _=[]
                break
        if self.progressShow:
            self.progressShow(100, True, self.stop, _)
        return _

    def kill(self):
        self.stop = True


class VideoToAudio:

    def __init__(self, file):
        self.file = file if type(file) == list else [file]
        self.stop = False
        self.progressShow = None

    def toAUDIO(self, path, modify={}):
        path = path if type(path) == list else [path]
        modify = modify if type(modify) == list else [modify]
        while len(modify) < len(path):
            modify.append({})
        _ = list()
        for xx, ww in enumerate(self.file):
            if not self.stop:
                if self.progressShow:
                    self.progressShow(int(xx * 100 / len(path)))
                temp = v_convert(ww)
                ext = mf.getExtension(path[xx])
                ext = mf.Return(ext).getValues(0) if mf.Return(ext).getSucced() else "mp3"
                modify[xx]["ext"] = ext
                try:
                    a_convert(temp, path[xx], modify[xx])
                    _.append(mf.setReturn(True, [type(path[xx])], [path[xx]]))
                except Exception as e:
                    _.append(mf.setReturn(False, [type(e)], [e]))
                if self.progressShow:
                    self.progressShow(int(xx * 100 / len(path)), 100)
            else:
                for i in _:
                    try:
                        os.remove(mf.Return(i).getValues(0))
                    except:pass
                _=[]
                break
        if self.progressShow:
            self.progressShow(100, True, self.stop, _)
        return _

    def kill(self):
        self.stop = True


class MixedToAudio:

    def __init__(self, *file):
        self.stop = False
        self.file = [*file]
        n = False
        for ww in self.file:
            if type(ww) != list:
                n = True
                break
        if n:self.file = [self.file]
        self.progressShow =None

    def Convert(self, pathF):
        __ = list()
        for xx, ww in enumerate(pathF):
            if not self.stop:
                if self.progressShow:
                    self.progressShow(int(xx * 100 / len(pathF)))
                _ = list()
                try:
                    for yy, zz in enumerate(ww):
                        if not self.stop:
                            if zz[0]=="video" :
                                temp = a_convert(v_convert(zz[1]))
                            else:
                                temp = a_convert(zz[1])
                            _.append(temp)
                            if self.progressShow:
                                self.progressShow(int(yy * 100 / len(ww)))
                        else:break
                    signals = []
                    for file in _:
                        data, sr = librosa.load(file, sr=44100)  # 44.1kHz
                        signals.append(data)
                        type(sr)
                    combined_signal = np.concatenate(signals, axis=0)
                    tmp = f"{TEMPCACHES}/tc-mdio-{xx}-{dt.now()}.wav".replace(":", "")
                    sf.write(tmp, combined_signal, 44100)  # 44.1kHz
                    for fi in _:
                        try:
                            os.remove(fi)
                        except Exception as e:
                            print(e)
                    __.append(mf.setReturn(True, [type(tmp)], [tmp]))
                except Exception as e:
                    __.append(mf.setReturn(False, [type(e)], [e]))
            else:
                for i in __:
                    try:
                        os.remove(mf.Return(i).getValues(0))
                    except:pass
                break
        if self.progressShow:
            self.progressShow(100)
        return __

    def toAUDIO(self, path):
        temp = self.Convert(self.file)
        path = path if type(path) == list else [path]
        _ = list()
        for xx, ww in enumerate(temp):
            if not self.stop:
                if mf.Return(ww).getSucced():
                    ext = mf.getExtension(path[xx])
                    ext = mf.Return(ext).getValues(0) if mf.Return(ext).getSucced() else "mp3"
                    try:
                        a_convert(mf.Return(ww).getValues(0), path[xx], modify={"ext":ext})
                        _.append(mf.setReturn(True, [type(path[xx])], [path[xx]]))
                    except Exception as e:
                        _.append(mf.setReturn(False, [type(e)], [e]))
                else:
                    _.append(ww)
            else:
                for i in _:
                    try:
                        os.remove(mf.Return(i).getValues(0))
                    except:pass
                _=[]
        if self.progressShow:
            self.progressShow(100, True, self.stop, _)
        return _

    def kill(self):
        self.stop = True









