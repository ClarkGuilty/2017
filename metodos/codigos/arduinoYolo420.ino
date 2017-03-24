
int boton1 = 11; 
int boton2 = 10; 
int dio1 = 3; 
int dio2 = 2; 
int fuente = 13; //la fuente
unsigned long old1 = 0;
unsigned long old2 = 0;
unsigned long actual1 = 0;
unsigned long actual2 = 0;
unsigned long tiempo = 3000;

void setup() {
  // put your setup code here, to run once:
  
//  pinMode(12, OUTPUT);
  pinMode(boton2, INPUT);
  pinMode(boton1, INPUT);
  pinMode(dio1, OUTPUT);
  pinMode(dio2, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(fuente,OUTPUT);
  pinMode(12, OUTPUT);
  digitalWrite(fuente,HIGH);
  digitalWrite(LED_BUILTIN, LOW);
  digitalWrite(12,HIGH);
  digitalWrite(3,LOW);
  digitalWrite(2,LOW);
}
  
  


void loop() {


  //digitalWrite(2,HIGH);
  //delay(3000);
  
  actual1 = millis();
  if(actual1-old1  >tiempo) {
    digitalWrite(3,LOW);
    digitalWrite(LED_BUILTIN, LOW);
  }
  if(digitalRead(boton1) == LOW) {
    digitalWrite(3,HIGH);
    digitalWrite(LED_BUILTIN, HIGH);
    old1 = millis();
  }

  actual2 = millis();
  if(actual2-old2  >tiempo) {
    digitalWrite(dio2,LOW);
  }
  if(digitalRead(boton2) == LOW) {
    digitalWrite(dio2,HIGH);
    old2 = millis();
  }
  
}

