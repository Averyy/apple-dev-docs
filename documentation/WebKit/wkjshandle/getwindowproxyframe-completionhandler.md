# getWindowProxyFrame(completionHandler:)

**Framework**: WebKit  
**Kind**: method

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var windowProxyFrame: WKFrameInfo? { get async }
```

#### Discussion

The frame represented by the JavaScript value.

If the `WKJSHandle` represents a JavaScript Window proxy object, the result of this method will be a snapshot of the frame represented by that Window object. Otherwise the result of this method will be `nil`


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkjshandle/getwindowproxyframe(completionhandler:))*