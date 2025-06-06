# sourceFrame

**Framework**: Videotoolbox  
**Kind**: property

The current source frame.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var sourceFrame: VTFrameProcessorFrame { get }
```

#### Discussion

This must be a non-nil value.

## See Also

- [var nextFrame: VTFrameProcessorFrame](vtopticalflowparameters/nextframe.md)
  The next source frame in presentation time order.
- [var destinationOpticalFlow: VTFrameProcessorOpticalFlow](vtopticalflowparameters/destinationopticalflow.md)
  A user allocated mutable optical flow that will receive the results.
- [var submissionMode: VTOpticalFlowParameters.SubmissionMode](vtopticalflowparameters/submissionmode-swift.property.md)
  A value describing the processing request in a parameters submission object.
- [VTOpticalFlowParameters.SubmissionMode](vtopticalflowparameters/submissionmode-swift.enum.md)
  A value describing the processing request in a parameters submission object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtopticalflowparameters/sourceframe)*