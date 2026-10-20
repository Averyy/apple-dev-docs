# VTFrameRateConversionParameters.SubmissionMode

**Framework**: Video Toolbox  
**Kind**: enum  
**Role**: Enumeration

A value describing the processing request in a parameters submission object.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+

## Declaration

```swift
enum SubmissionMode
```

```c
enum VTFrameRateConversionParametersSubmissionMode : NSInteger;
```

#### Overview

Set to VTFrameRateConversionParametersSubmissionModeSequential to indicate that the current submission follows the presentation time order without jumping or skipping when compared to the previous submission. Using the submission mode sequential will yield better performance. Set to VTFrameRateConversionParametersSubmissionModeRandom to indicate a skip or a jump in frame sequence. If the submission mode random is set, the internal cache will be cleared during the processWithParameters call.

## Topics

### Submission modes
- [VTFrameRateConversionParameters.SubmissionMode.random](./submissionmode-swift.enum/random.md)
  A submission follow presentation time order with a jump or skip in a frame sequence.
- [VTFrameRateConversionParameters.SubmissionMode.sequential](./submissionmode-swift.enum/sequential.md)
  A submission follow presentation time order without a jump or skip when compared to a previous submission.
### Initializers
- [init?(rawValue: Int)](./submissionmode-swift.enum/init%28rawvalue%29.md)
### Enumeration Cases
- [VTFrameRateConversionParameters.SubmissionMode.sequentialReferencesUnchanged](./submissionmode-swift.enum/sequentialreferencesunchanged.md)
  You are submitting frames sequentially.

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
  The current source frame.
- [var nextFrame: VTFrameProcessorFrame?](./nextframe.md)
  The next source frame in presentation time order.
- [var opticalFlow: VTFrameProcessorOpticalFlow?](./opticalflow.md)
  A property that defines the optical flow for an object.
- [var interpolationPhase: [Float]](./interpolationphase-2jky5.md)
  An array of floating-point values that indicate which intervals to insert a frame between the current and next frame.
- [var submissionMode: VTFrameRateConversionParameters.SubmissionMode](./submissionmode-swift.property.md)
  A value describing the processing request in a parameters submission object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframerateconversionparameters/submissionmode-swift.enum)*