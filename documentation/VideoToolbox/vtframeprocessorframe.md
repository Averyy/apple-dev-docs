# VTFrameProcessorFrame

**Framework**: Video Toolbox  
**Kind**: class  
**Role**: Class

An object that wraps video frames to send to the processor, as source, reference, or output frames.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class VTFrameProcessorFrame
```

```objc
@interface VTFrameProcessorFrame : NSObject
```

#### Overview

Instances retain the buffer backing them.

## Topics

### Creating a frame object
- [init?(buffer: CVPixelBuffer, presentationTimeStamp: CMTime)](./vtframeprocessorframe/init%28buffer,presentationtimestamp%29.md)
  Creates a frame object with a pixel buffer and presentation time.
### Inspecting the frame
- [var buffer: CVPixelBuffer](./vtframeprocessorframe/buffer.md)
  The pixel buffer specified when the object was created.
- [var presentationTimeStamp: CMTime](./vtframeprocessorframe/presentationtimestamp.md)
  The presentation timestamp specified when the object was created.
### Structures
- [VTFrameProcessorFrame.ReadOnlyFrame](./vtframeprocessorframe/readonlyframe.md)

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

### Frame processor
- [Enhancing your app with machine learning-based video effects](./enhancing-your-app-with-machine-learning-based-video-effects.md)
  Add powerful effects to your videos using the VideoToolbox VTFrameProcessor API.
- [class VTFrameProcessor](./vtframeprocessor.md)
  A class that creates a new frame processor for the configured video effect.
- [protocol VTFrameProcessorConfiguration](./vtframeprocessorconfiguration.md)
  A protocol that describes the configuration of a processor to use during a video processing session.
- [protocol VTFrameProcessorParameters](./vtframeprocessorparameters.md)
  The base protocol for input and output processing parameters for a frame processor implementation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessorframe)*