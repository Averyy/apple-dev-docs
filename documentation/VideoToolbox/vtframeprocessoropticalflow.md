# VTFrameProcessorOpticalFlow

**Framework**: Video Toolbox  
**Kind**: class  
**Role**: Class

A class to wrap bidirectional optical flow to send to the processor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class VTFrameProcessorOpticalFlow
```

```objc
@interface VTFrameProcessorOpticalFlow : NSObject
```

## Overview

Instances retain the buffers backing them.

## Topics

### Creating an optical flow configuration
- [init?(forwardFlow: CVPixelBuffer, backwardFlow: CVPixelBuffer)](./vtframeprocessoropticalflow/init%28forwardflow,backwardflow%29.md)
  Creates an object with forward and backward optical flow pixel buffers.
### Inspecting the configuration
- [var backwardFlow: CVPixelBuffer](./vtframeprocessoropticalflow/backwardflow.md)
  The backward optical flow pixel buffer that was provided when the object was created.
- [var forwardFlow: CVPixelBuffer](./vtframeprocessoropticalflow/forwardflow.md)
  The forward optical flow pixel that was provided when the object was created.

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

## See Also

### Optical flow
- [class VTOpticalFlowConfiguration](./vtopticalflowconfiguration.md)
  A configuration object that enables optical flow on a frame processing session.
- [class VTOpticalFlowParameters](./vtopticalflowparameters.md)
  An object that describes frame-level optical flow parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessoropticalflow)*