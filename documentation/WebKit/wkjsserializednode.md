# WKJSSerializedNode

**Framework**: WebKit  
**Kind**: class

A `WKJSSerializedNode` object contains the serialized representation of a DOM node

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class WKJSSerializedNode
```

#### Overview

There are various ways that JavaScript executing inside web content results in some return value being passed up to the WebKit application. Examples include calls to `[WKWebView evaluateJavaScript:...]`, `[WKWebView callAsyncJavaScript:...]`, and the body of a `WKScriptMessage`.

When application JavaScript returns a JavaScript value, the default behavior is to try to convert it to a foundational type. e.g. a JavaScript Number becomes an NSNumber, or a JavaScript array becomes an NSArray, etc.

When the return value is a DOM node, the default conversion is to “stringify” it and return that to the application as an NSString. If the JavaScript instead calls `window.webkit.serializeNode(...)` then WebKit will create a serialized representation of that node as the return value.

The node is an opaque object as far as the application is concerned, but it can be used as an argument to future JavaScript programs via `[WKWebView callAsyncJavaScript:...]`

Unlike `WKJSHandle` - which keeps an actual JavaScript object alive in its originating context - a `WKJSSerializedNode` is not attached to a live JavaScript object, and it can be used as an argument to a JavaScript program running in any context. e.g. In a different frame, or after a navigation.

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

## See Also

- [class WKUserContentController](wkusercontentcontroller.md)
  An object for managing interactions between JavaScript code and your web view, and for filtering content in your web view.
- [class WKContentRuleListStore](wkcontentruleliststore.md)
  An object that contains the rules for how to load and filter content in the web view.
- [class WKContentWorld](wkcontentworld.md)
  An object that defines a scope of execution for JavaScript code, and which you use to prevent conflicts between different scripts.
- [class WKFrameInfo](wkframeinfo.md)
  An object that contains information about a frame on a webpage.
- [class WKSecurityOrigin](wksecurityorigin.md)
  An object that identifies the origin of a particular resource.
- [class WKUserScript](wkuserscript.md)
  A script that the web view injects into a webpage.
- [class WKContentWorldConfiguration](wkcontentworldconfiguration.md)
- [class WKJSHandle](wkjshandle.md)
  A WKJSHandle object contains a reference to a JavaScript object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkjsserializednode)*