const int sensorPin = A0;   // 조도센서 핀
const int ledPin = 13;      // LED 핀 (13번 핀)

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(sensorPin); // whh
  Serial.println(sensorValue);

  if (sensorValue >= 520) { // 조도센서 값이 520 이하인 경우
    digitalWrite(ledPin, LOW); // LED 끄기
  } else {
    digitalWrite(ledPin, HIGH); // LED 켜기
  }
}
