# VTMotionEstimationSessionCopySourcePixelBufferAttributes

**Framework**: Video Toolbox  
**Kind**: func  
**Role**: Function

Copies the attributes for source pixel buffers expected by motion-estimation session.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```c
extern OSStatus VTMotionEstimationSessionCopySourcePixelBufferAttributes(VTMotionEstimationSessionRef motionEstimationSession, CFDictionaryRef*attributesOut);
```

#### Discussion

This function provides a `CFDictionary` of attributes that you must release. Use this function to query [`VTMotionEstimationSession`](./vtmotionestimationsession.md) for the native source attributes. If you provide an input `CVPixelBuffer` that is not compatible with the attributes that this function returns, [`VTMotionEstimationSession`](./vtmotionestimationsession.md) automatically converts the input pixel buffer into a compatible pixel buffer for processing.

## Parameters

- `attributesOut`: Points to a variable to receive the attributes dictionary.

## See Also

### Handling output
- [typealias VTMotionEstimationOutputHandler](./vtmotionestimationoutputhandler.md)
  A block invoked by motion-estimation session when frame processing is complete.
- [VTMotionEstimationSessionCompleteFrames](./vtmotionestimationsessioncompleteframes.md)
  Directs the motion-estimation session to emit all pending frames and waits for completion.
- [VTMotionEstimationSessionEstimateMotionVectors](./vtmotionestimationsessionestimatemotionvectors.md)
  Creates a new pixel buffer that contains motion vectors between the input pixel buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmotionestimationsessioncopysourcepixelbufferattributes)*