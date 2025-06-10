# session(_:didReceiveMessageData:replyHandler:)

**Framework**: Watch Connectivity  
**Kind**: method

Tells the delegate that an immediate data message has arrived, and it requires a response.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func session(_ session: WCSession, didReceiveMessageData messageData: Data, replyHandler: @escaping (Data) -> Void)
```

#### Discussion

This method is called in response to a message sent by the counterpart process using the [`sendMessageData(_:replyHandler:errorHandler:)`](wcsession/sendmessagedata(_:replyhandler:errorhandler:).md) method. This specific method is called when the counterpart specifies a valid reply handler, indicating that it wants a response. Use this method to process the message data and provide an appropriate reply. You must execute the `reply` block as part of your implementation.

Use messages to communicate quickly with the counterpart process. Messages can be sent and received only while both processes are active and running.

The delivery of multiple messages occurs serially, so your implementation of this method does not need to be reentrant. This method is called on a background thread of your app.

## Parameters

- `session`: The session object that received the data from its counterpart.
- `messageData`: The data object received from the counterpart. Use the contents of this object to determine what course of action to take.
- `replyHandler`: A reply block to execute with the response. This block has no return value and takes the following parameter:

## See Also

- [func session(WCSession, didReceiveMessage: [String : Any])](wcsessiondelegate/session(_:didreceivemessage:).md)
  Tells the delegate that an immediate message has arrived.
- [func session(WCSession, didReceiveMessage: [String : Any], replyHandler: ([String : Any]) -> Void)](wcsessiondelegate/session(_:didreceivemessage:replyhandler:).md)
  Tells the delegate that an immediate message has arrived, and it requires a response.
- [func session(WCSession, didReceiveMessageData: Data)](wcsessiondelegate/session(_:didreceivemessagedata:).md)
  Tells the delegate that an immediate data message has arrived.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/session(_:didreceivemessagedata:replyhandler:))*