# send(_:replyHandler:)

**Framework**: Xpc  
**Kind**: method

Sends an encodable message over the session to the destination service, using the closure you specify to handle a reply.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
func send<Message, Reply>(_ message: Message, replyHandler: @escaping (Result<Reply, any Error>) -> Void) throws where Message : Encodable, Reply : Decodable
```

#### Discussion

Sessions send messages serially in a first-in, first-out (FIFO) order. This method is safe to call from multiple dispatch queues. The session can’t indicate whether the message  is successful or not. While the session may successfully enqueue the message at the remote end of the connection, there’s no guarantee about when the destination dequeues the message and invokes the receiving session’s handler.

If the session fails to send the message, this method throws an error that contains details about the failure.

If the system tears down the session’s connection before receiving a reply, it invokes `replyHandler` with a result containing an [`XPCRichError`](xpcricherror.md) describing the failure. For example, the remote service exits prematurely before sending a reply.

> ❗ **Important**:  If you create an inactive session, you must activate it before sending messages. Calling this method with an inactive session crashes.

 If you create an inactive session, you must activate it before sending messages. Calling this method with an inactive session crashes.

## Parameters

- `message`: An encodable object that contains the message to send.
- `replyHandler`: A closure that receives a reply, and error if one occurs, that the service sends back.

## See Also

- [func send<Message>(Message) throws](xpcsession/send(_:).md)
  Sends an encodable message over the session to the destination service.
- [func send<Message>(Message, replyHandler: (Result<XPCReceivedMessage, XPCRichError>) -> Void) throws](xpcsession/send(_:replyhandler:)-3wjln.md)
  Sends an encodable message over the session to the destination service, using the closure you specify to handle a reply and rich error.
- [func send(message: XPCDictionary) throws](xpcsession/send(message:).md)
  Sends a dictionary message over the session to the destination service.
- [func send(message: XPCDictionary, replyHandler: (Result<XPCDictionary, XPCRichError>) -> Void)](xpcsession/send(message:replyhandler:).md)
  Sends a message asynchronously over the session to the destination service, calling a closure after receiving a reply.
- [func sendSync<Message>(Message) throws -> XPCReceivedMessage](xpcsession/sendsync(_:)-8a284.md)
  Sends an encodable message over the session to the destination service, blocking the caller until receiving a reply message.
- [func sendSync<Message, Reply>(Message) throws -> Reply](xpcsession/sendsync(_:)-88u0s.md)
  Sends an encodable message over the session to the destination service, blocking the caller until receiving an encodable reply message.
- [func sendSync(message: XPCDictionary) throws -> XPCDictionary](xpcsession/sendsync(message:).md)
  Sends a dictionary message over the session to the destination service, blocking the caller until receiving a reply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcsession/send(_:replyhandler:)-9an0u)*