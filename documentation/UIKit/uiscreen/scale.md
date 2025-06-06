# scale

**Framework**: UIKit  
**Kind**: property

The natural scale factor associated with the screen.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
var scale: CGFloat { get }
```

#### Discussion

This value reflects the scale factor needed to convert from the default logical coordinate space into the device coordinate space of this screen. The default logical coordinate space is measured using points. For Retina displays, the scale factor may be `3.0` or `2.0` and one point can represented by nine or four pixels, respectively. For standard-resolution displays, the scale factor is `1.0` and one point equals one pixel.

## See Also

- [var bounds: CGRect](uiscreen/bounds.md)
  The bounding rectangle of the screen, measured in points.
- [var nativeBounds: CGRect](uiscreen/nativebounds.md)
  The bounding rectangle of the physical screen, measured in pixels.
- [var nativeScale: CGFloat](uiscreen/nativescale.md)
  The native scale factor for the physical screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/scale)*