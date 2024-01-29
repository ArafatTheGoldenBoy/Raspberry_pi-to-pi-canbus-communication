#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <net/if.h>

#include <sys/types.h>
#include <sys/socket.h>
#include <sys/ioctl.h>

#include <linux/can.h>
#include <linux/can/raw.h>

int main(void)
{
    int s;
    int nbytes;
    int count = 0;
    struct sockaddr_can addr;
    struct can_frame frame;
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
    
    while(read(s, &frame, sizeof(struct can_frame))){
        
        printf("%d \n", frame.can_id);
        
        // frame id or data are all converted hex to decimal. hex 123 = dec 291
        if(frame.can_id == 291){
            if(frame.data[0] == 1){
                printf("Human Detected \n");
                count = 0;
            }
            else{
                printf("Continue: %d \n", count);
                count++;
                if(count > 9) count = 0;
            }
        }
        else if(frame.can_id == 801){
            
            if(frame.data[0] == 1){
                printf("Others Detected \n");
            }
            else{
                printf("Continue \n");
            }
        }
        else{
            printf("Continue \n");
        }
    }
    return 0;
}
