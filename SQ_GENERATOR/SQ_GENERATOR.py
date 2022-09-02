import pydub
from pydub import AudioSegment
import pydub.playback
import random
import numpy as np
import wave as wv
import tkinter as tk

import sys,glob,pathlib,os,time

min = 0.5
wavs = list()
#wav files
#cnt = 0
#gf_cnt = 0
#ms_cnt = 0

def SHIFT_WAVFILE(wav):
    begin = random.randint(0,3500)
    end = random.randint(3500,7000)
    wav_data = AudioSegment.from_file(wav)[begin:end]
    return wav_data

def PROGRESS_ANIMATION(_cnt,_gf_cnt,_ms_cnt):
    i = 0
    print('0%      50%      100%')
    print('+--------+--------+')
    wait_len = '|'+' '*17+'|'
    wait_time = 0.25
    while(i < 18):
        time.sleep(wait_time)
        #next = wait_len[::-1].replace('0', '1', i)[::-1]
        next = wait_len.replace(' ', '|', i)
        print(next,'\r',end='')
        i+=1
    print('|'*18)
    print('+--------+--------+')

def DATA_IN_WAV():
    print('hell')

def FIX_WAV():
    print('fix')

#print('SELECT OPTION Manual(M) or Auto(A)<<');

#sign = input()
#if sign == M or sign == m:
#    print("L<Manual Mode>")
#    print("wav data <- ")
#
#<!--KOBARA CODE--->
##音声データの受け取り
#num = int(input("データの個数を入力＞＞　"))
#sound = []
#for i in range(num):
#    fname = input("ファイル名を入力＞＞　")
#    sound.append(fname)
##問題の作成
#sourceAudio = []
##exAudio
#for i in range(num):
#    start = random.randint(0,3500)
#    end = random.randint(3500,7000)
#    pos = random.randint(0,1500)
#    sourceAudio.append(AudioSegment.from_file(sound[i]))
#    #play(sourceAudio[i][start:end])
#    exAudio = sourceAudio[0].overlay(sourceAudio[i][start:end], position = pos)
##play(exAudio)

#def Manual_Generator():
#    print(' Phase Manual...')
#    print(' Data Count(num):',end='')
#    size = int(input())
#    wav_list = []
#    for i in range(0,size,1):
#        print(' WAV_FILE[{}] : '.format(i),end='')
#        wav_ps = input()
#        wav_list.append(wav_ps)
#    print('  Mixing Mode => Manual(M)-(m)-(0) or Auto(anykey)')
#    print('command <= ',end = '')
#    cmd = input()
#    if(MODE_RETURN(cmd) == 0):
#        print('Begin time(mill second) : ',end='')
#        bgsec = int(input())
#        print('End time  (mill second) : ',end='')
#        edsec = int(input())
#        #SHIFT_WAVFILE()

#return random list(nosame value)
def Generate_Random(_size):
    rnd_list = []
    while(len(rnd_list) < _size):
        #max = wavs[]size
        num = random.randint(0,len(wavs))
        if(not num in rnd_list):
            rnd_list.append(num)
    return rnd_list

def Auto_Generator():
    print('[Phase Auto]')
    print('wav folder pass <- ',end = '')
    dir_ps = input()
    files = pathlib.Path(dir_ps).glob('*')
    for file in files:
        if file.is_file():
            wavs.append(file)
            print(file.name)

    print('何重にしますか(１音声当たりの合成数)?(3-40):',end = '')
    cnt = int(input())
    print('いくつ錬成しますか?(1-200)',end = '')
    gf_cnt = int(input())
    print('大体何ミリ秒ですか?(500-7000)',end = '')
    ms_cnt = int(input())
    print('問題を錬成します。')
    #GENERATE_PHASE(cnt,gf_cnt,ms_cnt)

    for gf in range(0,gf_cnt,1):
        rnd_list= Generate_Random(cnt)
        use_wav = list()
        j=0
        for i in rnd_list:
            use_wav.append(wavs[i])
            print('L__',use_wav[j].name)
            j+=1
        _path = os.path.abspath(use_wav[0])
        generate_wav = AudioSegment.from_file(_path)
        use_wav.pop(0)
        for wav in use_wav:
            generate_wav *= AudioSegment.from_file(os.path.abspath(wav))
        generate_wav.export("problem_" + str(gf) + ".wav",format='wav')

    #print(rnd_list)

    #SHIFT_WAVFILE()

def MODE_RETURN(_cmd):
    if(_cmd=='M' or _cmd=='m' or _cmd =='0'):
        return 0
    elif(_cmd=='A' or _cmd=='a' or _cmd =='1'):
        return 1
    else:
        return -1

if __name__== '__main__':
    print('|---------------------------------------|')
    print('| PROCON2022 SQ_Generator  -Chaos Wav-  |')
    print('| Auto Generate command : (A)-(a)-(1)   |')
    print('| Cancel command : (any-key command)    |')
    print('|---------------------------------------|')
    print('| プロトA1号 概要：音声完全ランダム生成 |')
    print('| A2号実装予定機能: 詳細オプション指定  |')
    print('| リリース 2022/09/02                   |')
    print('|---------------------------------------|')

    cmd = input()
    #Generate_Random(200)
    #GENERATE_PHASE(10,0,0)
    if(MODE_RETURN(cmd)==1):
        Auto_Generator()
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
