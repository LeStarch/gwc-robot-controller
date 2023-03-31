/**
 * Controller code for the robot-controller unit. It does several things:
 * 
 * 1. Imports the NeoPixel library
 * 2. Sets up some constants for use later
 * 3. Setup:
 *    a. Initialize the serial output (sending data to computer/labptop)
 *    b. Initialize LED array to show current levels
 * 4. Loop: (repeats)
 *    a. Read ADC x and y values
 *    b. Convert to number 0-8
 *    c. Set colors on LED array
 *    d. Print to serial
 */
#include <Adafruit_NeoPixel.h>

const int LED_COUNT = 8; // There are 8 leds on the neopixel
const int LED_PIN = 4;  // The pin in use for LED array output

// ADC pins used for reading the joystick (2 dimensions)
const int ADC_PIN_X = A0;
const int ADC_PIN_Y = A1;
const int ADC_MAX = 1023; // Maximum value from ADC (0-1023)

Adafruit_NeoPixel pixels(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);
auto GREEN = pixels.Color(0, 255, 0);


void setup() {
    Serial.begin(115200); // Serial speed to 115200bps
    pixels.begin();
}

void loop() {
    int x_val = analogRead(ADC_PIN_X); // 0 - 1023 (ADC_MAX)
    int y_val = analogRead(ADC_PIN_Y); // 0 - 1023 (ADC_MAX)
    // Convert y value to range 0-8
    int leds_value = ((LED_COUNT * y_val) + (ADC_MAX/2))/ADC_MAX;
    // Clear pixels, set up to "leds_value" on/green and show
    pixels.clear();
    for (int i = 0; i < leds_value && i < LED_COUNT; i++) {
        pixels.setPixelColor(i, GREEN);
    }
    pixels.show();
    // Print output to serial line
    Serial.print(x_val);
    Serial.print(",");
    Serial.println(y_val);
    delay(10);
}
