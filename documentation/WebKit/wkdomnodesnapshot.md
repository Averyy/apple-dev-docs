# WKDOMNodeSnapshot

**Framework**: WebKit  
**Kind**: class

A `WKDOMNodeSnapshot` object contains a snapshot of a DOM node

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class WKDOMNodeSnapshot
```

#### Overview

There are various ways that JavaScript executing inside web content results in some return value being passed up to the WebKit application. Examples include calls to `[WKWebView evaluateJavaScript:...]`, `[WKWebView callAsyncJavaScript:...]`, and the body of a `WKScriptMessage`.

When application JavaScript returns a JavaScript value, the default behavior is to try to convert it to a foundational type. e.g. a JavaScript Number becomes an NSNumber, or a JavaScript array becomes an NSArray, etc.

If the JavaScript calls `window.webkit.createNodeSnapshot(...)` then WebKit will create a snapshot representation of that node as the return value.

The node is an opaque object as far as the application is concerned, but it can be used as an argument to future JavaScript programs via `[WKWebView callAsyncJavaScript:...]`

Unlike `WKJSHandle` - which keeps an actual JavaScript object alive in its originating context - a `WKDOMNodeSnapshot` is not attached to a live JavaScript object, and it can be used as an argument to a JavaScript program running in any context. e.g. In a different frame, or after a navigation.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkdomnodesnapshot)*