# nativeBounds

**Framework**: UIKit  
**Kind**: property

The bounding rectangle of the physical screen, measured in pixels.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
var nativeBounds: CGRect { get }
```

#### Discussion

This rectangle is based on the device in a portrait-up orientation. This value does not change as the device rotates.

## See Also

- [var bounds: CGRect](uiscreen/bounds.md)
  The bounding rectangle of the screen, measured in points.
- [var nativeScale: CGFloat](uiscreen/nativescale.md)
  The native scale factor for the physical screen.
- [var scale: CGFloat](uiscreen/scale.md)
  The natural scale factor associated with the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/nativebounds)*