import pydub
from pydub import AudioSegment
import pydub.playback
import random
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
import sys,glob,pathlib,os,time,wave,soundfile

#MAIN CLASS(SQ_EDITOR_PROTO) in other words SQ_GENERATOR
class SQ_EDITOR_PROTO:
    def SHIFT_WAVFILE(wav):
        begin = random.randint(0,3500)
        end = random.randint(3500,7000)
        wav_data = AudioSegment.from_file(wav)[begin:end]
        return wav_data
    
#This class(CUI_UNIQUE) is refuse.
#for example Animation,Design and Layout.
class CUI_UNIQUE:
    def PROGRESS_ANIMATION(_prcs):
        i = 0
        print('0%      50%      100%')
        print('+--------+--------+')
        wait_len = '|'+' '*17+'|'
        wait_time = 0.01
        while(i < 18):
            time.sleep(wait_time)
            #next = wait_len[::-1].replace('0', '1', i)[::-1]
            next = wait_len.replace(' ', '|', i)
            print(next,'\r',end='')
            i+=1
        print('|'*18)
        print('+--------+--------+')

#return random list(nosame value)
#generation function <= access all class
def PACKAGE_RANDLIST(_size):
    rnd_list = []
    while(len(rnd_list) < _size):
        num = random.randint(0,len(wavs)-1)
        if(not num in rnd_list):
            rnd_list.append(num)
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
    #GENERATE_PHASE(cnt,gf_cnt,ms_cnt)

    for gf in range(0,gf_cnt,1):
        rnd_list = PACKAGE_RANDLIST(cnt)
        use_wav = list()
        j=0
        print('wavs_len = ',len(wavs))
        for i in rnd_list:
            use_wav.append(wavs[i])
            print('L__',use_wav[j].name)
            j+=1
        _path = os.path.abspath(use_wav[0])
        generate_wav = AudioSegment.from_file(_path)
        use_wav.pop(0)
        for wav in use_wav:
            generate_wav *= AudioSegment.from_file(os.path.abspath(wav))
        wav_data = np.array(generate_wav.get_array_of_samples())
        x = wav_data[::generate_wav.channels]
        print('{}:max = {} sampling = {}'.format(max(x)>sampling,max(x),sampling))
        plt.plot(x[::100])
        plt.grid()
        plt.show()
        generate_wav.export("problems/problem_" + str(gf) + ".wav",format='wav',tags={'artist': 'JOUGE', 'album': 'KYOUGI2022', 'comments': 'CHAOS'})

def AMPLIFER_FIX():
    print('[Phase FIX]')
    print('ここではアンプを修正します。修正するwavファイルが入ったフォルダパスを以下に参照してください。')
    print('fix wav folder pass <- ',end = '')
    #dir_ps = "C:/Users/futur/source/repos/SQ_GENERATOR\SQ_GENERATOR_System/SQ_GENERATOR\AMP_DEBUG\problem_0.wav"
    #dir_ps = input()
    #org_wavs = pathlib.Path(dir_ps).glob('*')
    
    data, fs = soundfile.read('problem_0.wav')
    #print(fs.samplerate)
    soundfile.write('output.wav', data, fs, subtype='PCM_16')
    print('end')
    #for test in org_wavs:
    #    print(test)
    #    data, fs = soundfile.read(test)
    #    soundfile.write('output'+str(u)+'.wav', data, fs, subtype='PCM_16')

    #wave_file = wave.open(dir_ps,'rb')
    #print(wave_file.getframerate())


    #print(chr(92))
    #for wav in org_wavs:
        #wav = repr(wav)
        #path = wav.replace(chr(92),'/')
        #print(path)
        #wave_file = wave.open(path,'r')
        #print(wave_file.getframerate())
        ##....
        #x = wave_file.readframes(wave_file.getnframes()) #frameの読み込み
        #x = np.frombuffer(x, dtype= "int16") #numpy.arrayに変換
        #print(x)
        #print(max(x))

        #wav_data = np.array(wave_file.getnframes())
        #x = wav_data[::generate_wav.channels]
        #print('{}:max = {} sampling = {}'.format(max(x)>sampling,max(x),sampling))
        #plt.plot(x[::10])
        #plt.grid()
        #plt.show()

def MODE_RETURN(_cmd):
    #if(_cmd=='M' or _cmd=='m' or _cmd =='0'):
    #    return 0
    if(_cmd=='A' or _cmd=='a' or _cmd =='1'):
        return 1
    elif(_cmd=='F' or _cmd=='f' or _cmd =='0'):
        return 0
    else:
        return -1

if __name__== '__main__':
    CUI_UNIQUE.PROGRESS_ANIMATION(1)
    print('|---------------------------------------|')
    print('| PROCON2022 SQ_Generator  -Chaos Wav-  |')
    print('| Auto Generate command: (A)-(a)-(1)    |')
    print('| Amplifier Fixed command: (F)-(f)-(0)  |')
    print('| Cancel command : (any-key command)    |')
    print('|---------------------------------------|')
    print('| プロトA1号 概要：音声完全ランダム生成 |')
    print('| A2号実装予定機能: 詳細オプション指定  |')
    print('| リリース 2022/09/02                   |')
    print('|---------------------------------------|')

    print('コマンド? : ',end = '')
    cmd = input()

    if(MODE_RETURN(cmd)==1):
        AUTO_GENERATOR()

    #developing now
    elif(MODE_RETURN(cmd)==0):
        #SQ_EDITOR_PROTO.AMPLIFER_FIX()
        AMPLIFER_FIX()
    else:
        print('CANCELLED')

    #SHIFT_WAVFILE()
    #DATA_IN_WAV()
    #exAudio1 = AudioSegment.from_file(input())[:3500]
    #exAudio1.export("problem2.wav",format='wav')


#def AUTO_RETURN(cmd):

#exAudio2 = AudioSegment.from_file(input())

#test = exAudio1*exAudio2

#ファイル出力
#ExportFname = input("出力ファイル名を入力＞＞　")
#test1.export("problem1.wav",format='wav')
