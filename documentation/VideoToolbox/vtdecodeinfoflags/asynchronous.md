# asynchronous

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Type Property

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

```c
kVTDecodeInfo_Asynchronous
```

## See Also

### Flag values
- [static var frameDropped: VTDecodeInfoFlags](./framedropped.md)
  A flag that indicates the decode operation dropped a frame.
- [static var skippedLeadingFrameDropped: VTDecodeInfoFlags](./skippedleadingframedropped.md)
  A flag that indicates whether the decode process skips leading frames after dropping a synchronization frame.
- [static var imageBufferModifiable: VTDecodeInfoFlags](./imagebuffermodifiable.md)
  A flag that indicates the image buffer is safe to modify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtdecodeinfoflags/asynchronous)*