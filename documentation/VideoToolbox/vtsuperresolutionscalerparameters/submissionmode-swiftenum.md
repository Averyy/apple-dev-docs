# VTSuperResolutionScalerParameters.SubmissionMode

**Framework**: Video Toolbox  
**Kind**: enum

Indicates the order of input frames.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
enum SubmissionMode
```

#### Overview

When submitting [`VTSuperResolutionScalerParameters`](vtsuperresolutionscalerparameters.md) to the processor, you need to provide one of these values based on how the input frames are related to each other.

Use [`VTSuperResolutionScalerParameters.SubmissionMode.sequential`](vtsuperresolutionscalerparameters/submissionmode-swift.enum/sequential.md) to indicate that the current submission follows presentation time order without jumps or skips, when compared to previous submissions. This value provides better processor performance than other values.

Use [`VTSuperResolutionScalerParameters.SubmissionMode.random`](vtsuperresolutionscalerparameters/submissionmode-swift.enum/random.md) to indicate that the current submission has no relation to the previous submission. Typically, this indicates a jump or skip in the frame sequence. The processor clears internal caches when it receives this value in `VTFrameProcessor/processWithParameters` function call.

## Topics

### Enumeration Cases
- [VTSuperResolutionScalerParameters.SubmissionMode.random](vtsuperresolutionscalerparameters/submissionmode-swift.enum/random.md)
- [VTSuperResolutionScalerParameters.SubmissionMode.sequential](vtsuperresolutionscalerparameters/submissionmode-swift.enum/sequential.md)
### Initializers
- [init?(rawValue: Int)](vtsuperresolutionscalerparameters/submissionmode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsuperresolutionscalerparameters/submissionmode-swift.enum)*