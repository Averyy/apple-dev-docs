# sourceFrame

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) VTFrameProcessorFrame * sourceFrame;
```

#### Discussion

This value must be non nil.

## See Also

### Inspecting the parameters
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
- [var submissionMode: VTMotionBlurParameters.SubmissionMode](./submissionmode-swift.property.md)
  A value describing the processing request in a parameters submission object.
- [VTMotionBlurParameters.SubmissionMode](./submissionmode-swift.enum.md)
  A value describing the processing request in a parameters submission object.
- [destinationFrame](./destinationframe.md)
  A user-allocated pixel buffer that receives the results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmotionblurparameters/sourceframe)*