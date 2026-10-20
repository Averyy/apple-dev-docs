# VTDecodeFrameFlags

**Framework**: Video Toolbox  
**Kind**: struct  
**Role**: Structure

Flags to pass to a decompression session and the video decoder.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
struct VTDecodeFrameFlags
```

```c
enum VTDecodeFrameFlags : uint32_t;
```

## Topics

### Flags
- [init(rawValue: UInt32)](./vtdecodeframeflags/init%28rawvalue%29.md)
  Creates a flags structure with a raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Data Types
- [class VTDecompressionSession](./vtdecompressionsession.md)
  A reference to a decompression session.
- [struct VTDecodeInfoFlags](./vtdecodeinfoflags.md)
  Flags that provide information about the status of a decode operation.
- [typealias VTDecompressionOutputCallback](./vtdecompressionoutputcallback.md)
  The prototype for the callback invoked when frame decompression is complete.
- [struct VTDecompressionOutputCallbackRecord](./vtdecompressionoutputcallbackrecord.md)
- [typealias VTDecompressionOutputHandler](./vtdecompressionoutputhandler.md)
  The prototype for the block invoked when frame decompression is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtdecodeframeflags)*