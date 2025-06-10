# sendSync(message:)

**Framework**: XPC  
**Kind**: method

Sends a dictionary message over the session to the destination service, blocking the caller until receiving a reply.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
func sendSync(message: XPCDictionary) throws -> XPCDictionary
```

#### Return Value

If successful, the response to the message; otherwise this method throws an error.

#### Discussion

This method supports priority inversion avoidance. Use this method instead of calling [`send(message:replyHandler:)`](xpcsession/send(message:replyhandler:).md) and using a semaphore.

Be judicious about your use of this API. It can block indefinitely. Calling this method while the session’s target queue is blocked may lead to deadlocks in certain scenarios. For that reason, invoking this method from the session’s target queue results in a crash.

> 💡 **Tip**:  If you provide an API that uses this method, consider allowing callers to specify a queue and callback handler to let you provide results asynchronously.

Sessions send messages serially in a first-in, first-out (FIFO) order. This method is safe to call from multiple dispatch queues. The session can’t indicate whether the message  is successful or not. While the session may successfully enqueue the message at the remote end of the connection, there’s no guarantee about when the destination dequeues the message and invokes the receiving session’s handler.

> ❗ **Important**:  If you create an inactive session, you must activate it before sending messages. Calling this method with an inactive session crashes.

## Parameters

- `message`: A dictionary object that contains the message to send.

## See Also

- [func send<Message>(Message) throws](xpcsession/send(_:).md)
  Sends an encodable message over the session to the destination service.
- [func send<Message>(Message, replyHandler: (Result<XPCReceivedMessage, XPCRichError>) -> Void) throws](xpcsession/send(_:replyhandler:)-3wjln.md)
  Sends an encodable message over the session to the destination service, using the closure you specify to handle a reply and rich error.
- [func send<Message, Reply>(Message, replyHandler: (Result<Reply, any Error>) -> Void) throws](xpcsession/send(_:replyhandler:)-9an0u.md)
  Sends an encodable message over the session to the destination service, using the closure you specify to handle a reply.
- [func send(message: XPCDictionary) throws](xpcsession/send(message:).md)
  Sends a dictionary message over the session to the destination service.
- [func send(message: XPCDictionary, replyHandler: (Result<XPCDictionary, XPCRichError>) -> Void)](xpcsession/send(message:replyhandler:).md)
  Sends a message asynchronously over the session to the destination service, calling a closure after receiving a reply.
- [func sendSync<Message>(Message) throws -> XPCReceivedMessage](xpcsession/sendsync(_:)-8a284.md)
  Sends an encodable message over the session to the destination service, blocking the caller until receiving a reply message.
- [func sendSync<Message, Reply>(Message) throws -> Reply](xpcsession/sendsync(_:)-88u0s.md)
  Sends an encodable message over the session to the destination service, blocking the caller until receiving an encodable reply message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcsession/sendsync(message:))*