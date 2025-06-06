# previousOpticalFlow

**Framework**: Videotoolbox  
**Kind**: property

Optional optical flow object that contains forward and backward optical flow with the previous frame.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var previousOpticalFlow: VTFrameProcessorOpticalFlow? { get }
```

#### Discussion

For the first frame this will always be nil. This object is only needed if optical flow is pre-computed.

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
- [var submissionMode: VTMotionBlurParameters.SubmissionMode](vtmotionblurparameters/submissionmode-swift.property.md)
  A value describing the processing request in a parameters submission object.
- [VTMotionBlurParameters.SubmissionMode](vtmotionblurparameters/submissionmode-swift.enum.md)
  A value describing the processing request in a parameters submission object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmotionblurparameters/previousopticalflow)*