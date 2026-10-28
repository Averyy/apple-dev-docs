# VTFrameProcessor

**Framework**: Video Toolbox  
**Kind**: class  
**Role**: Class

A class that creates a new frame processor for the configured video effect.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class VTFrameProcessor
```

```objc
@interface VTFrameProcessor : NSObject
```

## Overview

Use this class to perform frame by frame processing on your video. Start by specifying a video effect by passing a [`VTFrameProcessorConfiguration`](./vtframeprocessorconfiguration.md) object to the [`startSession(configuration:)`](./vtframeprocessor/startsession%28configuration%29.md) call. Once the session is created, [`process(parameters:completionHandler:)`](./vtframeprocessor/process%28parameters,completionhandler%29.md) is called in a loop to process your video’s frames one at a time. Once all the frames are processed, call an [`endSession()`](./vtframeprocessor/endsession%28%29.md) to finish all pending processing.

For successful processing, the caller needs to ensure that all buffers passed to the processWithParameters interface are unmodified (including attachments) until the function returns or the callback is received in the case of asynchronous mode.

## Topics

### Creating a frame processor
- [init()](./vtframeprocessor/init%28%29.md)
  Creates a new frame processor.
### Processing frames
- [func startSession(configuration: any VTFrameProcessorConfiguration) throws](./vtframeprocessor/startsession%28configuration%29.md)
  Starts a new session and configures the processor pipeline.
- [func process(parameters: any VTFrameProcessorParameters) -> some AsyncSequence<VTFrameProcessorFrame.ReadOnlyFrame, any Error>
](./vtframeprocessor/process%28parameters%29.md)
- [func process(parameters: any VTFrameProcessorParameters, completionHandler: (any VTFrameProcessorParameters, (any Error)?) -> Void)](./vtframeprocessor/process%28parameters,completionhandler%29.md)
  Asynchronously performs the video effect specified in the start session.
- [func process(with: any MTLCommandBuffer, parameters: any VTFrameProcessorParameters)](./vtframeprocessor/process%28with,parameters%29.md)
  Asynchronously performs the video effect specified in the start session specifically for Metal.
- [func endSession()](./vtframeprocessor/endsession%28%29.md)
  Performs all necessary tasks to end the session.
### Instance Methods
- [- processWithParameters:error:](./vtframeprocessor/processwithparameters_error_.md)
  Synchronously performs the configured video effect.
- [- processWithParameters:frameOutputHandler:](./vtframeprocessor/processwithparameters_frameoutputhandler_.md)
  Asynchronously performs the processor effects and outputs each frame separately.

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
- [protocol VTFrameProcessorConfiguration](./vtframeprocessorconfiguration.md)
  A protocol that describes the configuration of a processor to use during a video processing session.
- [class VTFrameProcessorFrame](./vtframeprocessorframe.md)
  An object that wraps video frames to send to the processor, as source, reference, or output frames.
- [protocol VTFrameProcessorParameters](./vtframeprocessorparameters.md)
  The base protocol for input and output processing parameters for a frame processor implementation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessor)*