# process(parameters:completionHandler:)

**Framework**: Video Toolbox  
**Kind**: method  
**Role**: Instance Method

Asynchronously performs the video effect specified in the start session.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func process(parameters: any VTFrameProcessorParameters, completionHandler: @escaping @Sendable (any VTFrameProcessorParameters, (any Error)?) -> Void)
```

```swift
func process(parameters: any VTFrameProcessorParameters) async throws -> any VTFrameProcessorParameters
```

```objc
- (void) processWithParameters:(id<VTFrameProcessorParameters>) parameters completionHandler:(void (^)(id<VTFrameProcessorParameters>, NSError *)) completionHandler;
```

## Parameters

- `parameters`: A [`VTFrameProcessorParameters`](../vtframeprocessorparameters.md) object to specify additional parameters to use during processing. It needs to match the configuration type used during start session.
- `completionHandler`: This completion handler is called when the frame processing is completed.  The completion handler will receive the same parameters object that was provided to the original call, as well as an NSError which will contain an error code if processing was not successful.

## See Also

### Processing frames
- [func startSession(configuration: any VTFrameProcessorConfiguration) throws](./startsession%28configuration%29.md)
  Starts a new session and configures the processor pipeline.
- [func process(parameters: any VTFrameProcessorParameters) -> some AsyncSequence<VTFrameProcessorFrame.ReadOnlyFrame, any Error>
](./process%28parameters%29.md)
- [func process(with: any MTLCommandBuffer, parameters: any VTFrameProcessorParameters)](./process%28with,parameters%29.md)
  Asynchronously performs the video effect specified in the start session specifically for Metal.
- [func endSession()](./endsession%28%29.md)
  Performs all necessary tasks to end the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessor/process(parameters:completionhandler:))*