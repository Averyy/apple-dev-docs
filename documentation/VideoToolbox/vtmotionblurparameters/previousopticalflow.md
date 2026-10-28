# previousOpticalFlow

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property

Optional optical flow object that contains forward and backward optical flow with the previous frame.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+

## Declaration

```swift
var previousOpticalFlow: VTFrameProcessorOpticalFlow? { get }
```

```objc
@property (nonatomic, readonly, nullable) VTFrameProcessorOpticalFlow * previousOpticalFlow;
```

## Discussion

For the first frame this will always be nil. This object is only needed if optical flow is pre-computed.

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
- [var submissionMode: VTMotionBlurParameters.SubmissionMode](./submissionmode-swift.property.md)
  A value describing the processing request in a parameters submission object.
- [VTMotionBlurParameters.SubmissionMode](./submissionmode-swift.enum.md)
  A value describing the processing request in a parameters submission object.
- [destinationFrame](./destinationframe.md)
  A user-allocated pixel buffer that receives the results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmotionblurparameters/previousopticalflow)*