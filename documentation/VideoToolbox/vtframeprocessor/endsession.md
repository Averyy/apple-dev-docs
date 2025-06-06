# endSession()

**Framework**: Videotoolbox  
**Kind**: method

Performs all necessary tasks to end the session.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func endSession()
```

#### Discussion

After this call completes, no new frames can be processed unless [`startSession(configuration:)`](vtframeprocessor/startsession(configuration:).md) is called again.

## See Also

- [func startSession(configuration: any VTFrameProcessorConfiguration) throws](vtframeprocessor/startsession(configuration:).md)
  Starts a new session and configures the processor pipeline.
- [func process(parameters: any VTFrameProcessorParameters, completionHandler: (any VTFrameProcessorParameters, (any Error)?) -> Void)](vtframeprocessor/process(parameters:completionhandler:).md)
  Asynchronously performs the video effect specified in the start session.
- [func process(with: any MTLCommandBuffer, parameters: any VTFrameProcessorParameters)](vtframeprocessor/process(with:parameters:).md)
  Asynchronously performs the video effect specified in the start session specifically for Metal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessor/endsession())*