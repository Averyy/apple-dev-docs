# sourceFrame

**Framework**: WebKit  
**Kind**: property

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@NSCopying
var sourceFrame: WKFrameInfo { get }
```

#### Discussion

The frame from which the `WKJSHandle` originates and where it can be used.

If the `WKJSHandle` is used as an argument to JavaScript in another frame or after the indicated frame has navigated, it will be interpreted as the JavaScript value `undefined`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkjshandle/sourceframe)*