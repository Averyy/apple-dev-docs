# VTMotionBlurParameters.SubmissionMode

**Framework**: Videotoolbox  
**Kind**: enum

A value describing the processing request in a parameters submission object.

**Availability**:
- macOS 15.4+

## Declaration

```swift
enum SubmissionMode
```

#### Overview

Set to VTMotionBlurParametersSubmissionModeSequential to indicate that the current submission follows the presentation time order without jumping or skipping when compared to the previous submission. Using the submission mode sequential will yield better performance. Set to VTMotionBlurParametersSubmissionModeRandom to indicate a skip or a jump in frame sequence. If the submission mode random is set, the internal cache will be cleared during the processWithParameters call.

## Topics

### Submission modes
- [VTMotionBlurParameters.SubmissionMode.random](vtmotionblurparameters/submissionmode-swift.enum/random.md)
  A submission follow presentation time order with a jump or skip in a frame sequence.
- [VTMotionBlurParameters.SubmissionMode.sequential](vtmotionblurparameters/submissionmode-swift.enum/sequential.md)
  A submission follow presentation time order without a jump or skip when compared to a previous submission.
### Initializers
- [init?(rawValue: Int)](vtmotionblurparameters/submissionmode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var sourceFrame: VTFrameProcessorFrame](vtmotionblurparameters/sourceframe.md)
  The current source frame.
- [var destinationFrame: VTFrameProcessorFrame](vtmotionblurparameters/destinationframe.md)
  A user-allocated pixel buffer that receives the results.
- [var nextFrame: VTFrameProcessorFrame?](vtmotionblurparameters/nextframe.md)
  The next source frame in presentation time order.
- [var previousFrame: VTFrameProcessorFrame?](vtmotionblurparameters/previousframe.md)
  The previous source frame in presentation time order.
- [var motionBlurStrength: Int](vtmotionblurparameters/motionblurstrength.md)
  A value that indicates the strength of blur to apply.
- [var nextOpticalFlow: VTFrameProcessorOpticalFlow?](vtmotionblurparameters/nextopticalflow.md)
  Optional optical flow object that contains forward and backward optical flow with the next frame.
- [var previousOpticalFlow: VTFrameProcessorOpticalFlow?](vtmotionblurparameters/previousopticalflow.md)
  Optional optical flow object that contains forward and backward optical flow with the previous frame.
- [var submissionMode: VTMotionBlurParameters.SubmissionMode](vtmotionblurparameters/submissionmode-swift.property.md)
  A value describing the processing request in a parameters submission object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmotionblurparameters/submissionmode-swift.enum)*