# FxPrincipalAPI

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

A protocol that provides an interface that the host application implements to retrieve an XPC proxy object for communicating with its XPC.

**Availability**:
- FxPlug 4.1+

## Declaration

```swift
protocol FxPrincipalAPI
```

```objc
@protocol FxPrincipalAPI
```

## Topics

### Getting XPC Proxy Objects
- [func servicePrincipal() -> Any!](./fxprincipalapi/serviceprincipal%28%29.md)
  Retrieves a pointer to the proxy object used for sandboxed out-of-process tasks.

## See Also

### Services
- [class FxPrincipal](./fxprincipal.md)
  Singleton object that starts your XPC service running and can return the embedded (in-process) component of your plug-in.
- [protocol FxPrincipalDelegate](./fxprincipaldelegate.md)
  A protocol that provides information about the host application that launched your XPC service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxprincipalapi)*