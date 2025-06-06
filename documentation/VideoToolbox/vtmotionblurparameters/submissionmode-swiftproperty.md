# submissionMode

**Framework**: Videotoolbox  
**Kind**: property

A value describing the processing request in a parameters submission object.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var submissionMode: VTMotionBlurParameters.SubmissionMode { get }
```

#### Discussion

Set to VTMotionBlurParametersSubmissionModeSequential to indicate that the current submission follows the presentation time order without jumping or skipping when compared to the previous submission. Using the submission mode sequential will yield better performance. Set to VTMotionBlurParametersSubmissionModeRandom to indicate a skip or a jump in frame sequence. If submission mode random is set, the internal cache will be cleared during the processWithParameters call.

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
- [VTMotionBlurParameters.SubmissionMode](vtmotionblurparameters/submissionmode-swift.enum.md)
  A value describing the processing request in a parameters submission object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmotionblurparameters/submissionmode-swift.property)*