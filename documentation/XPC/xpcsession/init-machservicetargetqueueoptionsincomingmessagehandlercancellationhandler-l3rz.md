# init(machService:targetQueue:options:incomingMessageHandler:cancellationHandler:)

**Framework**: Xpc  
**Kind**: init

Establishes a connection to a launch agent or launch daemon with the name and decodable message handler you specify.

**Availability**:
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
convenience init<Message>(machService: String, targetQueue: DispatchQueue? = nil, options: XPCSession.InitializationOptions = .none, incomingMessageHandler: ((Message) -> (any Encodable)?)? = nil, cancellationHandler: ((XPCRichError) -> Void)? = nil) throws where Message : Decodable
```

#### Discussion

If the service isn’t found or is unavailable, the connection fails and this method throws an error.

By default, this method activates the session it creates and the session is ready to accept messages. To create an inactive session, specify [`inactive`](xpcsession/initializationoptions/inactive.md) in the `options` parameter.

## Parameters

- `machService`: The name of the Mach service to connect to. The service name must exist in the Mach bootstrap accessible to the process and advertised in a  .
- `targetQueue`: The dispatch queue to use for session events. You can specify a concurrent dispatch queue. If you specify  , the session uses  .
- `options`: Attributes the session uses when establishing the connection.
- `incomingMessageHandler`: A closure the system calls when a client initiates a connection to the server.
- `cancellationHandler`: A closure the system calls when it cancels a session.

## See Also

- [convenience init<Message>(xpcService: String, targetQueue: DispatchQueue?, options: XPCSession.InitializationOptions, incomingMessageHandler: ((Message) -> (any Encodable)?)?, cancellationHandler: ((XPCRichError) -> Void)?) throws](xpcsession/init(xpcservice:targetqueue:options:incomingmessagehandler:cancellationhandler:)-407h2.md)
  Establishes a connection to an XPC service with the name and decodable message handler you specify.
- [convenience init(xpcService: String, targetQueue: DispatchQueue?, options: XPCSession.InitializationOptions, incomingMessageHandler: ((XPCReceivedMessage) -> (any Encodable)?)?, cancellationHandler: ((XPCRichError) -> Void)?) throws](xpcsession/init(xpcservice:targetqueue:options:incomingmessagehandler:cancellationhandler:)-9f4u0.md)
  Establishes a connection to an XPC service with the name and received message handler you specify.
- [convenience init(xpcService: String, targetQueue: DispatchQueue?, options: XPCSession.InitializationOptions, incomingMessageHandler: ((XPCDictionary) -> XPCDictionary?)?, cancellationHandler: ((XPCRichError) -> Void)?) throws](xpcsession/init(xpcservice:targetqueue:options:incomingmessagehandler:cancellationhandler:)-bel3.md)
  Establishes a connection to an XPC service with the name and dictionary message handler you specify.
- [convenience init(xpcService: String, targetQueue: DispatchQueue?, options: XPCSession.InitializationOptions, cancellationHandler: ((XPCRichError) -> Void)?) throws](xpcsession/init(xpcservice:targetqueue:options:cancellationhandler:).md)
  Establishes a connection to an XPC service with the name you specify.
- [convenience init(machService: String, targetQueue: DispatchQueue?, options: XPCSession.InitializationOptions, incomingMessageHandler: ((XPCReceivedMessage) -> (any Encodable)?)?, cancellationHandler: ((XPCRichError) -> Void)?) throws](xpcsession/init(machservice:targetqueue:options:incomingmessagehandler:cancellationhandler:)-2xuyi.md)
  Establishes a connection to a launch agent or launch daemon with the name and received message handler you specify.
- [convenience init(machService: String, targetQueue: DispatchQueue?, options: XPCSession.InitializationOptions, incomingMessageHandler: ((XPCDictionary) -> XPCDictionary?)?, cancellationHandler: ((XPCRichError) -> Void)?) throws](xpcsession/init(machservice:targetqueue:options:incomingmessagehandler:cancellationhandler:)-6jz7y.md)
  Establishes a connection to a launch agent or launch daemon with the name and dictionary message handler you specify.
- [convenience init(machService: String, targetQueue: DispatchQueue?, options: XPCSession.InitializationOptions, cancellationHandler: ((XPCRichError) -> Void)?) throws](xpcsession/init(machservice:targetqueue:options:cancellationhandler:).md)
  Establishes a connection to a launch agent or launch daemon with the name you specify.
- [XPCSession.InitializationOptions](xpcsession/initializationoptions.md)
  Options that control the session’s configuration.
- [func setTargetQueue(DispatchQueue)](xpcsession/settargetqueue(_:).md)
  Sets the target dispatch queue on an inactive session for processing messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcsession/init(machservice:targetqueue:options:incomingmessagehandler:cancellationhandler:)-l3rz)*