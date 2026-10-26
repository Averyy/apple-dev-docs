# kVTMotionEstimationSessionCreationOption_UseMultiPassSearch

**Framework**: Video Toolbox  
**Kind**: var  
**Role**: Global Variable

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

```c
extern CFStringRef const kVTMotionEstimationSessionCreationOption_UseMultiPassSearch;
```

#### Discussion

[`VTMotionEstimationSessionCreate`](./vtmotionestimationsessioncreate.md) takes a dictionary of creation options, `motionVectorProcessorSelectionOptions`. You can supply [`kVTMotionEstimationSessionCreationOption_UseMultiPassSearch`](./kvtmotionestimationsessioncreationoption_usemultipasssearch.md) with `kCFBooleanTrue` to provide higher quality motion estimation. True-motion achieves higher quality by running the motion estimator in multiple passes. The default is `kCFBooleanFalse`.

## See Also

### Creating a session
- [class VTMotionEstimationSession](./vtmotionestimationsession.md)
- [let kVTMotionEstimationSessionCreationOption_Label: CFString!](./kvtmotionestimationsessioncreationoption_label.md)
  A label you use to log and track resources.
- [let kVTMotionEstimationSessionCreationOption_MotionVectorSize: CFString!](./kvtmotionestimationsessioncreationoption_motionvectorsize.md)
  The size of the search blocks that motion estimation session uses.
- [VTMotionEstimationSessionCreate](./vtmotionestimationsessioncreate.md)
  Creates a session you use to generate a pixel buffer of motion vectors from two pixel buffers.
- [kVTMotionEstimationSessionCreationOption_DetectTrueMotion](./kvtmotionestimationsessioncreationoption_detecttruemotion.md)
  Enable multi pass true motion detection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtmotionestimationsessioncreationoption_usemultipasssearch)*