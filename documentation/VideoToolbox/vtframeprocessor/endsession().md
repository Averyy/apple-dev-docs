# endSession()

**Framework**: Video Toolbox  
**Kind**: method  
**Role**: Instance Method

Performs all necessary tasks to end the session.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func endSession()
```

```objc
- (void) endSession;
```

#### Discussion

After this call completes, no new frames can be processed unless [`startSession(configuration:)`](./startsession%28configuration%29.md) is called again.

## See Also

### Processing frames
- [func startSession(configuration: any VTFrameProcessorConfiguration) throws](./startsession%28configuration%29.md)
  Starts a new session and configures the processor pipeline.
- [func process(parameters: any VTFrameProcessorParameters) -> some AsyncSequence<VTFrameProcessorFrame.ReadOnlyFrame, any Error>
](./process%28parameters%29.md)
- [func process(parameters: any VTFrameProcessorParameters, completionHandler: (any VTFrameProcessorParameters, (any Error)?) -> Void)](./process%28parameters,completionhandler%29.md)
  Asynchronously performs the video effect specified in the start session.
- [func process(with: any MTLCommandBuffer, parameters: any VTFrameProcessorParameters)](./process%28with,parameters%29.md)
  Asynchronously performs the video effect specified in the start session specifically for Metal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessor/endsession())*