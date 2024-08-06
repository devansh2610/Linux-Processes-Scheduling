
# import matplotlib.pyplot as plt
# ans=[]
# def format_yaxis(y, pos):
#     return f"{y:.6f}"
# with open("file.txt","r") as file1:
#     for line in file1:
#         ans=[]
#         values = line.split()
#         ans=list(map(float, line.split()))
#         priority = ['Priority 0', 'Priority 1', 'Priority 2']
#         plt.hist(ans, bins=50)
#         plt.xlabel('Priority')
#         plt.xticks([ans[0],ans[1],ans[2]],priority,rotation=45)
#         plt.yticks([ans[0],ans[1],ans[2]])
#         plt.ylabel('Time(seconds)')
#         plt.title('Histogram of process durations')
#         plt.show()
#         print(values)
# import matplotlib.pyplot as plt
# import numpy as np
# ans=[]
# so=[]
# sr=[]
# sf=[]
# c=0
# with open("file.txt","r") as file1:
#     for line in file1:
#         values = line.split()
#         ans=list(map(float, line.split()))
#         if(c==0):
#             so.append(ans[0])
#             sr.append(ans[1])
#             sf.append(ans[2])
#         if(c==1):
#             so.append(ans[1])
#             sr.append(ans[0])
#             sf.append(ans[2])
#         if(c==2):
#             so.append(ans[0])
#             sr.append(ans[2])
#             sf.append(ans[1])
#         if(c==3):
#             so.append(ans[2])
#             sr.append(ans[1])
#             sf.append(ans[0])
#         if(c==4):
#             so.append(ans[1])
#             sr.append(ans[0])
#             sf.append(ans[2])
#         if(c==5):
#             so.append(ans[1])
#             sr.append(ans[2])
#             sf.append(ans[0])
#         c+=1
# print(so)
# print(sr)
# print(sf)
# priority = ['Priority 0', 'Priority 1', 'Priority 0 again', 'Priority 2','Priority 1 again','Priority 1 again*']
# colors = ['m', 'k', 'c']
# fig, axs = plt.subplots(1, 3, figsize=(30, 6))
# def format_yaxis(y, pos):
#     return f"{y:.6f}"
# axs[0].hist(so, bins=80,color=colors[0])
# axs[0].set_xlabel('Priority')
# axs[0].set_ylabel('Time (seconds)')
# axs[0].set_title("Scheduler Other")
# # print(axs[0].get_xlim())

# # Assuming 'ax' is your Axes object
# axs[0].set_xticks(np.linspace(0,0.0000009, len(priority)))
# axs[0].set_xticklabels(priority,rotation=45)
# axs[0].yaxis.set_major_formatter(plt.FuncFormatter(format_yaxis))
# priority = ['Priority 1', 'Priority 0', 'Priority 2','Priority 1 again','Priority 0 again','Priority 2 again']

# axs[1].hist(sr, bins=80,color=colors[1])
# axs[1].set_xlabel('Priority')
# axs[1].set_ylabel('Time (seconds)')
# axs[1].set_title("Scheduler RR")
# axs[1].set_xticklabels(priority,rotation=45)
# axs[1].yaxis.set_major_formatter(plt.FuncFormatter(format_yaxis))
# priority = ['Priority 2', 'Priority 2 again', 'Priority 1', 'Priority 0','Priority 2 again*','Priority 0 again']
# axs[2].hist(sf, bins=80,color=colors[2])
# axs[2].set_xlabel('Priority')
# axs[2].set_ylabel('Time (seconds)')
# axs[2].set_title("Scheduler FIFO")
# axs[2].set_xticklabels(priority,rotation=45)
# axs[2].yaxis.set_major_formatter(plt.FuncFormatter(format_yaxis))
# names = ['SCHED_OTHER', 'SCHED_RR', 'SCHED_FIFO']
# plt.tight_layout()
# fig.legend(names, loc='upper left')
# plt.show()
#!/usr/bin/env python3
# import matplotlib.pyplot as plt
# ans=[]
# with open("file.txt","r") as file1:
#     for line in file1:
#         ans=[]
#         values = line.split()
#         ans=list(map(float, line.split()))
#         plt.hist(ans, bins=100)
#         plt.xlabel('Duration (seconds)')
#         plt.ylabel('Frequency')
#         plt.title('Histogram of process durations')
#         plt.show()
#  
#       print(values)


