# WKFrameInfo

**Framework**: WebKit  
**Kind**: class

An object that contains information about a frame on a webpage.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class WKFrameInfo
```

#### Overview

An instance of this class is a transient, data-only object; it does not uniquely identify a frame across multiple delegate method calls.

## Topics

### Inspecting frame information
- [var isMainFrame: Bool](wkframeinfo/ismainframe.md)
  A Boolean value indicating whether the frame is the web site’s main frame or a subframe.
- [var request: URLRequest](wkframeinfo/request.md)
  The frame’s current request.
- [var securityOrigin: WKSecurityOrigin](wkframeinfo/securityorigin.md)
  The frame’s security origin.
- [var webView: WKWebView?](wkframeinfo/webview.md)
  The web view that contains this frame and the containing webpage.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class WKUserContentController](wkusercontentcontroller.md)
  An object for managing interactions between JavaScript code and your web view, and for filtering content in your web view.
- [class WKContentRuleListStore](wkcontentruleliststore.md)
  An object that contains the rules for how to load and filter content in the web view.
- [class WKContentWorld](wkcontentworld.md)
  An object that defines a scope of execution for JavaScript code, and which you use to prevent conflicts between different scripts.
- [class WKSecurityOrigin](wksecurityorigin.md)
  An object that identifies the origin of a particular resource.
- [class WKUserScript](wkuserscript.md)
  A script that the web view injects into a webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkframeinfo)*