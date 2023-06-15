// Goal: this script is a basic logging script to test serial connection between Arduino and PC w/ Python
// the data being sent is dummy data that counts upwards
// the python script should receive this data and save it into a txt or csv file

// HOW TO USE THIS SCRIPT
// 1. plug in the arduino to your laptop, and select the 'Board' and 'Port' in the 'Tools' dropdown
// 2. click 'upload' to send the script to the arduino and start it running
// 3. you should see two things happening on the board
//      a. light 13 (the built-in light on the board) should turn on/off every second
//      b. the light next to the 'TX' pin should blink once a second [indicates a serial message is being sent]
// 4. open python and... TODO FINISH THE PYTHON SIDE OF THIS!


// global variables
int loopNum;                      // the loop number
String message;                   // the basic contents of the message
String fullMessage;               // the full message to send over serial to python
unsigned long currentTime;        // the current time from getMilliTimeNow()


// analog and digital connections
#define testPin 13                // turn this on/off to confirm program is working [digital]


// setup function
void setup() {
  
  Serial.begin(9600);             // set the baud rate to match the Python code
  loopNum = 0;                    // start loopNum at 0
  pinMode(testPin, OUTPUT);       // configure testPin to be a digital output pin that we SEND info to
  digitalWrite(testPin, LOW);     // set testPin to LOW to start
}


// loop function
void loop() {
  
  // Read Analog pin for a value
  //int sensorValue = analogRead(A0);

  // increment loop number
  loopNum = loopNum + 1;

  // store main data to send over to python
  message = "test data";

  // get timestamp (not really a global time but useful in this exercise
  currentTime = getMilliTimeNow();

  // concatenate the full message to send to python
  fullMessage = String(loopNum) + "," + String(currentTime) + "," + message;


  // send the data over serial to python [or to arduino console]
  Serial.println(fullMessage);

  // flip the light on/off for sanity check
  if (loopNum % 2 == 0) {
    digitalWrite(testPin, LOW);
  } else {
    digitalWrite(testPin, HIGH);
  }

  // delay for the next loop (in milliseconds, 1000ms = 1s)
  delay(1000); 
  
}


// function definitions
unsigned long getMilliTimeNow(void)  // Returns time in ms units
{
  return (millis());
}
