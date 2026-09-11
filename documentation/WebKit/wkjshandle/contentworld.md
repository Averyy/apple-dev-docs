# contentWorld

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
weak var contentWorld: WKContentWorld? { get }
```

#### Discussion

The world in which the `WKJSHandle` can be used.

If the `WKJSHandle` is used in another world it will be interpreted as the JavaScript value `undefined`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkjshandle/contentworld)*