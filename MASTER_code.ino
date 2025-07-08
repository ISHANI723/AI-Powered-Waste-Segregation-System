#include <Wire.h>

#define SLAVE_ADDRESS 8  // Define the slave address

void setup() {
    Wire.begin();  // Join I2C bus as master
    Serial.begin(9600);
    Serial.println("Enter 'dry', 'wet', or 'paper':");
}

void loop() {
    if (Serial.available()) {
        String input = Serial.readStringUntil('\n'); // Read user input
        input.trim(); // Remove any extra spaces or newlines
        byte dataToSend = 0;

        if (input == "dry") {
            dataToSend = 0b01;  // Binary 01
        } else if (input == "wet") {
            dataToSend = 0b10;  // Binary 10
        } else if (input == "paper") {
            dataToSend = 0b11;  // Binary 11
        } else {
            Serial.println("Invalid input. Enter 'dry', 'wet', or 'paper'.");
            return;
        }

        Wire.beginTransmission(SLAVE_ADDRESS); // Start I2C transmission
        Wire.write(dataToSend); // Send binary data
        Wire.endTransmission(); // End transmission

        Serial.print("Sent: ");
        Serial.println(dataToSend, BIN); // Print sent binary data
    }
}
