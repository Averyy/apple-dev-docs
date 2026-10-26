# VTMotionEstimationFrameFlags

**Framework**: Video Toolbox  
**Kind**: enum  
**Role**: Enumeration

Flags to control processing of a frame you pass to the motion-estimation session.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```c
enum VTMotionEstimationFrameFlags : uint32_t;
```

## Topics

### Enumeration Cases
- [kVTMotionEstimationFrameFlags_CurrentBufferWillBeNextReferenceBuffer](./vtmotionestimationframeflags/kvtmotionestimationframeflags_currentbufferwillbenextreferencebuffer.md)
  A hint to the motion-estimation session that you are going to reuse the `currentBuffer` as `referenceBuffer` in the next call to [`VTMotionEstimationSessionEstimateMotionVectors`](./vtmotionestimationsessionestimatemotionvectors.md). Using this flag allows the motion-estimation processor to deliver better performance.

## See Also

### Data types
- [VTMotionEstimationSessionRef](./vtmotionestimationsessionref.md)
  A reference to a Video Toolbox motion-estimation session.
- [VTMotionEstimationInfoFlags](./vtmotionestimationinfoflags.md)
  Directives that provide information back to you with the results of motion-estimation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmotionestimationframeflags)*