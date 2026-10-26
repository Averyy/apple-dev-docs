# VTMotionEstimationSessionEstimateMotionVectors

**Framework**: Video Toolbox  
**Kind**: func  
**Role**: Function

Creates a new pixel buffer that contains motion vectors between the input pixel buffers.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```c
extern OSStatus VTMotionEstimationSessionEstimateMotionVectors(VTMotionEstimationSessionRef session, CVPixelBufferRef referenceImage, CVPixelBufferRef currentImage, VTMotionEstimationFrameFlags motionEstimationFrameFlags, CFDictionaryRef additionalFrameOptions, VTMotionEstimationOutputHandler outputHandler);
```

#### Return Value

If the call was successful, returns `noErr`; otherwise, returns an error code, such as `kVTMotionEstimationNotSupportedErr`.

#### Discussion

The motion-estimation session compares the reference frame to the current frame, and generates motion vectors in the form of a `CVPixelBuffer`.

## Parameters

- `session`: The motion-estimation session.
- `referenceImage`: The reference image.
- `currentImage`: The current image.
- `motionEstimationFrameFlags`: A bit field with per-frame options. See `kVTMotionEstimationFrameFlags_CurrentBufferWillBeNextReferenceBuffer`.
- `additionalFrameOptions`: A way to pass additional information that doesn’t fit in `motionEstimationFrameFlags`; currently the system expects it to be `NULL`.
- `outputHandler`: The block invoked by the syetem when the processing request is completed. If the `VTMotionEstimationSessionCreateMotionEstimation` call returns an error, the system does not invoke the block.

## See Also

### Handling output
- [typealias VTMotionEstimationOutputHandler](./vtmotionestimationoutputhandler.md)
  A block invoked by motion-estimation session when frame processing is complete.
- [VTMotionEstimationSessionCompleteFrames](./vtmotionestimationsessioncompleteframes.md)
  Directs the motion-estimation session to emit all pending frames and waits for completion.
- [VTMotionEstimationSessionCopySourcePixelBufferAttributes](./vtmotionestimationsessioncopysourcepixelbufferattributes.md)
  Copies the attributes for source pixel buffers expected by motion-estimation session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmotionestimationsessionestimatemotionvectors)*