# opticalFlow

**Framework**: Video Toolbox  
**Kind**: property

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

#### Discussion

You only need this if optical flow is pre-computed. For the first frame this is `nil`.

## See Also

- [var sourceFrame: VTFrameProcessorFrame](vtsuperresolutionscalerparameters/sourceframe.md)
  Current source frame, which must be non `nil`.
- [var previousFrame: VTFrameProcessorFrame?](vtsuperresolutionscalerparameters/previousframe.md)
  Previous source frame in presentation time order, which is `nil` for the first frame.
- [var previousOutputFrame: VTFrameProcessorFrame?](vtsuperresolutionscalerparameters/previousoutputframe.md)
  Previous output frame in presentation time order, which is `nil` for the first frame.
- [var submissionMode: VTSuperResolutionScalerParameters.SubmissionMode](vtsuperresolutionscalerparameters/submissionmode-swift.property.md)
  Ordering of the input frames in this submission relative to the previous submission.
- [VTSuperResolutionScalerParameters.SubmissionMode](vtsuperresolutionscalerparameters/submissionmode-swift.enum.md)
  Indicates the order of input frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsuperresolutionscalerparameters/opticalflow)*