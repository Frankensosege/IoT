# coding: utf-8

# GPIO 라이브러리 임포트
import RPi.GPIO as GPIO

# time 라이브러리 임포트
import time

# 핀 번호 할당 방법은 커넥터 핀 번호로 설정
GPIO.setmode(GPIO.BOARD)

# 사용할 핀 번호 할당
LED1 = 12
LED2 = 16
LED3 = 18

# 11번 핀을 출력 핀으로 설정, 초기 출력은 로우 레벨
GPIO.setup(LED1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED3, GPIO.OUT, initial=GPIO.LOW)

# 예외 처리
try:

    # 무한 반복
    while 1:

        # 하이 레벨 출력
        GPIO.output(LED3, GPIO.LOW)
        GPIO.output(LED1, GPIO.HIGH)

        # 0.5초 대기
        time.sleep(0.5)

        # 로우 레벨 출력
        GPIO.output(LED1, GPIO.LOW)
        GPIO.output(LED2, GPIO.HIGH)

        # 0.5초 대기
        time.sleep(0.5)
        
        GPIO.output(LED2, GPIO.LOW)
        GPIO.output(LED3, GPIO.HIGH)
        
        time.sleep(0.5)

# 키보드 예외를 검출
except KeyboardInterrupt:

    # 아무것도 안함
    pass

# GPIO 개방
GPIO.cleanup()
