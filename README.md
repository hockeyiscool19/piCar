# I am trying to build a self driving car

This readme will not only cover my project goals, what I achieve, and how I do it. I will also log the important sub-problems I solve along the way. 

## Documentation
### Windows Formatting Process
1. Insert SD card.
2. Go to command prompt typing diskpart
3. Enter commands:
```
DISKPART> list disk

DISKPART> select Disk 1

DISKPART> clean

DISKPART> list partition

DISKPART> create partition primary

DISKPART> format fs=ntfs quick

```
4. Go to Imager and re-download Pi OS. 

### See Pi through virtual machine
1. Enable screen sharing from pi. 
From Linux terminal on home computer:
```
ssh username@ip_address
```
Run commands from Pi: 
```
sudo apt update
sudo apt install xrdp
sudo systemctl enable xrdp
sudo systemctl start xrdp
hostname -I
```
2. Go to Windows Remote Desktop Connection.
3. Type in ip address and username of pi (which for me is pi).
4. Voila. 

# The Journey
## Outlook
In my journey, I hope to cover my more pragmatic challenges and realizations. At the end of the day, this project involves hardware, and so I hope to bring you through the engineering and design in addition to the machine learning. (I have never worked with embedded systems, so I will be learning along the way too!)
### Day 1
Today, I hit factory reset on my computer. I saw that the memory was 67% occupied before even executing any programs. This to me, has just caused tremendous slow downs in my computer. Thus, I faced challenges re-installing everything. Related to this project, this will be the first time I am using Neovim and C++ for any project. Setting up Neovim took time and installing packages was difficult too. 

One major problem I faced today was that I did not have an HDMI chord for my RasberryPi (Pi). Thus, I cannot plug it into my monitor. I came up with the solutuion of giving my Pi ethernet. I figured I could connect to my Pi through my local network. Making matters harder was that Pi runs on Ubuntu. Even though I run Ubuntu on my Windows computer through wsl, this causes issues, since I cannot connect to my Pi through the given GUI. This link, however, allows me to run Linux applications on my Windows computer: https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps.

### Day 2
Still having challenges ssh tunneling into my Pi. I suspect it is due to the SD card is not writing properly in my Windows system. I could solve these challenges with a GUI, but I found terminal commands to do this from my CLI, which I find more understandable. In addition to setting up my Pi, I am also assembling my PiCar. Along with assembling the car, I am also learning a bit about each part -- i.e., what is a linear actuator, chassis, etc. I am relatively surprised how similar this toy car is to a Tesla. For toy robot design and industrial car design, the ebst part is no part, or, as Bill Clinton sai, KISS.

After hours of work, I realized that I could find what devices were on my account through the Xfinity app, my home ISP. I found that connecting an ethernet cable was unnecessary, since my rasberry pi connected just fine. This process of downloading the Pi OS took at least ten times, which I found super time consuming and frustrating. Nonetheless, burning the OS onto thE SD card gave me time to assemble the car in part and brush up on some C++. 

### Day 3
I successfully built the car, downloaded all the PiCar packages, and connected remotely into the Pi. ```Cheese``` allows me to display the camera. The car can even drive around now! 
