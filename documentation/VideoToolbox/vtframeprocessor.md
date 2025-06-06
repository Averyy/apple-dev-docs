# VTFrameProcessor

**Framework**: Videotoolbox  
**Kind**: class

A class that creates a new frame processor for the configured video effect.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class VTFrameProcessor
```

#### Overview

Use this class to perform frame by frame processing on your video. Start by specifying a video effect by passing a [`VTFrameProcessorConfiguration`](vtframeprocessorconfiguration.md) object to the [`startSession(configuration:)`](vtframeprocessor/startsession(configuration:).md) call. Once the session is created, [`process(parameters:completionHandler:)`](vtframeprocessor/process(parameters:completionhandler:).md) is called in a loop to process your video’s frames one at a time. Once all the frames are processed, call an [`endSession()`](vtframeprocessor/endsession().md) to finish all pending processing.

For successful processing, the caller needs to ensure that all buffers passed to the processWithParameters interface are unmodified (including attachments) until the function returns or the callback is received in the case of asynchronous mode.

## Topics

### Creating a frame processor
- [init()](vtframeprocessor/init.md)
  Creates a new frame processor.
### Processing frames
- [func startSession(configuration: any VTFrameProcessorConfiguration) throws](vtframeprocessor/startsession(configuration:).md)
  Starts a new session and configures the processor pipeline.
- [func process(parameters: any VTFrameProcessorParameters, completionHandler: (any VTFrameProcessorParameters, (any Error)?) -> Void)](vtframeprocessor/process(parameters:completionhandler:).md)
  Asynchronously performs the video effect specified in the start session.
- [func process(with: any MTLCommandBuffer, parameters: any VTFrameProcessorParameters)](vtframeprocessor/process(with:parameters:).md)
  Asynchronously performs the video effect specified in the start session specifically for Metal.
- [func endSession()](vtframeprocessor/endsession.md)
  Performs all necessary tasks to end the session.

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

- [class VTFrameProcessorFrame](vtframeprocessorframe.md)
  An object that wraps video frames to send to the processor, as source, reference, or output frames.
- [protocol VTFrameProcessorConfiguration](vtframeprocessorconfiguration.md)
  A protocol that describes the configuration of a processor to use during a video processing session.
- [protocol VTFrameProcessorParameters](vtframeprocessorparameters.md)
  The base protocol for input and output processing parameters for a frame processor implementation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessor)*