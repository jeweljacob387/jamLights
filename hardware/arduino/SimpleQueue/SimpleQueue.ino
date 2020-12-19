/*
  Simple Queue
  Simple queue demonstration
  
  LIFO / FIFO implementations can be tested by changing IMPLEMENTATION

  This example code is in the public domain.

  created 22 March 2017
  modified 04 November 2020
  by SMFSW
 */

#include <cppQueue.h>

#define	IMPLEMENTATION	FIFO


typedef struct strRec {
  uint16_t  dev1;
} Rec;

Rec  tab[] = {
	{ 1 },
	{ 1 },
	{ 2 },
	{ 3 },
	{ 4 }
};


cppQueue	q(sizeof(Rec), 1000);	// Instantiate queue

// the setup function runs once when you press reset or power the board
void setup() {
	Serial.begin(9600);
}

// the loop function runs over and over again forever
void loop() {
	unsigned int i;
 Serial.print("sz tab");
 Serial.println(sizeof(tab));
 Serial.print("sz Rec");
 Serial.println(sizeof(Rec));

Rec rcc = {38};
 tab[6] = rcc;
	
	for (i = 0 ; i < sizeof(tab)/sizeof(Rec) ; i++)
	{
		Rec rec = tab[i];
		q.push(&rec);
	}
	
	for (i = 0 ; i < sizeof(tab)/sizeof(Rec) ; i++)
	{
		Rec rec;
		q.pop(&rec);
		Serial.println(rec.dev1, HEX);
	}
	
	while(1);
}
