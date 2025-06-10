# allowsMagnification

**Framework**: WebKit  
**Kind**: property

A Boolean value that indicates whether magnify gestures change the web view’s magnification.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var allowsMagnification: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/swift/false). You can set the `magnification` property even if `allowsMagnification` is set to [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var pageZoom: CGFloat](wkwebview/pagezoom.md)
  The scale factor by which the web view scales content relative to its bounds.
- [var magnification: CGFloat](wkwebview/magnification.md)
  The factor by which the page content is currently scaled.
- [func setMagnification(CGFloat, centeredAt: CGPoint)](wkwebview/setmagnification(_:centeredat:).md)
  Scales the page content and centers the result on the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/allowsmagnification)*