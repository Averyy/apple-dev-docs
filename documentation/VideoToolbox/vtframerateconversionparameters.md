# VTFrameRateConversionParameters

**Framework**: Video Toolbox  
**Kind**: class  
**Role**: Class

An object that contains the required input and output parameters to run a frame rate conversion processor on a frame.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+

## Declaration

```swift
class VTFrameRateConversionParameters
```

```objc
@interface VTFrameRateConversionParameters : NSObject
```

## Overview

This object is used in the processWithParameters call of a VTFrameProcessor class. The output parameter is a destinationFrame where the output frame is returned as a VTFrameProcessorMutableFrame back to the caller function once the processing completes.

The parameters within VTFrameRateConversionParameters are frame level parameters.

## Topics

### Creating conversion parameters
- [convenience init?(sourceFrame: VTFrameProcessorFrame, nextFrame: VTFrameProcessorFrame, opticalFlow: VTFrameProcessorOpticalFlow?, interpolationPhase: [Float], submissionMode: VTFrameRateConversionParameters.SubmissionMode, destinationFrames: [VTFrameProcessorFrame])](./vtframerateconversionparameters/init%28sourceframe,nextframe,opticalflow,interpolationphase,submissionmode,destinationframes%29.md)
  Creates a new frame rate conversion parameters object.
- [- initWithSourceFrame:nextFrame:opticalFlow:interpolationPhase:submissionMode:destinationFrames:](./vtframerateconversionparameters/initwithsourceframe_nextframe_opticalflow_interpolationphase_submissionmode_destinationframes_.md)
  Creates a new frame rate conversion parameters object.
### Inspecting the parameters
- [var sourceFrame: VTFrameProcessorFrame](./vtframerateconversionparameters/sourceframe.md)
  The current source frame.
- [var nextFrame: VTFrameProcessorFrame?](./vtframerateconversionparameters/nextframe.md)
  The next source frame in presentation time order.
- [var opticalFlow: VTFrameProcessorOpticalFlow?](./vtframerateconversionparameters/opticalflow.md)
  A property that defines the optical flow for an object.
- [var interpolationPhase: [Float]](./vtframerateconversionparameters/interpolationphase-2jky5.md)
  An array of floating-point values that indicate which intervals to insert a frame between the current and next frame.
- [var submissionMode: VTFrameRateConversionParameters.SubmissionMode](./vtframerateconversionparameters/submissionmode-swift.property.md)
  A value describing the processing request in a parameters submission object.
- [VTFrameRateConversionParameters.SubmissionMode](./vtframerateconversionparameters/submissionmode-swift.enum.md)
  A value describing the processing request in a parameters submission object.
- [interpolationPhase](./vtframerateconversionparameters/interpolationphase-6wdns.md)
  An array of floating-point values that indicate which intervals to insert a frame between the current and next frame.
- [destinationFrames](./vtframerateconversionparameters/destinationframes.md)
  A caller-allocated array of frames that contains the pixel buffers to receive the results.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [VTFrameProcessorParameters](./vtframeprocessorparameters.md)

## See Also

### Frame rate conversion
- [class VTFrameRateConversionConfiguration](./vtframerateconversionconfiguration.md)
  An object that enables the frame rate conversion on a frame processing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframerateconversionparameters)*