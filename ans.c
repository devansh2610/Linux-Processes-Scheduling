#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <sched.h>
#include <time.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/syscall.h>

int main(){
    cpu_set_t cpumask;
    CPU_ZERO(&cpumask);
    CPU_SET(1, &cpumask);
    if(sched_setaffinity(0, sizeof(cpumask), &cpumask) == -1){
        perror("error in cpu core 1.");
    }

    int rc[3];
    struct timespec start, end;//gives time in sec and nanosec.
    struct timespec begin[3];
    FILE* file=fopen("file.txt","w");
    
    for(int i=0;i<3;i++){

        clock_gettime(CLOCK_REALTIME,&begin[i]);
        rc[i]=fork();
        if(rc[i]<0){
            perror("Error during forking");
        }

        else if(rc[i]==0){
            struct sched_param var;//to set priority using an integer.
            if(i==0){
                var.sched_priority=0;
                nice(0);//setting nice value as 0
                sched_setscheduler(0,SCHED_OTHER,&var);//to set scheduling algo to SCHED_OTHER
                execl("./count1","trap1","trap2",NULL);
                perror("Some error in execl");
            }

            else if(i==1){
                var.sched_priority=((sched_get_priority_min(SCHED_RR)+sched_get_priority_max(SCHED_RR)))/2;//default priority
                sched_setscheduler(0,SCHED_RR,&var);//to set scheduling algo to SCHED_RR
                execl("./count2","trap1","trap2",NULL);
                perror("Some error in execl");

            }

            else if(i==2){
                var.sched_priority=((sched_get_priority_min(SCHED_FIFO)+sched_get_priority_max(SCHED_FIFO)))/2;//default priority
                sched_setscheduler(0,SCHED_FIFO,&var);//to set scheduling algo to SCHED_FIFO
                execl("./count3","trap1","trap2",NULL);
                perror("Some error in execl");

            }
        }
    }
    double other;
    double rr;
    double fifo;
    pid_t pid;

    while ((pid = waitpid(-1, 0, 0)) > 0) {
        clock_gettime(CLOCK_REALTIME,&end);
        if (pid == rc[0]) {
            other=(end.tv_sec - begin[0].tv_sec)+(end.tv_nsec - begin[0].tv_nsec) / 1e9;
            printf("Duration for other process: %f seconds\n", other);
        }

        else if (pid == rc[1]) {
            rr=(end.tv_sec - begin[1].tv_sec)+(end.tv_nsec - begin[1].tv_nsec) / 1e9;
            printf("Duration for RR process: %f seconds\n", rr);
        }

        else if (pid == rc[2]) {
            fifo=(end.tv_sec - begin[2].tv_sec)+(end.tv_nsec - begin[2].tv_nsec) / 1e9;
            printf("Duration for FIFO process: %f seconds\n", fifo);
        }
    }

    fprintf(file,"%f ",other);
    fprintf(file,"%f ",rr);
    fprintf(file,"%f ",fifo);
    fclose(file);
    system("python3 ./plot.py");
    return 0;
}