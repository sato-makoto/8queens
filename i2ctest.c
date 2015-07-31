#include<stdio.h>
#include<wiringPiI2C.h>
#include<time.h>

int main() 
{
  int chipfd, ret;
  int chipaddr = 112;
/*
  struct timespec req;
  req.tv_nsec = 1000000000;
  req.tv_sec = 5;
  nanosleep(&req, NULL);
*/

  int x = 100;
  chipfd =  wiringPiI2CSetup(chipaddr);

  for (x = 0; x < 100; x+=2) {
    ret = wiringPiI2CWrite(chipfd, x);
    printf("%d\n", x);
  }
  return ret;


}
