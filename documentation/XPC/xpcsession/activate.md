# activate()

**Framework**: Xpc  
**Kind**: method

Activates a session so you can send messages.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
func activate() throws
```

#### Discussion

> ❗ **Important**:  Don’t call [`activate()`](xpcsession/activate().md) on a session that’s already active.

 Don’t call [`activate()`](xpcsession/activate().md) on a session that’s already active.

If you create an inactive session using the [`inactive`](xpcsession/initializationoptions/inactive.md) initialization option, you must activate the session before deinitialization. Deinitializing an inactive session causes the process to crash.

If activation fails, this method automatically cancels the session and throws a [`XPCRichError`](xpcricherror.md) that describes the reason activation failed.

## See Also

- [func setIncomingMessageHandler<Message>((Message) -> (any Encodable)?)](xpcsession/setincomingmessagehandler(_:)-2ukdh.md)
  Sets a closure to receive incoming decodable messages for a session.
- [func setIncomingMessageHandler((XPCReceivedMessage) -> (any Encodable)?)](xpcsession/setincomingmessagehandler(_:)-5lu26.md)
  Sets a closure to receive incoming received messages for a session.
- [func setIncomingMessageHandler((XPCDictionary) -> XPCDictionary?)](xpcsession/setincomingmessagehandler(_:)-75ou9.md)
  Sets a closure to receive incoming dictionary messages for a session.
- [func cancel(reason: String)](xpcsession/cancel(reason:).md)
  Cancels a session, discarding any unsent messages.
- [func setCancellationHandler((XPCRichError) -> Void)](xpcsession/setcancellationhandler(_:).md)
  Sets a closure the session calls when it’s canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcsession/activate())*