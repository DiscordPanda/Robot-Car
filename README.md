
# Mission 1
Mission 1 objective:
1. Setup a goal post of width 25cm at any scale you like (mini or lifesize)
2. Place the robot exactly at 5m from the center of the goalpost and centered to the width of the post and facing the goalpost
3. Select any ball of your choice (feel free to fashion one if you would like).
4. Feel free to add/remove things from the bot. Mission is key. 
5. You can only add materials that are regarded scrap. No buying a part OR 3D printing.

**Activity**: Push the ball using the movement of the robot (or moving any accessory added to the bot) into the goal post. 

## Requirements
- Any used ball that is light and small
- GoPiGo3 robot kit assembled
- Download and install Raspbian for Robots [Raspbian for Robots](https://www.dexterindustries.com/howto/install-raspbian-for-robots-image-on-an-sd-card/)
- Connect to the GoPiGo3 with the Raspbian for Robots Operating System [Connect](https://www.dexterindustries.com/GoPiGo/get-started-with-the-gopigo3-raspberry-pi-robot/2-connect-to-the-gopigo-3/Raspbian-For-Robots-Operating-System/)

## Robot Modification(s)
- Using recycled parts, design and create an arm-like apparatus to improve control on the ball

## Terminal setup
```bash
pip install curtsies
```
```bash
pip install gopigo3
```
## How to start running the code
- Download [gpgv2m1.py](gpgv2m1.py) and move it onto the desktop via VNC
- Open up the terminal and go to the directory in which the gpgv2m1.py is located
- run the command
```bash
python gpgv2m1.py
```
The terminal should return this:
```lua
"w" : ["Move the GoPiGo3 forward", "forward"],
"s" : ["Move the GoPiGo3 backward", "backward"],
"a" : ["Turn the GoPiGo3 to the left", "left"],
"d" : ["Turn the GoPiGo3 to the right", "right"],
"<SPACE>" : ["Stop the GoPiGo3 from moving", "stop"],

"<F1>" : ["Drive forward for 495 (almost 5m) centimeters", "forward495cm"],
"<F2>" : ["Drive forward for 10 inches", "forward10in"],
"<F3>" : ["Drive forward for 360 degrees (aka 1 wheel rotation)", "forwardturn"],

"1" : ["Turn ON/OFF left blinker of the GoPiGo3", "leftblinker"],
"2" : ["Turn ON/OFF right blinker of the GoPiGo3", "rightblinker"],
"3" : ["Turn ON/OFF both blinkers of the GoPiGo3", "blinkers"],

"8" : ["Turn ON/OFF left eye of the GoPiGo3", "lefteye"],
"9" : ["Turn ON/OFF right eye of the GoPiGo3", "righteye"],
"0" : ["Turn ON/OFF both eyes of the GoPiGo3", "eyes"],

"<INSERT>" : ["Change the eyes' color on the go", "eyescolor"],

"<ESC>" : ["Exit", "exit"]
```
For the mission, we will be testing out and using the F1 key to start the robot
For manual controls, we can use the keybinds:

- `w` : ["Move the GoPiGo3 forward", "forward"]
- `s` : ["Move the GoPiGo3 backward", "backward"]
- `a` : ["Turn the GoPiGo3 to the left", "left"]
- `d` : ["Turn the GoPiGo3 to the right", "right"]
- `<space>` : ["Stop the GoPiGo3 from moving", "stop"]

## Mission Environment Set-Up
- Create goal posts 5 meters away from the robot's start position
- Set up 2 goal posts 25 cm away from one another
