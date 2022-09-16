import pydub
from pydub import AudioSegment
import pydub.playback
import random
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
import sys,glob,pathlib,os,wave,soundfile

import CUI_UNIQUE, SQ_EDITOR_PROTO

#return random list(nosame value)
#generation function <= access all class
def PACKAGE_RANDLIST(_size):
    rnd_list = []
    audit_list =[]
    while(len(rnd_list) < _size):
        num = random.randint(0,len(wavs) - 1)
        if(not num in rnd_list and not num % 44 in audit_list):
            audit_list.append(num % 44)
            rnd_list.append(num)
        #Debug Only
        #if(not num in rnd_list):
        #    rnd_list.append(num)
    rnd_list.sort()
    print(rnd_list)
    return rnd_list

min = 0.5
wavs = list()
sampling = pow(2,15)

def AUTO_GENERATOR():
    print('[Phase Auto]')
    print('wav folder pass <- ',end = '')
    dir_ps = input()
    files = pathlib.Path(dir_ps).glob('*')

    for file in files:
        if file.is_file():
            wavs.append(file)
            print(file.name)

    print('何重にしますか(１音声当たりの合成数)?(3-40) <- ',end = '')
    cnt = int(input())
    print('いくつ錬成しますか?(1-200) <- ',end = '')
    gf_cnt = int(input())
    print('大体何ミリ秒ですか?(500-7000) <- ',end = '')
    ms_cnt = int(input())
    print('問題を錬成します。')

    for gf in range(0,gf_cnt,1):
        rnd_list = PACKAGE_RANDLIST(cnt)
        use_wav = list()
        j=0
        print('wavs_len = ',len(wavs))
        for i in rnd_list:
            use_wav.append(wavs[i])
            print('L__',use_wav[j].name)
            j += 1
        _path = os.path.abspath(use_wav[0])
        generate_wav = AudioSegment.from_file(_path)
        generate_wav = SQ_EDITOR_PROTO.SHIFT_WAVFILE(generate_wav,ms_cnt)
        #generate_wav = AudioSegment.empty()[ms_cnt]
        file_name = use_wav[0].name[:3]

        use_wav.pop(0)
        
        for wav in use_wav:
            use_file = AudioSegment.from_file(os.path.abspath(wav))
            use_file = SQ_EDITOR_PROTO.SHIFT_WAVFILE(use_file,ms_cnt)
            #generate_wav *= AudioSegment.from_file(os.path.abspath(wav))
            generate_wav *= use_file

            file_name += ('_' + wav.name[:3])
        #for wav in use_wav:
        #    use_file = AudioSegment.from_file(os.path.abspath(wav))
        #    use_file = SQ_EDITOR_PROTO.SHIFT_WAVFILE(use_file,ms_cnt)
        #    
        #    #generate_wav *= AudioSegment.from_file(os.path.abspath(wav))
        #    use_file *= use_file
        #
        #    file_name += ('_' + wav.name[:3])
        wav_data = np.array(generate_wav.get_array_of_samples())
        x = wav_data[::generate_wav.channels]
        #print('{}:max = {} sampling = {}'.format(max(x)>sampling,max(x),sampling))
        #plt.plot(x[::100])
        #plt.grid()
        #plt.show()
        generate_wav.export("problems/SQ_" + str(gf) + file_name + ".wav",format='wav',tags={'artist': 'JOUGE', 'album': 'KYOUGI2022', 'comments': 'CHAOS'})

def MODE_RETURN(_cmd):
    if(_cmd=='A' or _cmd=='a' or _cmd =='1'):
        return 1
    else:
        return -1

#if __name__== '__main__':
#CUI_UNIQUE.PROGRESS_ANIMATION()
print('+---------------------------------------+')
print('| PROCON2022 SQ_Generator  -Chaos Wav-  |')
print('| Auto Generate command: (A)-(a)-(1)    |')
print('| Cancel command : (any-key command)    |')
print('+---------------------------------------+')
#print('| プロトA1号 概要：音声完全ランダム生成 |')
#print('| A2号実装予定機能: 詳細オプション指定  |')
#print('| リリース 2022/09/02                   |')
#print('|---------------------------------------|')

print('コマンド? : ',end = '')
cmd = input()

if(MODE_RETURN(cmd)==1):
    AUTO_GENERATOR()
else:
    print('CANCELLED')

#def AUTO_RETURN(cmd):

#exAudio2 = AudioSegment.from_file(input())

#test = exAudio1*exAudio2
 
#ファイル出力
#ExportFname = input("出力ファイル名を入力＞＞　")
#test1.export("problem1.wav",format='wav')
