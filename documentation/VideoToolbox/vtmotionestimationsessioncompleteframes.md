# VTMotionEstimationSessionCompleteFrames

**Framework**: Video Toolbox  
**Kind**: func  
**Role**: Function

Directs the motion-estimation session to emit all pending frames and waits for completion.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```c
extern OSStatus VTMotionEstimationSessionCompleteFrames(VTMotionEstimationSessionRef session);
```

## Discussion

Directs the motion-estimation session to emit all pending frames, then waits for all outstanding requests to complete, then returns.

## See Also

### Handling output
- [typealias VTMotionEstimationOutputHandler](./vtmotionestimationoutputhandler.md)
  A block invoked by motion-estimation session when frame processing is complete.
- [VTMotionEstimationSessionCopySourcePixelBufferAttributes](./vtmotionestimationsessioncopysourcepixelbufferattributes.md)
  Copies the attributes for source pixel buffers expected by motion-estimation session.
- [VTMotionEstimationSessionEstimateMotionVectors](./vtmotionestimationsessionestimatemotionvectors.md)
  Creates a new pixel buffer that contains motion vectors between the input pixel buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmotionestimationsessioncompleteframes)*