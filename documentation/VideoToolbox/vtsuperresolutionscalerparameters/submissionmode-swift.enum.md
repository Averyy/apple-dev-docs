# VTSuperResolutionScalerParameters.SubmissionMode

**Framework**: Video Toolbox  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum VTSuperResolutionScalerParametersSubmissionMode : NSInteger;
```

## Overview

When submitting [`VTSuperResolutionScalerParameters`](../vtsuperresolutionscalerparameters.md) to the processor, you need to provide one of these values based on how the input frames are related to each other.

Use [`VTSuperResolutionScalerParameters.SubmissionMode.sequential`](./submissionmode-swift.enum/sequential.md) to indicate that the current submission follows presentation time order without jumps or skips, when compared to previous submissions. This value provides better processor performance than other values.

Use [`VTSuperResolutionScalerParameters.SubmissionMode.random`](./submissionmode-swift.enum/random.md) to indicate that the current submission has no relation to the previous submission. Typically, this indicates a jump or skip in the frame sequence. The processor clears internal caches when it receives this value in `VTFrameProcessor/processWithParameters` function call.

## Topics

### Enumeration Cases
- [VTSuperResolutionScalerParameters.SubmissionMode.random](./submissionmode-swift.enum/random.md)
- [VTSuperResolutionScalerParameters.SubmissionMode.sequential](./submissionmode-swift.enum/sequential.md)
### Initializers
- [init?(rawValue: Int)](./submissionmode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting the parameters
- [var sourceFrame: VTFrameProcessorFrame](./sourceframe.md)
  Current source frame, which must be non `nil`.
- [var previousFrame: VTFrameProcessorFrame?](./previousframe.md)
  Previous source frame in presentation time order, which is `nil` for the first frame.
- [var previousOutputFrame: VTFrameProcessorFrame?](./previousoutputframe.md)
  Previous output frame in presentation time order, which is `nil` for the first frame.
- [var opticalFlow: VTFrameProcessorOpticalFlow?](./opticalflow.md)
  Optional object that contains forward and backward optical flow with the previous frame.
- [var submissionMode: VTSuperResolutionScalerParameters.SubmissionMode](./submissionmode-swift.property.md)
  Ordering of the input frames in this submission relative to the previous submission.
- [destinationFrame](./destinationframe.md)
  Destination frame that contains user-allocated pixel buffer that receives the results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsuperresolutionscalerparameters/submissionmode-swift.enum)*