import matplotlib.pyplot as plt

ans=[]
so=[]
sr=[]
sf=[]

with open("file.txt","r") as file1:
    for line in file1:
        values = list(map(float, line.split()))
        so.append(values[0])
        sr.append(values[1])
        sf.append(values[2])

# print(sf)
# print(sr)
# print(sf)

priority = ['NICE:0 OTHER','DEFAULT RR','DEFAULT FIFO']
colors = ['m', 'k', 'c']
def format_yaxis(y, pos):
    return f"{y:.6f}"
all_values = [so, sr, sf]

# Plot each list with corresponding color and label
for i in range(len(all_values)):
    plt.bar(priority[i], all_values[i], color=colors[i])

plt.xlabel('Scheduling Policy')
plt.ylabel('Time(seconds)')
plt.title('Histogram of process durations')
plt.ylim(4, max(max(so), max(sr), max(sf))+0.2)
plt.gca().yaxis.set_major_formatter(format_yaxis)
plt.tight_layout()
names = ['SCHED_OTHER', 'SCHED_RR', 'SCHED_FIFO']
plt.legend(names, loc='upper left')
plt.show()

# fig, axs = plt.subplots(1, 3, figsize=(20, 6))
# def format_yaxis(y, pos):
#     return f"{y:.6f}"
# axs[0].bar(priority, so, color=colors[0])
# axs[0].set_xlabel('Priority')
# axs[0].set_ylabel('Time (seconds)')
# axs[0].set_title("Scheduler Other")
# axs[0].set_ylim([min(so)-0.4, max(so)+0.1])
# axs[0].yaxis.set_major_formatter(plt.FuncFormatter(format_yaxis))
# priority = ['Priority 1', 'Priority 0', 'Priority 2','Priority 1 again','Priority 0 again','Priority 2 again']

# axs[1].bar(priority, sr, color=colors[1])
# axs[1].set_xlabel('Priority')
# axs[1].set_ylabel('Time (seconds)')
# axs[1].set_title("Scheduler RR")
# axs[1].set_ylim([min(sr)-0.4, max(sr)+0.1])
# axs[1].yaxis.set_major_formatter(plt.FuncFormatter(format_yaxis))
# priority = ['Priority 2', 'Priority 2 again', 'Priority 1', 'Priority 0','Priority 2 again*','Priority 0 again']
# axs[2].bar(priority, sf, color=colors[2])
# axs[2].set_xlabel('Priority')
# axs[2].set_ylabel('Time (seconds)')
# axs[2].set_title("Scheduler FIFO")
# axs[2].set_ylim([min(sf)-0.4, max(sf)+0.1])
# axs[2].yaxis.set_major_formatter(plt.FuncFormatter(format_yaxis))
# names = ['SCHED_OTHER', 'SCHED_RR', 'SCHED_FIFO']
# plt.tight_layout()
# fig.legend(names, loc='upper left')
# plt.show()

# import matplotlib.pyplot as plt

# # Read durations from file
# with open('file.txt', 'r') as f:
#     for line in f:
#         values = line.split()
#         durations = list(map(float, line.split()))
# print(durations)
# temp=[1,2,3]
# # Create histogram
# plt.hist(temp, bins=6, color='blue')
# plt.xlabel('Time to Complete (seconds)')
# plt.ylabel('Frequency')
# plt.xticks(temp,['pr0','pr1','pr2'])
# plt.title('Histogram of Process Completion Times')
# plt.show()