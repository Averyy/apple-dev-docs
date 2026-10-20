# process(parameters:)

**Framework**: Video Toolbox  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func process(parameters: any VTFrameProcessorParameters) -> some AsyncSequence<VTFrameProcessorFrame.ReadOnlyFrame, any Error>
```

## See Also

### Processing frames
- [func startSession(configuration: any VTFrameProcessorConfiguration) throws](./startsession%28configuration%29.md)
  Starts a new session and configures the processor pipeline.
- [func process(parameters: any VTFrameProcessorParameters, completionHandler: (any VTFrameProcessorParameters, (any Error)?) -> Void)](./process%28parameters,completionhandler%29.md)
  Asynchronously performs the video effect specified in the start session.
- [func process(with: any MTLCommandBuffer, parameters: any VTFrameProcessorParameters)](./process%28with,parameters%29.md)
  Asynchronously performs the video effect specified in the start session specifically for Metal.
- [func endSession()](./endsession%28%29.md)
  Performs all necessary tasks to end the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessor/process(parameters:))*