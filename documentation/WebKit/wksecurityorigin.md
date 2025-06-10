# WKSecurityOrigin

**Framework**: WebKit  
**Kind**: class

An object that identifies the origin of a particular resource.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class WKSecurityOrigin
```

#### Overview

A [`WKSecurityOrigin`](wksecurityorigin.md) object is a transient, data-only object that identifies the host name, protocol, and port number associated with a particular resource. You don’t create [`WKSecurityOrigin`](wksecurityorigin.md) objects directly. Instead, WebKit creates them for the resources it loads. A  load is any load URL has the same security origin as the requesting web site. First-party webpages can access each other’s resources, such as scripts and databases.

Because a [`WKSecurityOrigin`](wksecurityorigin.md) object is transient, it doesn’t uniquely identify a security origin across multiple delegate method calls.

## Topics

### Getting the Host Information
- [var host: String](wksecurityorigin/host.md)
  The security origin’s host.
- [var port: Int](wksecurityorigin/port.md)
  The security origin’s port.
### Getting the Host Protocol
- [var `protocol`: String](wksecurityorigin/protocol.md)
  The security origin’s protocol.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class WKUserContentController](wkusercontentcontroller.md)
  An object for managing interactions between JavaScript code and your web view, and for filtering content in your web view.
- [class WKContentRuleListStore](wkcontentruleliststore.md)
  An object that contains the rules for how to load and filter content in the web view.
- [class WKContentWorld](wkcontentworld.md)
  An object that defines a scope of execution for JavaScript code, and which you use to prevent conflicts between different scripts.
- [class WKFrameInfo](wkframeinfo.md)
  An object that contains information about a frame on a webpage.
- [class WKUserScript](wkuserscript.md)
  A script that the web view injects into a webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wksecurityorigin)*