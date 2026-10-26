# FxPrincipal

**Framework**: Professional Video Applications  
**Kind**: class  
**Role**: Class

Singleton object that starts your XPC service running and can return the embedded (in-process) component of your plug-in.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
class FxPrincipal
```

```objc
@interface FxPrincipal : NSObject
```

## Mentions

- [Editing property lists for FxPlug plug-ins](https://developer.apple.com/documentation/professional-video-applications/editing-property-lists-for-fxplug-plug-ins)

## Topics

### Type Methods
- [class func embeddedPrincipal() -> Any!](./fxprincipal/embeddedprincipal%28%29.md)
  Start your XPC service listening for connections from the host application.
- [class func startServicePrincipal()](./fxprincipal/startserviceprincipal%28%29.md)
  Start your XPC service listening for connections from the host application.
- [class func startServicePrincipal(with: (any FxPrincipalDelegate)!)](./fxprincipal/startserviceprincipal%28with%29.md)
  Start your XPC service listening for connections from the host application.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [FxXPCProtocol](./fxxpcprotocol.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [PROXPCProtocol](./proxpcprotocol.md)

## See Also

### Services
- [protocol FxPrincipalAPI](./fxprincipalapi.md)
  A protocol that provides an interface that the host application implements to retrieve an XPC proxy object for communicating with its XPC.
- [protocol FxPrincipalDelegate](./fxprincipaldelegate.md)
  A protocol that provides information about the host application that launched your XPC service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxprincipal)*