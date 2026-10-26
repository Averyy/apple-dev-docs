# kVTMotionEstimationFrameFlags_CurrentBufferWillBeNextReferenceBuffer

**Framework**: Video Toolbox  
**Kind**: case  
**Role**: Enumeration Case

A hint to the motion-estimation session that you are going to reuse the `currentBuffer` as `referenceBuffer` in the next call to [`VTMotionEstimationSessionEstimateMotionVectors`](../vtmotionestimationsessionestimatemotionvectors.md). Using this flag allows the motion-estimation processor to deliver better performance.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```c
kVTMotionEstimationFrameFlags_CurrentBufferWillBeNextReferenceBuffer
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmotionestimationframeflags/kvtmotionestimationframeflags_currentbufferwillbenextreferencebuffer)*