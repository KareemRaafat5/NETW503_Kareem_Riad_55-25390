#include "ThingsBoard.h"
#include <ESP8266WiFi.h>

const int ledPin = 15; //D8 pin esp
const int LDRPin = 5 ;  //D1 pin esp
const int LDRa = A0; //A0 analog pin esp
const int check = 4; //D2 pin esp


const char *ssid = "Kemz0";
const char *password = "12345678";
const char *accessToken = "vwuy9dcfufalkp8b30lp";
const char *thingsboardServer = "demo.thingsboard.io"; // Replace with your ThingsBoard server address
int i=1;
WiFiClient wifiClient;
ThingsBoard tb(wifiClient);

void setup() {
  Serial.begin(115200);
  pinMode(ledPin,OUTPUT);
    
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  // Connect to ThingsBoard
  if (tb.connect(thingsboardServer, accessToken)) {
    Serial.println("Connected to ThingsBoard");
  } else {
    Serial.println("Failed to connect to ThingsBoard");
  }
}

void loop() {
  delay(2000);
  
  /*int LDRstatus = digitalRead(LDRPin);
   if (LDRstatus ==1){
    digitalWrite(ledPin,HIGH);
   }
  else{
    digitalWrite(ledPin,LOW);
  }*/

   
  if (!tb.connected()) {
   
    // Connect to the ThingsBoard
    Serial.print("Connecting to: ");
    Serial.print(thingsboardServer);
    Serial.print(" with token ");
    Serial.println(accessToken);
    if (!tb.connect(thingsboardServer, accessToken)) {
      Serial.println("Failed to connect");
      return;
    }
    Serial.println("connected to thingsboard ");
  }
  

  
  //analog reading 
  int v= analogRead(LDRa);
  int per= map(v,0,1023,100,0);
  String s = ("BLUE READING: "+String(per)+"%");
  Serial.println(s);
  Serial.println("data sent");
  tb.sendTelemetryInt("Blue light intensity ", per);
  
   if (per<50){
    digitalWrite(ledPin,HIGH);
   }
  else{
    digitalWrite(ledPin,LOW);
  }
  
  

  tb.loop();
}
