# sourceFrame

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property

The current source frame.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+

## Declaration

```swift
var sourceFrame: VTFrameProcessorFrame { get }
```

```objc
@property (nonatomic, readonly) VTFrameProcessorFrame * sourceFrame;
```

## Discussion

This must be a non-nil value.

## See Also

### Inspecting the parameters
- [var nextFrame: VTFrameProcessorFrame](./nextframe.md)
  The next source frame in presentation time order.
- [var destinationOpticalFlow: VTFrameProcessorOpticalFlow](./destinationopticalflow.md)
  A user allocated mutable optical flow that will receive the results.
- [var submissionMode: VTOpticalFlowParameters.SubmissionMode](./submissionmode-swift.property.md)
  A value describing the processing request in a parameters submission object.
- [VTOpticalFlowParameters.SubmissionMode](./submissionmode-swift.enum.md)
  A value describing the processing request in a parameters submission object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtopticalflowparameters/sourceframe)*