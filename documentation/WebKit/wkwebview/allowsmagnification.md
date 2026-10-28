# allowsMagnification

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether magnify gestures change the web view’s magnification.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var allowsMagnification: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsMagnification;
```

## Discussion

The default value is [`false`](../../Swift/false.md). You can set the `magnification` property even if `allowsMagnification` is set to [`false`](../../Swift/false.md).

## See Also

### Scaling content
- [var pageZoom: CGFloat](./pagezoom.md)
  The scale factor by which the web view scales content relative to its bounds.
- [var magnification: CGFloat](./magnification.md)
  The factor by which the page content is currently scaled.
- [func setMagnification(CGFloat, centeredAt: CGPoint)](./setmagnification%28_,centeredat%29.md)
  Scales the page content and centers the result on the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/allowsmagnification)*