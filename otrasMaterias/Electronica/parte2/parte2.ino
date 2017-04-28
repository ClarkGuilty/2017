void setup() {
  // put your setup code here, to run once:
  pinMode(8, INPUT);
  pinMode(9, INPUT);
  pinMode(2, INPUT);
  pinMode(3, INPUT);
  pinMode(4, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(8) == HIGH){
    digitalWrite(2, LOW);
  }
  else{
    digitalWrite(2, HIGH);
  }
  if((digitalRead(8) == HIGH) and (digitalRead(9) == HIGH)){
    digitalWrite(3,HIGH);
  }
  else{
    digitalWrite(3, LOW);
  }
  if((digitalRead(8) == HIGH) or (digitalRead(9) == HIGH)){
    digitalWrite(4, HIGH);
  }
  else{
    digitalWrite(4,LOW);
  }

}
