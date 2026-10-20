# magnification

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The factor by which the page content is currently scaled.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var magnification: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat magnification;
```

#### Discussion

The default value is `1.0`.

## See Also

### Scaling content
- [var pageZoom: CGFloat](./pagezoom.md)
  The scale factor by which the web view scales content relative to its bounds.
- [var allowsMagnification: Bool](./allowsmagnification.md)
  A Boolean value that indicates whether magnify gestures change the web view’s magnification.
- [func setMagnification(CGFloat, centeredAt: CGPoint)](./setmagnification%28_,centeredat%29.md)
  Scales the page content and centers the result on the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/magnification)*