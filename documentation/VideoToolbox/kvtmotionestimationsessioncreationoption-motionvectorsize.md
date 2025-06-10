# kVTMotionEstimationSessionCreationOption_MotionVectorSize

**Framework**: Video Toolbox  
**Kind**: var

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
let kVTMotionEstimationSessionCreationOption_MotionVectorSize: CFString!
```

#### Discussion

```None
The size of the search blocks used in VTMotionEstimationSession.
```

VTMotionEstimationSessionCreate takes a dictionary of creation options, motionVectorProcessorSelectionOptions. kVTMotionEstimationSessionCreationOption_MotionVectorSize can be supplied with CFNumber to override the default search block size. Currently supported motion vector size is 4 or 16, meaning 4x4 or 16x16 respectively. 16x16 is the default if this key is not provided.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtmotionestimationsessioncreationoption_motionvectorsize)*