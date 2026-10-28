# opticalFlow

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property

Optional object that contains forward and backward optical flow with the previous frame.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
var opticalFlow: VTFrameProcessorOpticalFlow? { get }
```

```objc
@property (nonatomic, readonly, nullable) VTFrameProcessorOpticalFlow * opticalFlow;
```

## Discussion

You only need this if optical flow is pre-computed. For the first frame this is `nil`.

## See Also

### Inspecting the parameters
- [var sourceFrame: VTFrameProcessorFrame](./sourceframe.md)
  Current source frame, which must be non `nil`.
- [var previousFrame: VTFrameProcessorFrame?](./previousframe.md)
  Previous source frame in presentation time order, which is `nil` for the first frame.
- [var previousOutputFrame: VTFrameProcessorFrame?](./previousoutputframe.md)
  Previous output frame in presentation time order, which is `nil` for the first frame.
- [var submissionMode: VTSuperResolutionScalerParameters.SubmissionMode](./submissionmode-swift.property.md)
  Ordering of the input frames in this submission relative to the previous submission.
- [VTSuperResolutionScalerParameters.SubmissionMode](./submissionmode-swift.enum.md)
  Indicates the order of input frames.
- [destinationFrame](./destinationframe.md)
  Destination frame that contains user-allocated pixel buffer that receives the results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsuperresolutionscalerparameters/opticalflow)*