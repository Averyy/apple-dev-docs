# startSession(configuration:)

**Framework**: Video Toolbox  
**Kind**: method

Starts a new session and configures the processor pipeline.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 15.4+
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func startSession(configuration: any VTFrameProcessorConfiguration) throws
```

## Parameters

- `configuration`: A configuration object for the video effect that will be applied in the subsequent processing calls.

## See Also

- [func process(parameters: any VTFrameProcessorParameters, completionHandler: (any VTFrameProcessorParameters, (any Error)?) -> Void)](vtframeprocessor/process(parameters:completionhandler:).md)
  Asynchronously performs the video effect specified in the start session.
- [func process(with: any MTLCommandBuffer, parameters: any VTFrameProcessorParameters)](vtframeprocessor/process(with:parameters:).md)
  Asynchronously performs the video effect specified in the start session specifically for Metal.
- [func endSession()](vtframeprocessor/endsession.md)
  Performs all necessary tasks to end the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessor/startsession(configuration:))*