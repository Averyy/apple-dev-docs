# world

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
weak var world: WKContentWorld? { get }
```

#### Discussion

The world in which the `WKJSHandle` can be used.

If the `WKJSHandle` is used in another world it will be interpreted as the JavaScript value `undefined`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkjshandle/world)*