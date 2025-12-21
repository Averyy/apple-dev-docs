# VTMotionBlurParameters

**Framework**: Video Toolbox  
**Kind**: class

This object contains both input and output parameters necessary to run the motion blur processor on a frame.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+

## Declaration

```swift
class VTMotionBlurParameters
```

#### Overview

This object is used in the processWithParameters call of the VTFrameProcessor class. The output parameter is a destinationFrame where the output frame is returned as a VTFrameProcessorFrame back to the caller function once processWithParameters completes.

The parameters within VTMotionBlurParameters are frame level parameters.

## Topics

### Creating a parameters object
- [init?(sourceFrame: VTFrameProcessorFrame, nextFrame: VTFrameProcessorFrame?, previousFrame: VTFrameProcessorFrame?, nextOpticalFlow: VTFrameProcessorOpticalFlow?, previousOpticalFlow: VTFrameProcessorOpticalFlow?, motionBlurStrength: Int, submissionMode: VTMotionBlurParameters.SubmissionMode, destinationFrame: VTFrameProcessorFrame)](vtmotionblurparameters/init(sourceframe:nextframe:previousframe:nextopticalflow:previousopticalflow:motionblurstrength:submissionmode:destinationframe:).md)
### Inspecting the parameters
- [var sourceFrame: VTFrameProcessorFrame](vtmotionblurparameters/sourceframe.md)
  The current source frame.
- [var nextFrame: VTFrameProcessorFrame?](vtmotionblurparameters/nextframe.md)
  The next source frame in presentation time order.
- [var previousFrame: VTFrameProcessorFrame?](vtmotionblurparameters/previousframe.md)
  The previous source frame in presentation time order.
- [var motionBlurStrength: Int](vtmotionblurparameters/motionblurstrength.md)
  A value that indicates the strength of blur to apply.
- [var nextOpticalFlow: VTFrameProcessorOpticalFlow?](vtmotionblurparameters/nextopticalflow.md)
  Optional optical flow object that contains forward and backward optical flow with the next frame.
- [var previousOpticalFlow: VTFrameProcessorOpticalFlow?](vtmotionblurparameters/previousopticalflow.md)
  Optional optical flow object that contains forward and backward optical flow with the previous frame.
- [var submissionMode: VTMotionBlurParameters.SubmissionMode](vtmotionblurparameters/submissionmode-swift.property.md)
  A value describing the processing request in a parameters submission object.
- [VTMotionBlurParameters.SubmissionMode](vtmotionblurparameters/submissionmode-swift.enum.md)
  A value describing the processing request in a parameters submission object.

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

- [class VTMotionBlurConfiguration](vtmotionblurconfiguration.md)
  A configuration object to enable motion blur on a frame processing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmotionblurparameters)*