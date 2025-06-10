# VTFrameProcessorOpticalFlow

**Framework**: Video Toolbox  
**Kind**: class

A class to wrap bidirectional optical flow to send to the processor.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 15.4+
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class VTFrameProcessorOpticalFlow
```

#### Overview

Instances retain the buffers backing them.

## Topics

### Creating an optical flow configuration
- [init?(forwardFlow: CVPixelBuffer, backwardFlow: CVPixelBuffer)](vtframeprocessoropticalflow/init(forwardflow:backwardflow:).md)
  Creates an object with forward and backward optical flow pixel buffers.
### Inspecting the configuration
- [var backwardFlow: CVPixelBuffer](vtframeprocessoropticalflow/backwardflow.md)
  The backward optical flow pixel buffer that was provided when the object was created.
- [var forwardFlow: CVPixelBuffer](vtframeprocessoropticalflow/forwardflow.md)
  The forward optical flow pixel that was provided when the object was created.

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

## See Also

- [class VTOpticalFlowConfiguration](vtopticalflowconfiguration.md)
  A configuration object that enables optical flow on a frame processing session.
- [class VTOpticalFlowParameters](vtopticalflowparameters.md)
  An object that describes frame-level optical flow parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessoropticalflow)*