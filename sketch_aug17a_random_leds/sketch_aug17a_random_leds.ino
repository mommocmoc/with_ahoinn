// 2020년 8월 17일 오후 1시부터 3시까지 진행
// 사용한 보드 :  WeMos D1 R2 & Mini

// LED의 갯수
int ledNum = 9;
// LED 제어를 위해 연결한 핀
int leds[] = {D0, D1, D2, D3, D4, D5, D6, D7, D8};
// LED 상태 제어를 위한 변수 배열
bool ledSwitch[] = {false, false, false, false, false, false, false, false, false};
// 몇 초(ms) 한 번씩 상태를 변경할 지 설정하는 변수
int delayTime = 100;

void setup() {
  // WeMos D1 R2 모든 핀을 아웃풋모드로 설정합니다.
  for(int i = 0 ; i < ledNum; i++){
    pinMode(leds[i], OUTPUT); 
  }
}

void loop() {
  // random으로 어떤 LED의 상태를 바꿀지 랜덤하게 선택합니다.
  int switchPicker = random(0, 10);
  ledSwitch[switchPicker] = !ledSwitch[switchPicker];
  for(int i = 0 ; i < ledNum; i++){
    digitalWrite(leds[i],ledSwitch[i]);
  }
  delay(delayTime);
}
