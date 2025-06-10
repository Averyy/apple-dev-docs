# VTPixelRotationSessionCreate(_:_:)

**Framework**: Video Toolbox  
**Kind**: func

Creates a session to rotate images between pixel buffers.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func VTPixelRotationSessionCreate(_ allocator: CFAllocator?, _ pixelRotationSessionOut: UnsafeMutablePointer<VTPixelRotationSession?>) -> OSStatus
```

## Parameters

- `allocator`: An allocator for the session. Specify   to use the default allocator.
- `pixelRotationSessionOut`: On output, an initialized pixel rotation session.

## See Also

- [func VTPixelRotationSessionInvalidate(VTPixelRotationSession)](vtpixelrotationsessioninvalidate(_:).md)
  Tears down a pixel rotation session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtpixelrotationsessioncreate(_:_:))*