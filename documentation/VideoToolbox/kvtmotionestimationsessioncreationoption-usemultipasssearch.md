# kVTMotionEstimationSessionCreationOption_UseMultiPassSearch

**Framework**: Video Toolbox  
**Kind**: var

An option to use for higher quality motion estimation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
let kVTMotionEstimationSessionCreationOption_UseMultiPassSearch: CFString!
```

#### Discussion

[`VTMotionEstimationSessionCreate`](vtmotionestimationsessioncreate.md) takes a dictionary of creation options, `motionVectorProcessorSelectionOptions`. You can supply [`kVTMotionEstimationSessionCreationOption_UseMultiPassSearch`](kvtmotionestimationsessioncreationoption_usemultipasssearch.md) with `kCFBooleanTrue` to provide higher quality motion estimation. True-motion achieves higher quality by running the motion estimator in multiple passes. The default is `kCFBooleanFalse`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtmotionestimationsessioncreationoption_usemultipasssearch)*