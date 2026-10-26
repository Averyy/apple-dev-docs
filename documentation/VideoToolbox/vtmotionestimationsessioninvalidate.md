# VTMotionEstimationSessionInvalidate

**Framework**: Video Toolbox  
**Kind**: func  
**Role**: Function

Tears down a motion-estimation session.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```c
extern void VTMotionEstimationSessionInvalidate(VTMotionEstimationSessionRef session);
```

#### Discussion

When you are done with a motion-estimation session you created, call this function to tear it down and then `CFRelease` to release the session object reference. When a motion-estimation session’s retain count reaches zero, the system automatically invalidates it, but because multiple parties may retain sessions, it can be hard to predict when this happens. Calling this function ensures a deterministic, orderly teardown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmotionestimationsessioninvalidate)*