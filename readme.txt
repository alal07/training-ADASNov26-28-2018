Step1:create directory and initialize ros workspace

mkdir catkin_ws
cd catkin_ws
mkdir src
cd src
catkin_init_workspace

cd ~/catkin_ws
catkin_make 

echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc

step2:create ros package 
cd src
catkin_create_pkg p1py rospy std_msgs

copy the souce code files "talker.py"&"listener.py" into /home/learningbee/catkin_ws/src/p1py/src/scripts

step3:make python scripts as executable
chmod +x talker.py
chmod +x listener.py

step4:ros build
cd ~/catkin_ws
catkin_make


ste5:run ros package

step5.1:open termminal1
roscore

step 5.2
open terminal 2
rosrun p1py talker.py

step5.3
open terminal 3
rosrun p1py listener.py

step6:to see the ros nodes
open terminal 4
rosrun rqt_graph rqt_graph



ifthere is any runtime issue then plz check the source path of ros workspace is added into "~/.bashrc"
gedit ~/.bashrc



