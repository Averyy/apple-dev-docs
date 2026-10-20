# VTOpticalFlowParameters.SubmissionMode

**Framework**: Video Toolbox  
**Kind**: enum  
**Role**: Enumeration

A value describing the processing request in a parameters submission object.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+

## Declaration

```swift
enum SubmissionMode
```

```c
enum VTOpticalFlowParametersSubmissionMode : NSInteger;
```

## Topics

### Enumeration Cases
- [VTOpticalFlowParameters.SubmissionMode.random](./submissionmode-swift.enum/random.md)
  A submission follow presentation time order with a jump or skip in a frame sequence.
- [VTOpticalFlowParameters.SubmissionMode.sequential](./submissionmode-swift.enum/sequential.md)
  A submission follow presentation time order without a jump or skip when compared to a previous submission.
### Initializers
- [init?(rawValue: Int)](./submissionmode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting the parameters
- [var sourceFrame: VTFrameProcessorFrame](./sourceframe.md)
  The current source frame.
- [var nextFrame: VTFrameProcessorFrame](./nextframe.md)
  The next source frame in presentation time order.
- [var destinationOpticalFlow: VTFrameProcessorOpticalFlow](./destinationopticalflow.md)
  A user allocated mutable optical flow that will receive the results.
- [var submissionMode: VTOpticalFlowParameters.SubmissionMode](./submissionmode-swift.property.md)
  A value describing the processing request in a parameters submission object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtopticalflowparameters/submissionmode-swift.enum)*