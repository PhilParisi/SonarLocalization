/*
  Get the high position accuracy of the RTK enhanced position from HPPOSECEF
  By: Nathan Seidle
  SparkFun Electronics
  Date: January 3rd, 2019
  License: MIT. See license file for more information.

  This example shows how to inspect the accuracy of the high-precision
  positional solution.

  Feel like supporting open source hardware?
  Buy a board from SparkFun!
  SparkFun GPS-RTK2 - ZED-F9P (GPS-15136)    https://www.sparkfun.com/products/15136
  SparkFun GPS-RTK-SMA - ZED-F9P (GPS-16481) https://www.sparkfun.com/products/16481
  SparkFun MAX-M10S Breakout (GPS-18037)     https://www.sparkfun.com/products/18037
  SparkFun ZED-F9K Breakout (GPS-18719)      https://www.sparkfun.com/products/18719
  SparkFun ZED-F9R Breakout (GPS-16344)      https://www.sparkfun.com/products/16344

*/

#include <Wire.h> //Needed for I2C to GNSS

#include <SparkFun_u-blox_GNSS_v3.h> //http://librarymanager/All#SparkFun_u-blox_GNSS_v3
SFE_UBLOX_GNSS myGNSS;

String serial_msg;

void setup()
{
  delay(1000);
  
  Serial.begin(115200);

  Wire.begin();

  if (myGNSS.begin() == false) //Connect to the u-blox module using Wire port
  {
    Serial.println(F("u-blox GNSS not detected at default I2C address. Please check wiring. Freezing."));
    while (1);
  }

  myGNSS.setI2COutput(COM_TYPE_UBX); //Set the I2C port to output UBX only (turn off NMEA noise)
  //myGNSS.saveConfiguration(); //Optional: Save the current settings to flash and BBR
}

void loop()
{

  // query module. The module only responds when a new position is available
  if (myGNSS.getPVT())
  {
    // get arduino timestamp (time since the start of the .ino program --> counts up to ~45 days)
    unsigned long currentTime = getMilliTimeNow();
    serial_msg = String(currentTime);
    
    // get latitude (degrees*10^-7)
    long latitude = myGNSS.getLatitude();

    // get longitude (degrees*10^-7)
    long longitude = myGNSS.getLongitude();

    // get altitude (millimeters)
    long altitude = myGNSS.getAltitude();

    // create serial_msg
    serial_msg = serial_msg + "," + String(latitude) + "," + String(longitude) + "," + String(altitude);
  }
  
  if (myGNSS.getNAVHPPOSECEF())
  {
    // get accuracy if available (in millimeters)
    long accuracy = myGNSS.getPositionAccuracy();
    serial_msg = serial_msg + "," + String(accuracy);
  }

  // send the serial message
  Serial.println(serial_msg);
}


// function definitions
unsigned long getMilliTimeNow(void)  // Returns time in ms units
{
  return (millis());
}
