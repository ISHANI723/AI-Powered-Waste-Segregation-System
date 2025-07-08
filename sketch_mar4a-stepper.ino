#define DIR_PIN 10   // Direction pin
#define STEP_PIN 11  // Step pin
#define EN_PIN 12    // Enable pin (optional)

void setup() {
  pinMode(DIR_PIN, OUTPUT);
  pinMode(STEP_PIN, OUTPUT);
  pinMode(EN_PIN, OUTPUT);

  digitalWrite(EN_PIN, LOW); // Enable the stepper driver
}

void loop() {
  digitalWrite(DIR_PIN, HIGH); // Set direction to clockwise

  for (int i = 0; i < 200; i++) { // Rotate 1 revolution (200 steps for 1.8° stepper motor)
    digitalWrite(STEP_PIN, HIGH);
    delayMicroseconds(1000); // Control speed
    digitalWrite(STEP_PIN, LOW);
    delayMicroseconds(1000);
  }

  delay(1000); // Wait for 1 second

  digitalWrite(DIR_PIN, LOW); // Change direction to counter-clockwise

  for (int i = 0; i < 200; i++) {
    digitalWrite(STEP_PIN, HIGH);
    delayMicroseconds(1000);
    digitalWrite(STEP_PIN, LOW);
    delayMicroseconds(1000);
  }

  delay(1000); // Wait for 1 second
}