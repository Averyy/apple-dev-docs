# XPCSession.InitializationOptions

**Framework**: XPC  
**Kind**: struct

Options that control the session’s configuration.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
struct InitializationOptions
```

## Topics

### Session creation options
- [static let inactive: XPCSession.InitializationOptions](xpcsession/initializationoptions/inactive.md)
  Indicates that the session isn’t activated during its creation.
- [static let privileged: XPCSession.InitializationOptions](xpcsession/initializationoptions/privileged.md)
  Indicates that the Mach service is in the priviledged Mach bootstrap.
- [static let none: XPCSession.InitializationOptions](xpcsession/initializationoptions/none.md)
  Indicates that the listener uses a default configuration during creation.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

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
- [func setTargetQueue(DispatchQueue)](xpcsession/settargetqueue(_:).md)
  Sets the target dispatch queue on an inactive session for processing messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcsession/initializationoptions)*