import rospy
from geometry_msgs.msg import Pose
#from geometry_msgs.msg import Pose
def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('/chatter_', Pose, callback) #TOPIC

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

def callback(data):
    #mensaje=data.position.y
    
    rospy.loginfo('DATA DRONE_1 RECIVED: \n%s',data)
    
if __name__ == '__main__':
    listener()
