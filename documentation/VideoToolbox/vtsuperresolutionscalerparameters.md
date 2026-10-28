# VTSuperResolutionScalerParameters

**Framework**: Video Toolbox  
**Kind**: class  
**Role**: Class

An object that contains both input and output parameters that the super-resolution processor needs to run on a frame.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
class VTSuperResolutionScalerParameters
```

```objc
@interface VTSuperResolutionScalerParameters : NSObject
```

## Overview

Use this object in the `processWithParameters` call of the `VTFrameProcessor` class. The output parameter for this class is `destinationFrame`, where the processor returns the output frame (as `VTFrameProcessorFrame`) back to you once `processWithParameters` completes.

`VTSuperResolutionScalerParameters` are frame-level parameters.

## Topics

### Creating a parameters object
- [init?(sourceFrame: VTFrameProcessorFrame, previousFrame: VTFrameProcessorFrame?, previousOutputFrame: VTFrameProcessorFrame?, opticalFlow: VTFrameProcessorOpticalFlow?, submissionMode: VTSuperResolutionScalerParameters.SubmissionMode, destinationFrame: VTFrameProcessorFrame)](./vtsuperresolutionscalerparameters/init%28sourceframe,previousframe,previousoutputframe,opticalflow,submissionmode,destinationframe%29.md)
  Creates a new super-resolution scaler parameters instance.
### Inspecting the parameters
- [var sourceFrame: VTFrameProcessorFrame](./vtsuperresolutionscalerparameters/sourceframe.md)
  Current source frame, which must be non `nil`.
- [var previousFrame: VTFrameProcessorFrame?](./vtsuperresolutionscalerparameters/previousframe.md)
  Previous source frame in presentation time order, which is `nil` for the first frame.
- [var previousOutputFrame: VTFrameProcessorFrame?](./vtsuperresolutionscalerparameters/previousoutputframe.md)
  Previous output frame in presentation time order, which is `nil` for the first frame.
- [var opticalFlow: VTFrameProcessorOpticalFlow?](./vtsuperresolutionscalerparameters/opticalflow.md)
  Optional object that contains forward and backward optical flow with the previous frame.
- [var submissionMode: VTSuperResolutionScalerParameters.SubmissionMode](./vtsuperresolutionscalerparameters/submissionmode-swift.property.md)
  Ordering of the input frames in this submission relative to the previous submission.
- [VTSuperResolutionScalerParameters.SubmissionMode](./vtsuperresolutionscalerparameters/submissionmode-swift.enum.md)
  Indicates the order of input frames.
- [destinationFrame](./vtsuperresolutionscalerparameters/destinationframe.md)
  Destination frame that contains user-allocated pixel buffer that receives the results.

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

### Super resolution
- [class VTSuperResolutionScalerConfiguration](./vtsuperresolutionscalerconfiguration.md)
  Configuration that you use to set up the super-resolution processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsuperresolutionscalerparameters)*