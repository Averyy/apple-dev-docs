# kVTMotionEstimationSessionCreationOption_MotionVectorSize

**Framework**: Video Toolbox  
**Kind**: var

The size of the search blocks that motion estimation session uses.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
let kVTMotionEstimationSessionCreationOption_MotionVectorSize: CFString!
```

#### Discussion

[`VTMotionEstimationSessionCreate`](vtmotionestimationsessioncreate.md) takes a dictionary of creation options, `motionVectorProcessorSelectionOptions`. You can supply [`kVTMotionEstimationSessionCreationOption_MotionVectorSize`](kvtmotionestimationsessioncreationoption_motionvectorsize.md) with `CFNumber` to override the default search block size. Supported motion vector size is 4 or 16, meaning 4x4 or 16x16 respectively. 16x16 is the default if you don’t provide this key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtmotionestimationsessioncreationoption_motionvectorsize)*