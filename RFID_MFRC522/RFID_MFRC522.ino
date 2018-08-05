

#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9
MFRC522 mfrc522(SS_PIN, RST_PIN);  // Create MFRC522 instance.
byte readCard[4];

void setup() {
  Serial.begin(9600); // Initialize serial communications with the PC
  SPI.begin();      // Init SPI bus
  mfrc522.PCD_Init(); // Init MFRC522 card
  Serial.println("Scan PICC to see UID and type...");
}

void loop() {
        // Se una nuova PICC viene posta sul lettore RFID, continua
      if ( ! mfrc522.PICC_IsNewCardPresent()) { 
      return 0;
      }
      if ( ! mfrc522.PICC_ReadCardSerial()) {   
      return 0;
      }

      Serial.println(F("UID PICC scansionata:"));
      
      for (int i = 0; i < 4; i++) {  //
        
          readCard[i] = mfrc522.uid.uidByte[i];
          Serial.print(readCard[i], HEX);
          }
          Serial.println("");
          mfrc522.PICC_HaltA(); // Smette di leggere
          return 1;
}
