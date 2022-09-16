#CLASS CUI_UNIQUE
import time

#CUIでのプロセスアニメーションなどのクラス
def PROGRESS_ANIMATION():
    i = 0
    print('0%      50%      100%')
    print('+--------+--------+')
    wait_len = '|'+' '*17+'|'
    wait_time = 0.01
    while(i < 18):
        time.sleep(wait_time)
        next = wait_len.replace(' ', '|', i)
        print(next,'\r',end='')
        i+=1
    print('|'*18)
    print('+--------+--------+')