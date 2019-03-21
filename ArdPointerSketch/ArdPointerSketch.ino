/*
            presentationPointer (c) 2019 by Michał Stojke, LICENSE: MIT

  Simple code for Arduino, which allows to read received codes from IR (TSOP31238),
  with small debouncing. For binding IR codes into keyboard, look at python files of 
  the project. This code was written for cheap Arduino UNO clone, which can't be 
  upgraded to operate on lib "Keyboard.h", so it needs the other way to handle with PC 
  keyboard.
*/

#include <IRremote.h>

int IR_PIN = 2; // define TSOP31238 (or other) OUT pin

IRrecv irrecv(IR_PIN);

decode_results results;
int key_pressed;
int last_key_pressed;
unsigned long t_start;
unsigned long t_end;
long debounce_time = 500; // debounce time

void setup()
{
  Serial.begin(9600);
  irrecv.enableIRIn(); // start the receiver
}

void loop() {
  if (irrecv.decode(&results)) {
    key_pressed = results.value;
    if (key_pressed != last_key_pressed) {
      Serial.println(key_pressed);
      last_key_pressed = key_pressed;
      t_start = millis();
    }
    else if (t_start - millis() < debounce_time) {
      Serial.println("debouncing");
    } else {
      last_key_pressed = 0;
    }
    irrecv.resume();
  }
}
