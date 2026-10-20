# XPCListener.InitializationOptions

**Framework**: XPC  
**Kind**: struct  
**Role**: Structure

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
- [static let inactive: XPCListener.InitializationOptions](./initializationoptions/inactive.md)
  Indicates that the listener isn’t activated during its creation.
- [static let none: XPCListener.InitializationOptions](./initializationoptions/none.md)
  Indicates that the listener uses a default configuration during creation.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Creating a listener
- [init(service: String, targetQueue: DispatchQueue?, options: XPCListener.InitializationOptions, incomingSessionHandler: (XPCListener.IncomingSessionRequest) -> XPCListener.IncomingSessionRequest.Decision) throws](./init%28service,targetqueue,options,incomingsessionhandler%29.md)
  Creates the server side of an XPC service using the specified service name.
- [XPCListener.IncomingSessionRequest](./incomingsessionrequest.md)
  A session request from a client that you accept or reject.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpclistener/initializationoptions)*