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
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [init(service: String, targetQueue: DispatchQueue?, options: XPCListener.InitializationOptions, incomingSessionHandler: (XPCListener.IncomingSessionRequest) -> XPCListener.IncomingSessionRequest.Decision) throws](xpclistener/init(service:targetqueue:options:incomingsessionhandler:).md)
  Creates the server side of an XPC service using the specified service name.
- [XPCListener.IncomingSessionRequest](xpclistener/incomingsessionrequest.md)
  A session request from a client that you accept or reject.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpclistener/initializationoptions)*