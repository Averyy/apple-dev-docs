# submissionMode

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property

A value describing the processing request in a parameters submission object.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+

## Declaration

```swift
var submissionMode: VTOpticalFlowParameters.SubmissionMode { get }
```

```objc
@property (nonatomic, readonly) VTOpticalFlowParametersSubmissionMode submissionMode;
```

## See Also

### Inspecting the parameters
- [var sourceFrame: VTFrameProcessorFrame](./sourceframe.md)
  The current source frame.
- [var nextFrame: VTFrameProcessorFrame](./nextframe.md)
  The next source frame in presentation time order.
- [var destinationOpticalFlow: VTFrameProcessorOpticalFlow](./destinationopticalflow.md)
  A user allocated mutable optical flow that will receive the results.
- [VTOpticalFlowParameters.SubmissionMode](./submissionmode-swift.enum.md)
  A value describing the processing request in a parameters submission object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtopticalflowparameters/submissionmode-swift.property)*