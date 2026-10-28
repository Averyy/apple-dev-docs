# rect

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The portion of your web view to capture, specified as a rectangle in the view’s coordinate system.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
var rect: CGRect { get set }
```

```objc
@property (nonatomic) CGRect rect;
```

## Discussion

The default value of this property is [`CGRectNull`](../../CoreGraphics/cgrectnull.md), which captures everything in the view’s bounds rectangle. If you specify a custom rectangle, it must lie within the bounds rectangle of the [`WKWebView`](../wkwebview.md) object.

## See Also

### Specifying the snapshot dimensions
- [var snapshotWidth: NSNumber?](./snapshotwidth.md)
  The width of the captured image, in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wksnapshotconfiguration/rect)*