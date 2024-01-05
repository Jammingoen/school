const int sensorPin = A0;   
const int ledPin = 13;      

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(sensorPin); 
  Serial.println(sensorValue);

  if (sensorValue >= 520) { 
    digitalWrite(ledPin, LOW); 
  } else {
    digitalWrite(ledPin, HIGH); 
  }
}