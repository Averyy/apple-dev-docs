# VTOpticalFlowParameters.SubmissionMode

**Framework**: Videotoolbox  
**Kind**: enum

A value describing the processing request in a parameters submission object.

**Availability**:
- macOS 15.4+

## Declaration

```swift
enum SubmissionMode
```

## Topics

### Enumeration Cases
- [VTOpticalFlowParameters.SubmissionMode.random](vtopticalflowparameters/submissionmode-swift.enum/random.md)
  A submission follow presentation time order with a jump or skip in a frame sequence.
- [VTOpticalFlowParameters.SubmissionMode.sequential](vtopticalflowparameters/submissionmode-swift.enum/sequential.md)
  A submission follow presentation time order without a jump or skip when compared to a previous submission.
### Initializers
- [init?(rawValue: Int)](vtopticalflowparameters/submissionmode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var sourceFrame: VTFrameProcessorFrame](vtopticalflowparameters/sourceframe.md)
  The current source frame.
- [var nextFrame: VTFrameProcessorFrame](vtopticalflowparameters/nextframe.md)
  The next source frame in presentation time order.
- [var destinationOpticalFlow: VTFrameProcessorOpticalFlow](vtopticalflowparameters/destinationopticalflow.md)
  A user allocated mutable optical flow that will receive the results.
- [var submissionMode: VTOpticalFlowParameters.SubmissionMode](vtopticalflowparameters/submissionmode-swift.property.md)
  A value describing the processing request in a parameters submission object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtopticalflowparameters/submissionmode-swift.enum)*