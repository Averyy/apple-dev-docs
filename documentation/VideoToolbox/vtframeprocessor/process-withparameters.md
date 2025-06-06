# process(with:parameters:)

**Framework**: Videotoolbox  
**Kind**: method

Asynchronously performs the video effect specified in the start session specifically for Metal.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func process(with commandBuffer: any MTLCommandBuffer, parameters: any VTFrameProcessorParameters)
```

#### Discussion

This function allows you to add the effect to an existing Metal command buffer. This can be used by clients that have an existing Metal pipeline and want to add this effect to it.

> **Note**: This is an asynchronous call that waits until all previously inserted tasks in the command buffer finish before running. Tasks inserted after the buffer will run after the effect is applied.

## Parameters

- `commandBuffer`: An existing Metal command buffer where the frame processing will be inserted.
- `parameters`: A VTFrameProcessorParameters based object to specify additional frame based parameters to be used during processing. It needs to match the configuration type used during start session.

## See Also

- [func startSession(configuration: any VTFrameProcessorConfiguration) throws](vtframeprocessor/startsession(configuration:).md)
  Starts a new session and configures the processor pipeline.
- [func process(parameters: any VTFrameProcessorParameters, completionHandler: (any VTFrameProcessorParameters, (any Error)?) -> Void)](vtframeprocessor/process(parameters:completionhandler:).md)
  Asynchronously performs the video effect specified in the start session.
- [func endSession()](vtframeprocessor/endsession.md)
  Performs all necessary tasks to end the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessor/process(with:parameters:))*