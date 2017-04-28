const int c = 5;
const int d = 6;
const int y = 7;
const int a = 8;
const int b = 9;

void setup() {
  // put your setup code here, to run once:
  pinMode(c, OUTPUT);
  pinMode(d, OUTPUT);
  pinMode(y, OUTPUT);
  pinMode(a, INPUT);
  pinMode(b, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if((digitalRead(a) == LOW) and (digitalRead(b) == HIGH)){
    digitalWrite(c, HIGH);
  }
  else{
    digitalWrite(c, LOW);
  }
  if((digitalRead(a) == HIGH) and (digitalRead(b) == LOW)){
    digitalWrite(d, HIGH);
  }
  else{
    digitalWrite(d, LOW);
  }
  if((digitalRead(c) == HIGH) or (digitalRead(b) == HIGH)){
    digitalWrite(y, HIGH);
  }
  else{
    digitalWrite(y, LOW);
  }
  
}
