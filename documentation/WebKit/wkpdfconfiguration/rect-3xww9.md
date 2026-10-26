# rect

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The portion of your web view to capture, specified as a rectangle in the view’s coordinate system.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic) CGRect rect;
```

#### Discussion

The default value of this property is [`CGRectNull`](../../CoreGraphics/cgrectnull.md), which captures everything in the view’s bounds rectangle. If you specify a custom rectangle, it must lie within the bounds rectangle of the [`WKWebView`](../wkwebview.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkpdfconfiguration/rect-3xww9)*