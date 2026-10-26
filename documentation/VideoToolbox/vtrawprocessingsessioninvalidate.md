# VTRAWProcessingSessionInvalidate

**Framework**: Video Toolbox  
**Kind**: func  
**Role**: Function

Tears down a RAW processing session.

**Availability**:
- macOS 15.0+

## Declaration

```c
extern void VTRAWProcessingSessionInvalidate(VTRAWProcessingSessionRef session);
```

#### Discussion

When you are done with a RAW processing session you created, call this function to tear it down and then `CFRelease` to release your object reference. When a  session’s retain count reaches zero, it is automatically invalidated, but since sessions may be retained by multiple parties, it can be hard to predict when this will happen.

Calling this function ensures a deterministic, orderly teardown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtrawprocessingsessioninvalidate)*