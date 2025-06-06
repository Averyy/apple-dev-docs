# setMagnification(_:centeredAt:)

**Framework**: Webkit  
**Kind**: method

Scales the page content and centers the result on the specified point.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func setMagnification(_ magnification: CGFloat, centeredAt point: CGPoint)
```

## Parameters

- `magnification`: The factor by which to scale the content.
- `point`: The point (in the web view’s bounds) at which to center magnification.

## See Also

- [var pageZoom: CGFloat](wkwebview/pagezoom.md)
  The scale factor by which the web view scales content relative to its bounds.
- [var allowsMagnification: Bool](wkwebview/allowsmagnification.md)
  A Boolean value that indicates whether magnify gestures change the web view’s magnification.
- [var magnification: CGFloat](wkwebview/magnification.md)
  The factor by which the page content is currently scaled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/setmagnification(_:centeredat:))*