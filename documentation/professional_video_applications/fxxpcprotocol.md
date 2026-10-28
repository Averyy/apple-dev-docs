# FxXPCProtocol

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

## Declaration

```swift
protocol FxXPCProtocol
```

```objc
@protocol FxXPCProtocol
```

## Overview

The protocol used by all FxPlug 4 plug-ins to initiate contact with the host application.

The plug-in should never use this protocol. It’s called by the host application only.

## Topics

### Instance Methods
- [func createNewConnection(forProcessID: pid_t, minimumVersion: Int, maximumVersion: Int, hostCapabilities: [AnyHashable : Any]!, reply: ((NSXPCListenerEndpoint?, (any Error)?) -> Void)!)](./fxxpcprotocol/createnewconnection%28forprocessid,minimumversion,maximumversion,hostcapabilities,reply%29.md)
- [func viewServiceListenerEndPoint(((NSXPCListenerEndpoint?) -> Void)!)](./fxxpcprotocol/viewservicelistenerendpoint%28_%29.md)

## Relationships

### Inherited By
- [PROXPCProtocol](./proxpcprotocol.md)
### Conforming Types
- [FxPrincipal](./fxprincipal.md)

## See Also

### Protocols
- [protocol PROAPIAccessing](./proapiaccessing.md)
- [protocol PROAPIObject](./proapiobject.md)
- [protocol PROPlugInRegistering](./propluginregistering.md)
- [protocol PROXPCProtocol](./proxpcprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxxpcprotocol)*