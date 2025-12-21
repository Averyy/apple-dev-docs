# VTMotionEstimationOutputHandler

**Framework**: Video Toolbox  
**Kind**: typealias

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

#### Discussion

When the client requests a motion-estimation, the client passes in a callback block that the system invokes for the result of that request. If the `VTMotionEstimationSessionCreateMotionEstimation` call returns an error, the system does not invoke this block.

## Parameters

- `status`:   if processing request was successful; an error code if motion-estimation was not successful.
- `infoFlags`: A bit field that contains information about the processing operation.
- `additionalInfo`: Additional processing information about the operation that cannot fit in  .   Currently, the system expects this to be NULL.
- `motionVectorPixelBuffer`: A   that contains the motion vector information, if processing request   was successful; otherwise, NULL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmotionestimationoutputhandler)*