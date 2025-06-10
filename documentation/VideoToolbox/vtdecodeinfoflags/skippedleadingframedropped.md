# skippedLeadingFrameDropped

**Framework**: Video Toolbox  
**Kind**: property

A flag that indicates whether the decode process skips leading frames after dropping a synchronization frame.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
static var skippedLeadingFrameDropped: VTDecodeInfoFlags { get }
```

#### Discussion

This condition occurs when you performs a seek to a sync frame, and due to frame reordering, there are leading frames following the sync frame that the system can’t decode due to missing references. Dropping these frames has no impact on playback because the nondecodeable frames won’t render.

If the system sets this flag, it sets the [`frameDropped`](vtdecodeinfoflags/framedropped.md) flag as well.

## See Also

- [static var asynchronous: VTDecodeInfoFlags](vtdecodeinfoflags/asynchronous.md)
  A flag that indicates the decode operation ran asynchronously.
- [static var frameDropped: VTDecodeInfoFlags](vtdecodeinfoflags/framedropped.md)
  A flag that indicates the decode operation dropped a frame.
- [static var imageBufferModifiable: VTDecodeInfoFlags](vtdecodeinfoflags/imagebuffermodifiable.md)
  A flag that indicates the image buffer is safe to modify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtdecodeinfoflags/skippedleadingframedropped)*