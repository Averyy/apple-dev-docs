# VTOpticalFlowParameters

**Framework**: Video Toolbox  
**Kind**: class

An object that describes frame-level optical flow parameters.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+

## Declaration

```swift
class VTOpticalFlowParameters
```

## Topics

### Creating a parameters object
- [init?(sourceFrame: VTFrameProcessorFrame, nextFrame: VTFrameProcessorFrame, submissionMode: VTOpticalFlowParameters.SubmissionMode, destinationOpticalFlow: VTFrameProcessorOpticalFlow)](vtopticalflowparameters/init(sourceframe:nextframe:submissionmode:destinationopticalflow:).md)
### Inspecting the parameters
- [var sourceFrame: VTFrameProcessorFrame](vtopticalflowparameters/sourceframe.md)
  The current source frame.
- [var nextFrame: VTFrameProcessorFrame](vtopticalflowparameters/nextframe.md)
  The next source frame in presentation time order.
- [var destinationOpticalFlow: VTFrameProcessorOpticalFlow](vtopticalflowparameters/destinationopticalflow.md)
  A user allocated mutable optical flow that will receive the results.
- [var submissionMode: VTOpticalFlowParameters.SubmissionMode](vtopticalflowparameters/submissionmode-swift.property.md)
  A value describing the processing request in a parameters submission object.
- [VTOpticalFlowParameters.SubmissionMode](vtopticalflowparameters/submissionmode-swift.enum.md)
  A value describing the processing request in a parameters submission object.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [VTFrameProcessorParameters](vtframeprocessorparameters.md)

## See Also

- [class VTFrameProcessorOpticalFlow](vtframeprocessoropticalflow.md)
  A class to wrap bidirectional optical flow to send to the processor.
- [class VTOpticalFlowConfiguration](vtopticalflowconfiguration.md)
  A configuration object that enables optical flow on a frame processing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtopticalflowparameters)*