# XPCListener.InitializationOptions

**Framework**: XPC  
**Kind**: struct

Options that control the listener’s configuration, such as if it’s inactive at creation.

**Availability**:
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
struct InitializationOptions
```

## Topics

### Listener creation options
- [static let inactive: XPCListener.InitializationOptions](xpclistener/initializationoptions/inactive.md)
  Indicates that the listener isn’t activated during its creation.
- [static let none: XPCListener.InitializationOptions](xpclistener/initializationoptions/none.md)
  Indicates that the listener uses a default configuration during creation.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [init(service: String, targetQueue: DispatchQueue?, options: XPCListener.InitializationOptions, incomingSessionHandler: (XPCListener.IncomingSessionRequest) -> XPCListener.IncomingSessionRequest.Decision) throws](xpclistener/init(service:targetqueue:options:incomingsessionhandler:).md)
  Creates the server side of an XPC service using the specified service name.
- [XPCListener.IncomingSessionRequest](xpclistener/incomingsessionrequest.md)
  A session request from a client that you accept or reject.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpclistener/initializationoptions)*