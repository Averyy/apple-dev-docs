# sendMessage(_:replyHandler:errorHandler:)

**Framework**: Watchconnectivity  
**Kind**: method

Sends a message immediately to the paired and active device and optionally handles a response.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func sendMessage(_ message: [String : Any], replyHandler: (([String : Any]) -> Void)?, errorHandler: ((any Error) -> Void)? = nil)
```

#### Discussion

Use this message to send a dictionary of data to the counterpart as soon as possible. Messages are queued serially and delivered in the order in which you sent them. Delivery of the messages happens asynchronously, so this method returns immediately.

If you specify a reply handler block, your handler block is executed asynchronously on a background thread. The block is executed serially with respect to other incoming delegate messages.

Calling this method from your WatchKit extension while it is active and running wakes up the corresponding iOS app in the background and makes it reachable. Calling this method from your iOS app does not wake up the corresponding WatchKit extension. If you call this method and the counterpart is unreachable (or becomes unreachable before the message is delivered), the `errorHandler` block is executed with an appropriate error. The `errorHandler` block may also be called if the `message` parameter contains non property list data types.

This method can only be called while the session is active—that is, the [`activationState`](wcsession/activationstate.md) property is set to  [`WCSessionActivationState.activated`](wcsessionactivationstate/activated.md). Calling this method for an inactive or deactivated session is a programmer error.

## Parameters

- `message`: A dictionary of property list values that you want to send. You define the contents of the dictionary that your counterpart supports. This parameter must not be  .
- `replyHandler`: A reply handler for receiving a response from the counterpart. Specify   if you do not want to receive a reply. This block has no return value and takes the following parameter:
- `errorHandler`: A block that is executed when an error occurs. Specify   if you do not care about error information. This block has no return value and takes the following parameter:

## See Also

- [func sendMessageData(Data, replyHandler: ((Data) -> Void)?, errorHandler: ((any Error) -> Void)?)](wcsession/sendmessagedata(_:replyhandler:errorhandler:).md)
  Sends a data object immediately to the paired and active device and optionally handles a response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsession/sendmessage(_:replyhandler:errorhandler:))*