# WKJSHandle

**Framework**: WebKit  
**Kind**: class

A WKJSHandle object contains a reference to a JavaScript object.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class WKJSHandle
```

#### Overview

There are various ways that JavaScript executing inside web content results in some return value being passed up to the WebKit application. Examples include calls to `[WKWebView evaluateJavaScript:...]`, `[WKWebView callAsyncJavaScript:...]`, and the body of a `WKScriptMessage`.

Usually these result objects are a foundational type, such as a number, string, array, dictionary, etc. In some environments the result object can be a `WKJSHandle` or be a container that contains one or more `WKJSHandle` objects. These environments are:

- The JavaScript in question executed in a `WKContentWorld` that has `allowJSHandleCreation` set to `YES`
- The most recent navigation in the `WKWebView` had `WKWebpagePreferences.allowsJSHandleCreationInPageWorld` set to `YES`

JavaScript running in those environments can make a `WKJSHandle` instead of following normal serialization rules by calling `window.webkit.createJSHandle(...)` with the target value as an argument.

Whatever JavaScript object the `WKJSHandle` represents, it will be protected from garbage collection for the lifetime of the `WKJSHandle` The `WKJSHandle` can also be used as an argument to future JavaScript run via `[WKWebView callAsyncJavaScript:...]`

## Topics

### Instance Properties
- [var frame: WKFrameInfo](wkjshandle/frame.md)
- [var world: WKContentWorld?](wkjshandle/world.md)
### Instance Methods
- [func windowProxyFrameInfo((WKFrameInfo?) -> Void)](wkjshandle/windowproxyframeinfo(_:).md)

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
- [class WKJSScriptingBuffer](wkjsscriptingbuffer.md)
  A WKJSScriptingBuffer object exposes an application controlled data buffer to JavaScript.
- [class WKJSSerializedNode](wkjsserializednode.md)
  A `WKJSSerializedNode` object contains the serialized representation of a DOM node


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkjshandle)*