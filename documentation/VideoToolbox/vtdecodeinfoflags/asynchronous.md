# asynchronous

**Framework**: Video Toolbox  
**Kind**: property

A flag that indicates the decode operation ran asynchronously.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
static var asynchronous: VTDecodeInfoFlags { get }
```

## See Also

- [static var frameDropped: VTDecodeInfoFlags](vtdecodeinfoflags/framedropped.md)
  A flag that indicates the decode operation dropped a frame.
- [static var skippedLeadingFrameDropped: VTDecodeInfoFlags](vtdecodeinfoflags/skippedleadingframedropped.md)
  A flag that indicates whether the decode process skips leading frames after dropping a synchronization frame.
- [static var imageBufferModifiable: VTDecodeInfoFlags](vtdecodeinfoflags/imagebuffermodifiable.md)
  A flag that indicates the image buffer is safe to modify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtdecodeinfoflags/asynchronous)*