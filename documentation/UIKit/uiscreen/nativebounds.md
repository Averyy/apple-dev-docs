# nativeBounds

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The bounding rectangle of the physical screen, measured in pixels.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS

## Declaration

```swift
var nativeBounds: CGRect { get }
```

```objc
@property (nonatomic, readonly) CGRect nativeBounds;
```

## Discussion

This rectangle is based on the device in a portrait-up orientation. This value does not change as the device rotates.

## See Also

### Getting the size and scale
- [var bounds: CGRect](./bounds.md)
  The bounding rectangle of the screen, measured in points.
- [var nativeScale: CGFloat](./nativescale.md)
  The native scale factor for the physical screen.
- [var scale: CGFloat](./scale.md)
  The natural scale factor associated with the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/nativebounds)*