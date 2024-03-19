#publisher for the pos


import rospy
#from std_msgs.msg import Float64 # from package.[msg/srv] import ["msg"/"srv"] 
from geometry_msgs.msg import Pose
pose_msg = Pose()

pose_msg.orientation.x = 0  #default quaternion value representing no rotation ([0, 0, 0, 1]).
pose_msg.orientation.y = 0
pose_msg.orientation.z = 0
pose_msg.orientation.w = 1

def pos_publisher():
    #pub = rospy.Publisher('data_topic', Float64, queue_size=10) # TOPIC
    
    pub = rospy.Publisher('chatter_', Pose, queue_size=10) # TOPIC NAme
    
    
    rospy.init_node('talker', anonymous=True) #Node name


    rate = rospy.Rate(10) # 10hz
    
    k=0.2
    
    while not rospy.is_shutdown():


        #hello_str = "hello world %s" % k
        variable = k
        #pub.publish(variable)
        pose_msg.position.x = -k/1.5 ## - FOR THE DIRECTION 
        pose_msg.position.y = k/2.5
        pose_msg.position.z = k/3

        

        pub.publish(pose_msg)

        #rospy.loginfo('Envio: %s', variable)

        rospy.loginfo('SEND DATA: \n%s', pose_msg) ## PRINT THE DATA

        k=k+0.1
        
        rate.sleep()

if __name__ == '__main__':
    try:
        pos_publisher()
    except rospy.ROSInterruptException:
        pass
