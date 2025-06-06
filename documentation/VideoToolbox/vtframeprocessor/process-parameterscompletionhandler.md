# process(parameters:completionHandler:)

**Framework**: Videotoolbox  
**Kind**: method

Asynchronously performs the video effect specified in the start session.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func process(parameters: any VTFrameProcessorParameters) async throws -> any VTFrameProcessorParameters
```

## Parameters

- `parameters`: A   object to specify additional parameters to use during processing. It needs to match the configuration type used during start session.
- `completionHandler`: This completion handler is called when the frame processing is completed.  The completion handler will receive the same parameters object that was provided to the original call, as well as an NSError which will contain an error code if processing was not successful.

## See Also

- [func startSession(configuration: any VTFrameProcessorConfiguration) throws](vtframeprocessor/startsession(configuration:).md)
  Starts a new session and configures the processor pipeline.
- [func process(with: any MTLCommandBuffer, parameters: any VTFrameProcessorParameters)](vtframeprocessor/process(with:parameters:).md)
  Asynchronously performs the video effect specified in the start session specifically for Metal.
- [func endSession()](vtframeprocessor/endsession.md)
  Performs all necessary tasks to end the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessor/process(parameters:completionhandler:))*