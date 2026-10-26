# processWithParameters:frameOutputHandler:

**Framework**: Video Toolbox  
**Kind**: method  
**Role**: Instance Method

Asynchronously performs the processor effects and outputs each frame separately.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (void) processWithParameters:(id<VTFrameProcessorParameters>) parameters frameOutputHandler:(void (^)(id<VTFrameProcessorParameters>, CMTime , BOOL , NSError *)) frameOutputHandler;
```

#### Discussion

Use with frame processor configurations which allow multiple output frames from a single processing call, such as frame rate conversion processor cases when you need access to output frames as they become available, rather than waiting for all output frames to be complete.

This interface is suitable for low-latency scenarios when a call would generate multiple output frames, but waiting for all frames to be generated before beginning to use the frames is not ideal. Because the processor may use the output frames as references for frames still being generated, the output frames are strictly read-only. If you want to modify the frames, you must create a copy first.

## Parameters

- `parameters`: A `VTFrameProcessorParameters` based object to specify additional frame based parameters to use during processing. It needs to match the configuration type used during start session.
- `frameOutputHandler`: This frame output handler is called once for each destination frame in the provided parameters if no errors are encountered. The output handler receives the same parameters object that you provided to the original call, a flag indicating if this is the final output to be called for this processing request, and the presentation timestamp associated with the `VTFrameProcessorFrame` that it is being called for. The `NSError` parameter contains an error code if processing was not successful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessor/processwithparameters:frameoutputhandler:)*