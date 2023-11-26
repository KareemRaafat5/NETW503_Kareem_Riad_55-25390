#include <ESP8266WiFi.h>

const int ledPin = 15; //D8 pin esp
const int LDRPin = 5 ;  //D1 pin esp
const int LDRa = A0; //A0 analog pin esp

bool b= false;
bool d= false;

const char* ssid = "Kemz0";
const char* password =  "12345678";
//bool fc=false;
bool f=false;

const uint16_t port = 8008;
const char * host = "192.168.43.230";
const int check = 4; //D2 pin esp
WiFiClient client;

void setup() {
  Serial.begin(9600);
  pinMode(check,INPUT);

  pinMode(ledPin,OUTPUT);
  pinMode(LDRPin,INPUT);

  Serial.println("Connecting to Wi-Fi...");
  WiFi.begin(ssid, password);

  int attempts = 0;
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
    attempts++;
    if (attempts > 20) {
      Serial.println("\nConnection failed. Check your credentials or network.");
      return;
    }
  }

  Serial.println("");
  Serial.print("WiFi connected with IP: ");
  Serial.println(WiFi.localIP());
}


void loop()
{


  
  int checkpin = digitalRead(check);
  
  if (checkpin==HIGH){
   
    if (client.connected())
  {
    client.println("CLOSE SOCKET");
    client.stop();
    Serial.println("disconnected");
    //fc=true;
    f=false;
    
  }
    }
  
  else{
    if (!client.connected()){
      if (client.connect(host,port)){
      if (!f){
     Serial.println("Connected to server successful!");
      }
      
 
   while(checkpin==LOW){

  //analog reading 
    int v= analogRead(LDRa);
    int per= map(v,0,1023,100,0);
    String s = ("RED READING: "+String(per)+"%");
    Serial.println(s);
    client.println(s);
    Serial.println("sent");
    f=true;
    checkpin = digitalRead(check);
    //fc=false;
    delay(5000);
    }

    }
    }
  }
  
}
