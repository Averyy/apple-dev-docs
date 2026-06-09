# WKJSScriptingBuffer

**Framework**: WebKit  
**Kind**: class

A WKJSScriptingBuffer object exposes an application controlled data buffer to JavaScript.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class WKJSScriptingBuffer
```

#### Overview

JavaScript has access to various WebKit extensions via the `window.webkit` object. One such feature is `window.webkit.buffers` which provides access to named data buffers that can be provided by the WebKit application.

To provide a data buffer to JavaScript the application first creates a `WKJSScriptingBuffer` object. It then adds it to the appropriate `WKUserContentController` with an application provided name.

For example, if the application creates a `WKJSScriptingBuffer` and adds it to a web view’s `WKUserContentController` with the name `"mybuffer"`, then JavaScript can access it by referencing `window.webkit.buffers.mybuffer`

## Topics

### Initializers
- [init?(data: Data)](wkjsscriptingbuffer/init(data:).md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkjsscriptingbuffer)*