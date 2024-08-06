This program demonstrates process scheduling in a Linux environment using three different scheduling algorithms: SCHED_OTHER, SCHED_RR (Round Robin), and SCHED_FIFO (First-In-First-Out). The program also measures the execution time of each process and records the results in a file for further analysis.

NOTE: Please use sudo to run the ./ans file.

CPU Affinity Setting: The program starts by setting the CPU affinity to CPU core 1 using `sched_setaffinity`. This ensures that all child processes will run on this specific core.
Forking Three Child Processes: Three child processes (`count1`, `count2`, and `count3`) are forked. They are using execl. Each child process performs a computation task and then exits.

Scheduling and Priority Configuration:
   - `count1` uses the default scheduling algorithm `SCHED_OTHER` with a nice value of 0.
   - `count2` uses `SCHED_RR` with a priority set to the midpoint between the minimum and maximum priorities for `SCHED_RR` (default priority).
   - `count3` uses `SCHED_FIFO` with a priority set to the midpoint between the minimum and maximum priorities for `SCHED_FIFO` (default priority).


Measurement of Execution Time: The parent process waits for the termination of all child processes using `waitpid` and records the execution times for each process.

Output to File: The execution times for each process (other, RR, and FIFO) are written to a file named `file.txt`.

Plotting Results: The program then uses a Python script (`plot.py`) to generate plots from the recorded data.




Outcomes and Measurements

Scheduling Algorithms
SCHED_OTHER (Other): This scheduling algorithm is designed for non-real-time tasks. In this program, `count1` uses `SCHED_OTHER`. It has the lowest priority and shares CPU time with other processes, including system tasks.
SCHED_RR (Round Robin): `count2` uses `SCHED_RR`, a real-time scheduling algorithm that provides each process with a time slice. It has a moderate priority compared to `SCHED_FIFO`.
SCHED_FIFO (First-In-First-Out): `count3` uses `SCHED_FIFO`, a real-time scheduling algorithm with higher priority than `SCHED_RR`. It gives absolute priority to the process until it completes.

Execution Time Measurements
- The execution time is measured using the `clock_gettime` function before and after each child process.
- The measured times are recorded in seconds and nanoseconds and then converted to a floating-point value for easier analysis.

Results Analysis
- The program records the execution time for each scheduling algorithm (`other`, `RR`, and `FIFO`) in the `file.txt` file.
- The Python script (`plot.py`) can be used to visualize and analyze the execution times to observe the impact of different scheduling algorithms on the execution of tasks.

Conclusion
This program showcases process scheduling with different algorithms in a Linux environment and measures the execution times of each process. The recorded data can be analyzed to understand how different scheduling policies affect the execution of tasks, providing insights into real-time and non-real-time scheduling behaviors on a specific CPU core.
