# nextFrame

**Framework**: Video Toolbox  
**Kind**: property

The next source frame in presentation time order.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 15.4+

## Declaration

```swift
var nextFrame: VTFrameProcessorFrame { get }
```

#### Discussion

This value can be set to nil for the last frame.

## See Also

- [var sourceFrame: VTFrameProcessorFrame](vtopticalflowparameters/sourceframe.md)
  The current source frame.
- [var destinationOpticalFlow: VTFrameProcessorOpticalFlow](vtopticalflowparameters/destinationopticalflow.md)
  A user allocated mutable optical flow that will receive the results.
- [var submissionMode: VTOpticalFlowParameters.SubmissionMode](vtopticalflowparameters/submissionmode-swift.property.md)
  A value describing the processing request in a parameters submission object.
- [VTOpticalFlowParameters.SubmissionMode](vtopticalflowparameters/submissionmode-swift.enum.md)
  A value describing the processing request in a parameters submission object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtopticalflowparameters/nextframe)*