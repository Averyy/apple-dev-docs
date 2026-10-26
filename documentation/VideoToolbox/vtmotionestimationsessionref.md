# VTMotionEstimationSessionRef

**Framework**: Video Toolbox  
**Kind**: typealias  
**Role**: Type Alias

A reference to a Video Toolbox motion-estimation session.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```c
typedef struct OpaqueVTMotionEstimationSession * VTMotionEstimationSessionRef;
```

#### Discussion

A motion-estimation session supports two `CVPixelBuffer`s of the same size and type, and returns motion vectors in the form of a `CVPixelBuffer`. The session is a reference-counted CF object. To create a motion-estimation session, call [`VTMotionEstimationSessionCreate`](./vtmotionestimationsessioncreate.md); then you can optionally configure the session using `VTSessionSetProperty`. To create motion-estimations, call `VTMotionEstimationSessionCreateMotionEstimation`. When you are done with the session, you should call [`VTMotionEstimationSessionInvalidate`](./vtmotionestimationsessioninvalidate.md) to tear it down and `CFRelease` to release the session object reference.

## See Also

### Data types
- [VTMotionEstimationFrameFlags](./vtmotionestimationframeflags.md)
  Flags to control processing of a frame you pass to the motion-estimation session.
- [VTMotionEstimationInfoFlags](./vtmotionestimationinfoflags.md)
  Directives that provide information back to you with the results of motion-estimation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmotionestimationsessionref)*