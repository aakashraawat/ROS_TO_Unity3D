using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using RosSharp.RosBridgeClient;
using RosSharp.RosBridgeClient.MessageTypes.Std;


public class CarMovementSubscriber : MonoBehaviour
{
    public RosConnector rosConnector;
    public string topicName = "car_movement";
    public float movementSpeed = 5f;// u can change accordingly and than fix it by using private

    private bool isMessageReceived;
    private Vector3 receivedMovement;

    private void Start()
    {
        rosConnector.RosSocket.Subscribe<Float64MultiArray>(topicName, MessageReceived, (int)(1 / UnityEngine.Time.fixedDeltaTime)); // Adjust the throttle rate as needed
    }

    private void FixedUpdate()
    {
        if (isMessageReceived)
            ProcessMessage();
    }

    private void MessageReceived(Float64MultiArray message)
    {
        receivedMovement = new Vector3((float)message.data[0], 0, (float)message.data[1]);
        isMessageReceived = true;
    }

    private void ProcessMessage()
    {
        // Process the received message to move the car
        // Example: Translate the car based on the received x and z values
        transform.Translate(receivedMovement * movementSpeed * UnityEngine.Time.fixedDeltaTime);
        isMessageReceived = false;
    }
}


