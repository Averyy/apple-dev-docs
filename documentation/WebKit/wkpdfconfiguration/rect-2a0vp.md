# rect

**Framework**: WebKit  
**Kind**: property

The portion of your web view to capture, specified as a rectangle in the view’s coordinate system.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var rect: CGRect? { get set }
```

#### Discussion

The default value of this property is [`CGRectNull`](https://developer.apple.com/documentation/CoreGraphics/CGRectNull), which captures everything in the view’s bounds rectangle. If you specify a custom rectangle, it must lie within the bounds rectangle of the [`WKWebView`](wkwebview.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkpdfconfiguration/rect-2a0vp)*