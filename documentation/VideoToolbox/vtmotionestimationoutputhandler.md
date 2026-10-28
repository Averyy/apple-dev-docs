# VTMotionEstimationOutputHandler

**Framework**: Video Toolbox  
**Kind**: typealias  
**Role**: Type Alias

A block invoked by motion-estimation session when frame processing is complete.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
typealias VTMotionEstimationOutputHandler = (OSStatus, __VTMotionEstimationInfoFlags, CFDictionary?, CVPixelBuffer?) -> Void
```

```c
typedef void (^)(int, enum VTMotionEstimationInfoFlags, const struct __CFDictionary *, struct __CVBuffer *) VTMotionEstimationOutputHandler;
```

## Discussion

When the client requests a motion-estimation, the client passes in a callback block that the system invokes for the result of that request. If the `VTMotionEstimationSessionCreateMotionEstimation` call returns an error, the system does not invoke this block.

## Parameters

- `status`: `noErr` if processing request was successful; an error code if motion-estimation was not successful.
- `infoFlags`: A bit field that contains information about the processing operation.
- `additionalInfo`: Additional processing information about the operation that cannot fit in `infoFlags`. Currently, the system expects this to be NULL.
- `motionVectorPixelBuffer`: A `CVPixelBuffer` that contains the motion vector information, if processing request was successful; otherwise, NULL.

## See Also

### Handling output
- [VTMotionEstimationSessionCompleteFrames](./vtmotionestimationsessioncompleteframes.md)
  Directs the motion-estimation session to emit all pending frames and waits for completion.
- [VTMotionEstimationSessionCopySourcePixelBufferAttributes](./vtmotionestimationsessioncopysourcepixelbufferattributes.md)
  Copies the attributes for source pixel buffers expected by motion-estimation session.
- [VTMotionEstimationSessionEstimateMotionVectors](./vtmotionestimationsessionestimatemotionvectors.md)
  Creates a new pixel buffer that contains motion vectors between the input pixel buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmotionestimationoutputhandler)*