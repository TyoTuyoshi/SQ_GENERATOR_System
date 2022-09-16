#CLASS SQ_EDITOR_PROTO
import pydub
import pydub.playback
from pydub import AudioSegment
import random
#音声編集のクラス
#SHIFT_WAVFILEメソッド
#引数(AudioSegment wav,int millsecond)
#シフトしたAudioSegment型を返します。
def SHIFT_WAVFILE(wav,ms):
        begin = random.randint( 0, ms - 100)
        end = ms - begin + 100
        print(begin)
        print(end)
        begin_data = wav[begin:]
        #end_data = AudioSegment.empty()[end]
        #debug loop
        end_data = wav[:begin]
        wav_data = begin_data + end_data
        return wav_data

def _WAVFILE():
    return 0

