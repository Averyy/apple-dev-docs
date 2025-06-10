# VTDecodeInfoFlags

**Framework**: Video Toolbox  
**Kind**: struct

Flags that provide information about the status of a decode operation.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
struct VTDecodeInfoFlags
```

## Topics

### Flag values
- [static var asynchronous: VTDecodeInfoFlags](vtdecodeinfoflags/asynchronous.md)
  A flag that indicates the decode operation ran asynchronously.
- [static var frameDropped: VTDecodeInfoFlags](vtdecodeinfoflags/framedropped.md)
  A flag that indicates the decode operation dropped a frame.
- [static var skippedLeadingFrameDropped: VTDecodeInfoFlags](vtdecodeinfoflags/skippedleadingframedropped.md)
  A flag that indicates whether the decode process skips leading frames after dropping a synchronization frame.
- [static var imageBufferModifiable: VTDecodeInfoFlags](vtdecodeinfoflags/imagebuffermodifiable.md)
  A flag that indicates the image buffer is safe to modify.
### Initializers
- [init(rawValue: UInt32)](vtdecodeinfoflags/init(rawvalue:).md)
  Creates a flag from a raw unsigned-integer value.
### Type Properties
- [static var frameInterrupted: VTDecodeInfoFlags](vtdecodeinfoflags/frameinterrupted.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [class VTDecompressionSession](vtdecompressionsession.md)
  A reference to a decompression session.
- [struct VTDecodeFrameFlags](vtdecodeframeflags.md)
  Flags to pass to a decompression session and the video decoder.
- [typealias VTDecompressionOutputCallback](vtdecompressionoutputcallback.md)
  The prototype for the callback invoked when frame decompression is complete.
- [struct VTDecompressionOutputCallbackRecord](vtdecompressionoutputcallbackrecord.md)
- [typealias VTDecompressionOutputHandler](vtdecompressionoutputhandler.md)
  The prototype for the block invoked when frame decompression is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtdecodeinfoflags)*