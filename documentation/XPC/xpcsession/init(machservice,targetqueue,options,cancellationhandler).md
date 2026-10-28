# init(machService:targetQueue:options:cancellationHandler:)

**Framework**: XPC  
**Kind**: init  
**Role**: Initializer

Establishes a connection to a launch agent or launch daemon with the name you specify.

**Availability**:
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
@preconcurrency
convenience init(machService: String, targetQueue: DispatchQueue? = nil, options: XPCSession.InitializationOptions = .none, cancellationHandler: (@Sendable (XPCRichError) -> Void)? = nil) throws
```

## Discussion

If the service isn’t found or is unavailable, the connection fails and this method throws an error.

By default, this method activates the session it creates and the session is ready to accept messages. To create an inactive session, specify [`inactive`](./initializationoptions/inactive.md) in the `options` parameter.

## Parameters

- `machService`: The name of the Mach service to connect to. The service name must exist in the Mach bootstrap accessible to the process and advertised in a `launchd.plist`.
- `targetQueue`: The dispatch queue to use for session events. You can specify a concurrent dispatch queue. If you specify [`nil`](../../ObjectiveC/nil-227m0.md), the session uses `DISPATCH_TARGET_QUEUE_DEFAULT`.
- `options`: Attributes the session uses when establishing the connection.
- `cancellationHandler`: A closure the system calls when it cancels a session.

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
- [XPCSession.InitializationOptions](./initializationoptions.md)
  Options that control the session’s configuration.
- [func setTargetQueue(DispatchQueue)](./settargetqueue%28_%29.md)
  Sets the target dispatch queue on an inactive session for processing messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcsession/init(machservice:targetqueue:options:cancellationhandler:))*