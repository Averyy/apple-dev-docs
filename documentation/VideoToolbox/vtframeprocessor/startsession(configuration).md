# startSession(configuration:)

**Framework**: Video Toolbox  
**Kind**: method  
**Role**: Instance Method

Starts a new session and configures the processor pipeline.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func startSession(configuration: any VTFrameProcessorConfiguration) throws
```

```objc
- (BOOL) startSessionWithConfiguration:(id<VTFrameProcessorConfiguration>) configuration error:(NSError **) error;
```

## Parameters

- `configuration`: A configuration object for the video effect that will be applied in the subsequent processing calls.

## See Also

### Processing frames
- [func process(parameters: any VTFrameProcessorParameters) -> some AsyncSequence<VTFrameProcessorFrame.ReadOnlyFrame, any Error>
](./process%28parameters%29.md)
- [func process(parameters: any VTFrameProcessorParameters, completionHandler: (any VTFrameProcessorParameters, (any Error)?) -> Void)](./process%28parameters,completionhandler%29.md)
  Asynchronously performs the video effect specified in the start session.
- [func process(with: any MTLCommandBuffer, parameters: any VTFrameProcessorParameters)](./process%28with,parameters%29.md)
  Asynchronously performs the video effect specified in the start session specifically for Metal.
- [func endSession()](./endsession%28%29.md)
  Performs all necessary tasks to end the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessor/startsession(configuration:))*