# FxPrincipalDelegate

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

A protocol that provides information about the host application that launched your XPC service.

**Availability**:
- FxPlug 4.1+

## Declaration

```swift
protocol FxPrincipalDelegate
```

```objc
@protocol FxPrincipalDelegate
```

## Overview

When the host application first launches your XPC Service, your XPC calls +[`startServicePrincipal(with:)`](./fxprincipal/startserviceprincipal%28with%29.md) to get communication with the host application started. Passing in a delegate allows you to know which host application and version launched your XPC service.

## Topics

### Instance Method
- [func didEstablishConnection(withHost: String!, version: String!)](./fxprincipaldelegate/didestablishconnection%28withhost,version%29.md)
  Notifies your XPC service that a connection was established with the host.

## See Also

### Services
- [class FxPrincipal](./fxprincipal.md)
  Singleton object that starts your XPC service running and can return the embedded (in-process) component of your plug-in.
- [protocol FxPrincipalAPI](./fxprincipalapi.md)
  A protocol that provides an interface that the host application implements to retrieve an XPC proxy object for communicating with its XPC.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxprincipaldelegate)*