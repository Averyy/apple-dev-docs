# bounds

**Framework**: UIKit  
**Kind**: property

The bounding rectangle of the screen, measured in points.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
var bounds: CGRect { get }
```

#### Discussion

This rectangle is specified in the current coordinate space, which takes into account any interface rotations in effect for the device. Therefore, the value of this property may change when the device rotates between portrait and landscape orientations.

## See Also

- [var nativeBounds: CGRect](uiscreen/nativebounds.md)
  The bounding rectangle of the physical screen, measured in pixels.
- [var nativeScale: CGFloat](uiscreen/nativescale.md)
  The native scale factor for the physical screen.
- [var scale: CGFloat](uiscreen/scale.md)
  The natural scale factor associated with the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/bounds)*