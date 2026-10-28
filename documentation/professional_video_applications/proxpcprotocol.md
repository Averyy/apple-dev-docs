# PROXPCProtocol

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

## Declaration

```swift
protocol PROXPCProtocol : FxXPCProtocol
```

```objc
@protocol PROXPCProtocol <FxXPCProtocol>
```

## Overview

The protocol used by PluginManager plug-ins that also handle dynamic registration.

The plug-in should never directly use this protocol. It’s called by the host application only. Plug-ins should, however, put this protocol name as the value for the Protocl key in the PluginKit section of their Info.plist file.

## Topics

### Instance Methods
- [func dynamicRegistrationEndpoint(forProcessID: pid_t, version: Int, reply: ((NSXPCListenerEndpoint?, (any Error)?) -> Void)!)](./proxpcprotocol/dynamicregistrationendpoint%28forprocessid,version,reply%29.md)
- [func newConnection(forProcessID: pid_t, minimumVersion: Int, maximumVersion: Int, hostCapabilities: [AnyHashable : Any]!, reply: ((NSXPCListenerEndpoint?, Int, (any Error)?) -> Void)!)](./proxpcprotocol/newconnection%28forprocessid,minimumversion,maximumversion,hostcapabilities,reply%29.md)

## Relationships

### Inherits From
- [FxXPCProtocol](./fxxpcprotocol.md)
### Conforming Types
- [FxPrincipal](./fxprincipal.md)

## See Also

### Protocols
- [protocol FxXPCProtocol](./fxxpcprotocol.md)
- [protocol PROAPIAccessing](./proapiaccessing.md)
- [protocol PROAPIObject](./proapiobject.md)
- [protocol PROPlugInRegistering](./propluginregistering.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/proxpcprotocol)*