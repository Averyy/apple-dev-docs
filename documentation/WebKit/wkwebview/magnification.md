# magnification

**Framework**: Webkit  
**Kind**: property

The factor by which the page content is currently scaled.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var magnification: CGFloat { get set }
```

#### Discussion

The default value is `1.0`.

## See Also

- [var pageZoom: CGFloat](wkwebview/pagezoom.md)
  The scale factor by which the web view scales content relative to its bounds.
- [var allowsMagnification: Bool](wkwebview/allowsmagnification.md)
  A Boolean value that indicates whether magnify gestures change the web view’s magnification.
- [func setMagnification(CGFloat, centeredAt: CGPoint)](wkwebview/setmagnification(_:centeredat:).md)
  Scales the page content and centers the result on the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/magnification)*