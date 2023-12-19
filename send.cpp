#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <iostream>

#include <net/if.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/ioctl.h>

#include <linux/can.h>
#include <linux/can/raw.h>

#include <opencv2/core.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>

using namespace std;
using namespace cv;

int main(int, char**)
{
    int s;
    int nbytes, nbytes2;
    struct sockaddr_can addr;
    struct can_frame canFrame;
    struct can_frame canFrame2;
    struct ifreq ifr;
    const char *ifname = "can0";
    // can initialize
    if ((s = socket(PF_CAN, SOCK_RAW, CAN_RAW)) == -1)
    {
        perror("Error while opening socket");
        return -1;
    }

    strcpy(ifr.ifr_name, ifname);
    ioctl(s, SIOCGIFINDEX, &ifr);

    addr.can_family = AF_CAN;
    addr.can_ifindex = ifr.ifr_ifindex;

    printf("%s at index %d\n", ifname, ifr.ifr_ifindex);

    if (bind(s, (struct sockaddr *)&addr, sizeof(addr)) == -1)
    {
        perror("Error in socket bind");
        return -2;
    }
    // can massage 1
    canFrame.can_id = 0x123;
    canFrame.can_dlc = 2;
    canFrame.data[0] = 0x11;
    canFrame.data[1] = 0x22;
    // can massage 2
    canFrame2.can_id = 0x321;
    canFrame2.can_dlc = 2;
    canFrame2.data[0] = 0x15;
    canFrame2.data[1] = 0x25;
    // can conf
    Mat frame;
    //--- INITIALIZE VIDEOCAPTURE
    VideoCapture cap;
    // open the default camera using default API
    // cap.open(0);
    // OR advance usage: select any API backend
    int deviceID = 0;             // 0 = open default camera
    int apiID = cv::CAP_ANY;      // 0 = autodetect default API
    // open selected camera using selected API
    cap.open(deviceID, apiID);
    // resizing camera resulation
    cv::namedWindow("frame",cv::WINDOW_NORMAL);
    cv::resizeWindow("frame",640,480);
    // check if we succeeded
    if (!cap.isOpened()) {
        cerr << "ERROR! Unable to open camera\n";
        return -1;
    }
    //--- GRAB AND WRITE LOOP
    cout << "Start grabbing" << endl
        << "Press any key to terminate" << endl;
    for (int i = 0,j=3,k=5; i <= 30; i++)
    {
        // Every 3 secend, now we can send message
        if(i == j){
            cout << "3 send can message" << endl;
            nbytes = write(s, &canFrame, sizeof(struct can_frame));
            j+=3;
        }
        if(i == k){
            cout << "5 send can message" << endl;
            nbytes2 = write(s, &canFrame2, sizeof(struct can_frame));
            k+=5;
        }
        // wait for a new frame from camera and store it into 'frame'
        cap.read(frame);
        // check if we succeeded
        if (frame.empty()) {
            cerr << "ERROR! blank frame grabbed\n";
            break;
        }
        // show live and wait for a key with timeout long enough to show images
        imshow("frame", frame);
        if (waitKey(5) >= 0)
            break;
    }
    // the camera will be deinitialized automatically in VideoCapture destructor
    return 0;
}
