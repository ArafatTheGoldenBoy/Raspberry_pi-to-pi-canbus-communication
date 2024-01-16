#include</usr/include/opencv4/opencv2/core.hpp>
#include</usr/include/opencv4/opencv2/videoio.hpp>
#include</usr/include/opencv4/opencv2/highgui.hpp>
#include<iostream>#include<stdio.h>
using namespace cv;
using namespace std;
int main(int, char**){
    Mat frame;
   VideoCapture cap;
    int deviceID = 0;               //0 = open defaut camera    
int apiID = cv::CAP_ANY;
        //0 = autodetect default API    cap.open(deviceID);
   if(!cap.isOpened()){     
cerr << "Error! Unable to open camera\n";
       return -1; 
}
    cout << "Start grabbing "        << "Press any key to terminate" << endl;
       for(;;){       cap.read(frame);     if(frame.empty()){
          cerr << "Error! blank frame grabbed \n";          break;      }
              cv::namedWindow("Live", cv::WINDOW_AUTOSIZE);
       imshow("Live", frame);      if(waitKey(5) >= 0)          break;   }
   return 0;}