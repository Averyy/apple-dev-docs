# setTargetQueue(_:)

**Framework**: Xpc  
**Kind**: method

Sets the target dispatch queue on an inactive session for processing messages.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
func setTargetQueue(_ targetQueue: DispatchQueue)
```

## Parameters

- `targetQueue`: The dispatch queue where the session processes messages. The target queue can be a concurrent queue.

## See Also

- [convenience init<Message>(xpcService: String, targetQueue: DispatchQueue?, options: XPCSession.InitializationOptions, incomingMessageHandler: ((Message) -> (any Encodable)?)?, cancellationHandler: ((XPCRichError) -> Void)?) throws](xpcsession/init(xpcservice:targetqueue:options:incomingmessagehandler:cancellationhandler:)-407h2.md)
  Establishes a connection to an XPC service with the name and decodable message handler you specify.
- [convenience init(xpcService: String, targetQueue: DispatchQueue?, options: XPCSession.InitializationOptions, incomingMessageHandler: ((XPCReceivedMessage) -> (any Encodable)?)?, cancellationHandler: ((XPCRichError) -> Void)?) throws](xpcsession/init(xpcservice:targetqueue:options:incomingmessagehandler:cancellationhandler:)-9f4u0.md)
  Establishes a connection to an XPC service with the name and received message handler you specify.
- [convenience init(xpcService: String, targetQueue: DispatchQueue?, options: XPCSession.InitializationOptions, incomingMessageHandler: ((XPCDictionary) -> XPCDictionary?)?, cancellationHandler: ((XPCRichError) -> Void)?) throws](xpcsession/init(xpcservice:targetqueue:options:incomingmessagehandler:cancellationhandler:)-bel3.md)
  Establishes a connection to an XPC service with the name and dictionary message handler you specify.
- [convenience init(xpcService: String, targetQueue: DispatchQueue?, options: XPCSession.InitializationOptions, cancellationHandler: ((XPCRichError) -> Void)?) throws](xpcsession/init(xpcservice:targetqueue:options:cancellationhandler:).md)
  Establishes a connection to an XPC service with the name you specify.
- [convenience init<Message>(machService: String, targetQueue: DispatchQueue?, options: XPCSession.InitializationOptions, incomingMessageHandler: ((Message) -> (any Encodable)?)?, cancellationHandler: ((XPCRichError) -> Void)?) throws](xpcsession/init(machservice:targetqueue:options:incomingmessagehandler:cancellationhandler:)-l3rz.md)
  Establishes a connection to a launch agent or launch daemon with the name and decodable message handler you specify.
- [convenience init(machService: String, targetQueue: DispatchQueue?, options: XPCSession.InitializationOptions, incomingMessageHandler: ((XPCReceivedMessage) -> (any Encodable)?)?, cancellationHandler: ((XPCRichError) -> Void)?) throws](xpcsession/init(machservice:targetqueue:options:incomingmessagehandler:cancellationhandler:)-2xuyi.md)
  Establishes a connection to a launch agent or launch daemon with the name and received message handler you specify.
- [convenience init(machService: String, targetQueue: DispatchQueue?, options: XPCSession.InitializationOptions, incomingMessageHandler: ((XPCDictionary) -> XPCDictionary?)?, cancellationHandler: ((XPCRichError) -> Void)?) throws](xpcsession/init(machservice:targetqueue:options:incomingmessagehandler:cancellationhandler:)-6jz7y.md)
  Establishes a connection to a launch agent or launch daemon with the name and dictionary message handler you specify.
- [convenience init(machService: String, targetQueue: DispatchQueue?, options: XPCSession.InitializationOptions, cancellationHandler: ((XPCRichError) -> Void)?) throws](xpcsession/init(machservice:targetqueue:options:cancellationhandler:).md)
  Establishes a connection to a launch agent or launch daemon with the name you specify.
- [XPCSession.InitializationOptions](xpcsession/initializationoptions.md)
  Options that control the session’s configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcsession/settargetqueue(_:))*