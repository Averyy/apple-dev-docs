# VTMotionEstimationOutputHandler

**Framework**: Video Toolbox  
**Kind**: typealias

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

When the client requests a motion estimation, the client passes in a callback block to be called for that result of that request. If the VTMotionEstimationSessionCreateMotionEstimation call returns an error, the block will not be called.

## Parameters

- `status`: noErr if processing request was successful; an error code if motion estimation was not successful.
- `infoFlags`: A bit field containing information about the processing operation.
- `additionalInfo`: Additional processing information about the processing operation that can not fit in infoFlags.   Currently, this is expected to be NULL.
- `motionVectorPixelBuffer`: A CVPixelBuffer containing the motion vector information, if processing request was successful;   otherwise, NULL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmotionestimationoutputhandler)*