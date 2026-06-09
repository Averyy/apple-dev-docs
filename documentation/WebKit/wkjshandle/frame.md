# frame

**Framework**: WebKit  
**Kind**: property

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@NSCopying
var frame: WKFrameInfo { get }
```

#### Discussion

The frame in which the `WKJSHandle` can be used.

If the `WKJSHandle` is used as an argument to JavaScript in another frame or after the indicated frame has navigated, it will be interpreted as the JavaScript value `undefined`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkjshandle/frame)*