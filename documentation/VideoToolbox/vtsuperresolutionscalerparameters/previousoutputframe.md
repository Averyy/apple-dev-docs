# previousOutputFrame

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property

Previous output frame in presentation time order, which is `nil` for the first frame.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
var previousOutputFrame: VTFrameProcessorFrame? { get }
```

```objc
@property (nonatomic, readonly, nullable) VTFrameProcessorFrame * previousOutputFrame;
```

## See Also

### Inspecting the parameters
- [var sourceFrame: VTFrameProcessorFrame](./sourceframe.md)
  Current source frame, which must be non `nil`.
- [var previousFrame: VTFrameProcessorFrame?](./previousframe.md)
  Previous source frame in presentation time order, which is `nil` for the first frame.
- [var opticalFlow: VTFrameProcessorOpticalFlow?](./opticalflow.md)
  Optional object that contains forward and backward optical flow with the previous frame.
- [var submissionMode: VTSuperResolutionScalerParameters.SubmissionMode](./submissionmode-swift.property.md)
  Ordering of the input frames in this submission relative to the previous submission.
- [VTSuperResolutionScalerParameters.SubmissionMode](./submissionmode-swift.enum.md)
  Indicates the order of input frames.
- [destinationFrame](./destinationframe.md)
  Destination frame that contains user-allocated pixel buffer that receives the results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsuperresolutionscalerparameters/previousoutputframe)*