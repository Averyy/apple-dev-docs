# setTargetQueue(_:)

**Framework**: XPC  
**Kind**: method  
**Role**: Instance Method

Sets the target dispatch queue on an inactive session for processing messages.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS
- watchOS 10.0+

## Declaration

```swift
func setTargetQueue(_ targetQueue: DispatchQueue)
```

## Parameters

- `targetQueue`: The dispatch queue where the session processes messages. The target queue can be a concurrent queue.

## See Also

### Creating a session
- [convenience init<Message>(xpcService: String, targetQueue: DispatchQueue?, options: XPCSession.InitializationOptions, incomingMessageHandler: ((Message) -> (any Encodable)?)?, cancellationHandler: ((XPCRichError) -> Void)?) throws](./init%28xpcservice,targetqueue,options,incomingmessagehandler,cancellationhandler%29-407h2.md)
  Establishes a connection to an XPC service with the name and decodable message handler you specify.
- [convenience init(xpcService: String, targetQueue: DispatchQueue?, options: XPCSession.InitializationOptions, incomingMessageHandler: ((XPCReceivedMessage) -> (any Encodable)?)?, cancellationHandler: ((XPCRichError) -> Void)?) throws](./init%28xpcservice,targetqueue,options,incomingmessagehandler,cancellationhandler%29-9f4u0.md)
  Establishes a connection to an XPC service with the name and received message handler you specify.
- [convenience init(xpcService: String, targetQueue: DispatchQueue?, options: XPCSession.InitializationOptions, incomingMessageHandler: ((XPCDictionary) -> XPCDictionary?)?, cancellationHandler: ((XPCRichError) -> Void)?) throws](./init%28xpcservice,targetqueue,options,incomingmessagehandler,cancellationhandler%29-bel3.md)
  Establishes a connection to an XPC service with the name and dictionary message handler you specify.
- [convenience init(xpcService: String, targetQueue: DispatchQueue?, options: XPCSession.InitializationOptions, cancellationHandler: ((XPCRichError) -> Void)?) throws](./init%28xpcservice,targetqueue,options,cancellationhandler%29.md)
  Establishes a connection to an XPC service with the name you specify.
- [convenience init<Message>(machService: String, targetQueue: DispatchQueue?, options: XPCSession.InitializationOptions, incomingMessageHandler: ((Message) -> (any Encodable)?)?, cancellationHandler: ((XPCRichError) -> Void)?) throws](./init%28machservice,targetqueue,options,incomingmessagehandler,cancellationhandler%29-l3rz.md)
  Establishes a connection to a launch agent or launch daemon with the name and decodable message handler you specify.
- [convenience init(machService: String, targetQueue: DispatchQueue?, options: XPCSession.InitializationOptions, incomingMessageHandler: ((XPCReceivedMessage) -> (any Encodable)?)?, cancellationHandler: ((XPCRichError) -> Void)?) throws](./init%28machservice,targetqueue,options,incomingmessagehandler,cancellationhandler%29-2xuyi.md)
  Establishes a connection to a launch agent or launch daemon with the name and received message handler you specify.
- [convenience init(machService: String, targetQueue: DispatchQueue?, options: XPCSession.InitializationOptions, incomingMessageHandler: ((XPCDictionary) -> XPCDictionary?)?, cancellationHandler: ((XPCRichError) -> Void)?) throws](./init%28machservice,targetqueue,options,incomingmessagehandler,cancellationhandler%29-6jz7y.md)
  Establishes a connection to a launch agent or launch daemon with the name and dictionary message handler you specify.
- [convenience init(machService: String, targetQueue: DispatchQueue?, options: XPCSession.InitializationOptions, cancellationHandler: ((XPCRichError) -> Void)?) throws](./init%28machservice,targetqueue,options,cancellationhandler%29.md)
  Establishes a connection to a launch agent or launch daemon with the name you specify.
- [XPCSession.InitializationOptions](./initializationoptions.md)
  Options that control the session’s configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcsession/settargetqueue(_:))*