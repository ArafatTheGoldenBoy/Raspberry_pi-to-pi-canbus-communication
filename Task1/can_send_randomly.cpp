#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <iostream>
using namespace std;
#include <net/if.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/ioctl.h>

#include <linux/can.h>
#include <linux/can/raw.h>

int main(void)
{
    int s;
    int nbytes, nbytes2;
    struct sockaddr_can addr;
    struct can_frame frame;
    struct can_frame frame2;
    struct ifreq ifr;

    const char *ifname = "can0";

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
    frame.can_id = 0x123;
    frame.can_dlc = 2;
    frame.data[0] = 0x11;
    frame.data[1] = 0x22;
    // can massage 2
    frame2.can_id = 0x321;
    frame2.can_dlc = 2;
    frame2.data[0] = 0x15;
    frame2.data[1] = 0x25;
    for(int i = 0; i < 6 ; i++){
        nbytes = write(s, &frame, sizeof(struct can_frame));
        nbytes2 = write(s, &frame2, sizeof(struct can_frame));
        frame.can_id = rand() % 100;
        frame.data[0] = rand() % 100;
        frame.data[1] = rand() % 100;
        frame.can_dlc = (rand() % (8 - 1 + 1)) + 1;
        
        frame2.can_id = rand() % 100;
        frame2.data[0] = rand() % 100;
        frame2.data[1] = rand() % 100;
        frame2.can_dlc = (rand() % (8 - 1 + 1)) + 1;
    }

    printf("Wrote %d bytes\n", nbytes);
    printf("Wrote %d bytes\n", nbytes2);
    cout << nbytes << endl;
    cout << nbytes2 << endl;

    return 0;
}
