# previousFrame

**Framework**: Video Toolbox  
**Kind**: property

Previous source frame in presentation time order, which is `nil` for the first frame.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
var previousFrame: VTFrameProcessorFrame? { get }
```

## See Also

- [var sourceFrame: VTFrameProcessorFrame](vtsuperresolutionscalerparameters/sourceframe.md)
  Current source frame, which must be non `nil`.
- [var previousOutputFrame: VTFrameProcessorFrame?](vtsuperresolutionscalerparameters/previousoutputframe.md)
  Previous output frame in presentation time order, which is `nil` for the first frame.
- [var opticalFlow: VTFrameProcessorOpticalFlow?](vtsuperresolutionscalerparameters/opticalflow.md)
  Optional object that contains forward and backward optical flow with the previous frame.
- [var submissionMode: VTSuperResolutionScalerParameters.SubmissionMode](vtsuperresolutionscalerparameters/submissionmode-swift.property.md)
  Ordering of the input frames in this submission relative to the previous submission.
- [VTSuperResolutionScalerParameters.SubmissionMode](vtsuperresolutionscalerparameters/submissionmode-swift.enum.md)
  Indicates the order of input frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsuperresolutionscalerparameters/previousframe)*