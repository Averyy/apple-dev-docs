# VTFrameRateConversionParameters

**Framework**: Videotoolbox  
**Kind**: class

An object that contains the required input and output parameters to run a frame rate conversion processor on a frame.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class VTFrameRateConversionParameters
```

#### Overview

This object is used in the processWithParameters call of a VTFrameProcessor class. The output parameter is a destinationFrame where the output frame is returned as a VTFrameProcessorMutableFrame back to the caller function once the processing completes.

The parameters within VTFrameRateConversionParameters are frame level parameters.

## Topics

### Creating conversion parameters
- [convenience init?(sourceFrame: VTFrameProcessorFrame, nextFrame: VTFrameProcessorFrame, opticalFlow: VTFrameProcessorOpticalFlow?, interpolationPhase: [Float], submissionMode: VTFrameRateConversionParameters.SubmissionMode, destinationFrames: [VTFrameProcessorFrame])](vtframerateconversionparameters/init(sourceframe:nextframe:opticalflow:interpolationphase:submissionmode:destinationframes:).md)
  Creates a new frame rate conversion parameters object.
### Inspecting the parameters
- [var sourceFrame: VTFrameProcessorFrame](vtframerateconversionparameters/sourceframe.md)
  The current source frame.
- [var nextFrame: VTFrameProcessorFrame?](vtframerateconversionparameters/nextframe.md)
  The next source frame in presentation time order.
- [var opticalFlow: VTFrameProcessorOpticalFlow?](vtframerateconversionparameters/opticalflow.md)
  A property that defines the optical flow for an object.
- [var interpolationPhase: [Float]](vtframerateconversionparameters/interpolationphase-2jky5.md)
  An array of floating-point values that indicate which intervals to insert a frame between the current and next frame.
- [var submissionMode: VTFrameRateConversionParameters.SubmissionMode](vtframerateconversionparameters/submissionmode-swift.property.md)
  A value describing the processing request in a parameters submission object.
- [VTFrameRateConversionParameters.SubmissionMode](vtframerateconversionparameters/submissionmode-swift.enum.md)
  A value describing the processing request in a parameters submission object.
- [var destinationFrames: [VTFrameProcessorFrame]](vtframerateconversionparameters/destinationframes.md)
  A caller-allocated array of frames that contains the pixel buffers to receive the results.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [VTFrameProcessorParameters](vtframeprocessorparameters.md)

## See Also

- [class VTFrameRateConversionConfiguration](vtframerateconversionconfiguration.md)
  An object that enables the frame rate conversion on a frame processing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframerateconversionparameters)*