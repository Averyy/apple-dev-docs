# submissionMode

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property

A value describing the processing request in a parameters submission object.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+

## Declaration

```swift
var submissionMode: VTMotionBlurParameters.SubmissionMode { get }
```

```objc
@property (nonatomic, readonly) VTMotionBlurParametersSubmissionMode submissionMode;
```

#### Discussion

Set to VTMotionBlurParametersSubmissionModeSequential to indicate that the current submission follows the presentation time order without jumping or skipping when compared to the previous submission. Using the submission mode sequential will yield better performance. Set to VTMotionBlurParametersSubmissionModeRandom to indicate a skip or a jump in frame sequence. If submission mode random is set, the internal cache will be cleared during the processWithParameters call.

## See Also

### Inspecting the parameters
- [var sourceFrame: VTFrameProcessorFrame](./sourceframe.md)
  The current source frame.
- [var nextFrame: VTFrameProcessorFrame?](./nextframe.md)
  The next source frame in presentation time order.
- [var previousFrame: VTFrameProcessorFrame?](./previousframe.md)
  The previous source frame in presentation time order.
- [var motionBlurStrength: Int](./motionblurstrength.md)
  A value that indicates the strength of blur to apply.
- [var nextOpticalFlow: VTFrameProcessorOpticalFlow?](./nextopticalflow.md)
  Optional optical flow object that contains forward and backward optical flow with the next frame.
- [var previousOpticalFlow: VTFrameProcessorOpticalFlow?](./previousopticalflow.md)
  Optional optical flow object that contains forward and backward optical flow with the previous frame.
- [VTMotionBlurParameters.SubmissionMode](./submissionmode-swift.enum.md)
  A value describing the processing request in a parameters submission object.
- [destinationFrame](./destinationframe.md)
  A user-allocated pixel buffer that receives the results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmotionblurparameters/submissionmode-swift.property)*