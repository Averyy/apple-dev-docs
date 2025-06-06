# rect

**Framework**: Webkit  
**Kind**: property

The portion of your web view to capture, specified as a rectangle in the view’s coordinate system.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var rect: CGRect { get set }
```

#### Discussion

The default value of this property is [`CGRectNull`](https://developer.apple.com/documentation/CoreGraphics/CGRectNull), which captures everything in the view’s bounds rectangle. If you specify a custom rectangle, it must lie within the bounds rectangle of the [`WKWebView`](wkwebview.md) object.

## See Also

- [var snapshotWidth: NSNumber?](wksnapshotconfiguration/snapshotwidth.md)
  The width of the captured image, in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wksnapshotconfiguration/rect)*