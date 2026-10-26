# processWithParameters:error:

**Framework**: Video Toolbox  
**Kind**: method  
**Role**: Instance Method

Synchronously performs the configured video effect.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (BOOL) processWithParameters:(id<VTFrameProcessorParameters>) parameters error:(NSError **) error;
```

#### Discussion

Frame level settings and frame level input/output parameters are passed by using the respective [`VTFrameProcessorParameters`](../vtframeprocessorparameters.md) for the effect that the frame processor is configured for.

## Parameters

- `parameters`: Frame processing parameters to specify additional frame based parameters to be used during processing. The parameters need to match the configuration type used during start session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessor/processwithparameters:error:)*