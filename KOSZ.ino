#include "esp_camera.h"
#include <WiFi.h>
#include <WiFiClient.h>
#include <Stepper.h>

#define CAMERA_MODEL_AI_THINKER 
#include "camera_pins.h"



int motorSpeed = 10;
Stepper myStepper(2048,15,14,2,4);

const char *ssid = "%$%$@%";
const char *password = "@#!@#!";
const char *server_ip = "192.168.0.63"; 
const uint16_t server_port = 5555;      
int step=0;
int steppers[4]={0,512,1024,1536};
WiFiClient client;


const int ledPin = 13;  
const int id = 2123;

void setup() {
  Serial.begin(115200);
  myStepper.setSpeed(motorSpeed);
  Serial.setDebugOutput(true);
  Serial.println();

  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);  
  pinMode(motorPin, OUTPUT);
  digitalWrite(motorPin, LOW); 

  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sccb_sda = SIOD_GPIO_NUM;
  config.pin_sccb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXFORMAT_JPEG;
  config.frame_size = FRAMESIZE_QVGA;
  config.jpeg_quality = 10;
  config.fb_count = 2;
  config.fb_location = CAMERA_FB_IN_PSRAM;

  if (psramFound()) {
    config.grab_mode = CAMERA_GRAB_LATEST;
  } else {
    config.frame_size = FRAMESIZE_SVGA;
    config.fb_location = CAMERA_FB_IN_DRAM;
  }

  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed with error 0x%x", err);
    return;
  }

  WiFi.begin(ssid, password);
  WiFi.setSleep(false);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  if (client.connect(server_ip, server_port)) {
    Serial.println("Connected to server");

    camera_fb_t *fb = esp_camera_fb_get();
    if (!fb) {
      Serial.println("Camera capture failed");
      client.stop();
      delay(5000);
      return;
    }
    client.write((const uint8_t *)&id, sizeof(id));

    client.write((const uint8_t *)&fb->len, sizeof(fb->len));
    client.write(fb->buf, fb->len);

    esp_camera_fb_return(fb);
    Serial.println("Image sent");

    digitalWrite(ledPin, HIGH);

    delay(15000);
    int response = client.read(); 
    Serial.println(response-48);
    step=steppers[response-48];
    myStepper.step(step);
    delay(10000);
    myStepper.step(-step);
    step=0;

  

    client.stop(); 

  digitalWrite(ledPin, LOW);
  delay(10000); 
}}
