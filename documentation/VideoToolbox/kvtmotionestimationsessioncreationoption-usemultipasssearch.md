# kVTMotionEstimationSessionCreationOption_UseMultiPassSearch

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
let kVTMotionEstimationSessionCreationOption_UseMultiPassSearch: CFString!
```

#### Discussion

```None
An option used for higher quality motion estimation
```

VTMotionEstimationSessionCreate takes a dictionary of creation options, motionVectorProcessorSelectionOptions. kVTMotionEstimationSessionCreationOption_UseMultiPassSearch can be supplied with kCFBooleanTrue to provide higher quality motion estimation. True motion achieves higher quality by running the motion estimator in multiple passes. The default is kCFBooleanFalse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtmotionestimationsessioncreationoption_usemultipasssearch)*