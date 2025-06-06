# VTPixelRotationSessionInvalidate(_:)

**Framework**: Videotoolbox  
**Kind**: func

Tears down a pixel rotation session.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func VTPixelRotationSessionInvalidate(_ session: VTPixelRotationSession)
```

#### Discussion

When a pixel rotation session’s retain count reaches zero, the system automatically invalidates it. However, because other processes may retain a session, it can be hard to predict when the invalidation occurs. Calling this function ensures a deterministic, orderly teardown.

## Parameters

- `session`: The pixel rotation session to invalidate.

## See Also

- [func VTPixelRotationSessionCreate(CFAllocator?, UnsafeMutablePointer<VTPixelRotationSession?>) -> OSStatus](vtpixelrotationsessioncreate(_:_:).md)
  Creates a session to rotate images between pixel buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtpixelrotationsessioninvalidate(_:))*