#include<stdio.h>
#include<math.h>
#include <stdlib.h>
int main(int argc,char* argv[]){
    if(argc==1){
        exit(0);
    }
    printf("RR started\n");
    long long int cnt=1;
    long long int a=pow(2,32);
    while(cnt!=a){
        // printf("%f",cnt);
        cnt++;
    }
    printf("rr-%lld\n",cnt);
    return 0;
}