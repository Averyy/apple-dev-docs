# VTPixelRotationSessionCreate(_:_:)

**Framework**: Video Toolbox  
**Kind**: func  
**Role**: Function

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

```c
extern OSStatus VTPixelRotationSessionCreate(CFAllocatorRef allocator, VTPixelRotationSessionRef*pixelRotationSessionOut);
```

## Parameters

- `allocator`: An allocator for the session. Specify `NULL` to use the default allocator.
- `pixelRotationSessionOut`: On output, an initialized pixel rotation session.

## See Also

### Managing a Session
- [func VTPixelRotationSessionInvalidate(VTPixelRotationSession)](./vtpixelrotationsessioninvalidate%28_%29.md)
  Tears down a pixel rotation session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtpixelrotationsessioncreate(_:_:))*