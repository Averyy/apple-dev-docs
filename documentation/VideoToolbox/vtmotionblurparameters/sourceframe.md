# sourceFrame

**Framework**: Video Toolbox  
**Kind**: property

The current source frame.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+

## Declaration

```swift
var sourceFrame: VTFrameProcessorFrame { get }
```

#### Discussion

This value must be non nil.

## See Also

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
- [VTMotionBlurParameters.SubmissionMode](vtmotionblurparameters/submissionmode-swift.enum.md)
  A value describing the processing request in a parameters submission object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmotionblurparameters/sourceframe)*