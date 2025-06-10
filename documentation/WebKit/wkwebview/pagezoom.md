# pageZoom

**Framework**: WebKit  
**Kind**: property

The scale factor by which the web view scales content relative to its bounds.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var pageZoom: CGFloat { get set }
```

#### Discussion

The default value of this property is `1.0`, which displays the content without any scaling. Changing the value of this property is equivalent to setting the CSS `zoom` property on all page content.

## See Also

- [var allowsMagnification: Bool](wkwebview/allowsmagnification.md)
  A Boolean value that indicates whether magnify gestures change the web view’s magnification.
- [var magnification: CGFloat](wkwebview/magnification.md)
  The factor by which the page content is currently scaled.
- [func setMagnification(CGFloat, centeredAt: CGPoint)](wkwebview/setmagnification(_:centeredat:).md)
  Scales the page content and centers the result on the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/pagezoom)*