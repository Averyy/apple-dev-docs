# sourceFrame

**Framework**: Video Toolbox  
**Kind**: property

Current source frame, which must be non `nil`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
var sourceFrame: VTFrameProcessorFrame { get }
```

## See Also

- [var previousFrame: VTFrameProcessorFrame?](vtsuperresolutionscalerparameters/previousframe.md)
  Previous source frame in presentation time order, which is `nil` for the first frame.
- [var previousOutputFrame: VTFrameProcessorFrame?](vtsuperresolutionscalerparameters/previousoutputframe.md)
  Previous output frame in presentation time order, which is `nil` for the first frame.
- [var opticalFlow: VTFrameProcessorOpticalFlow?](vtsuperresolutionscalerparameters/opticalflow.md)
  Optional object that contains forward and backward optical flow with the previous frame.
- [var submissionMode: VTSuperResolutionScalerParameters.SubmissionMode](vtsuperresolutionscalerparameters/submissionmode-swift.property.md)
  Ordering of the input frames in this submission relative to the previous submission.
- [VTSuperResolutionScalerParameters.SubmissionMode](vtsuperresolutionscalerparameters/submissionmode-swift.enum.md)
  Indicates the order of input frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsuperresolutionscalerparameters/sourceframe)*