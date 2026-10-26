# kVTMotionEstimationSessionCreationOption_Label

**Framework**: Video Toolbox  
**Kind**: var  
**Role**: Global Variable

A label you use to log and track resources.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
let kVTMotionEstimationSessionCreationOption_Label: CFString!
```

```c
extern CFStringRef const kVTMotionEstimationSessionCreationOption_Label;
```

#### Discussion

[`VTMotionEstimationSessionCreate`](./vtmotionestimationsessioncreate.md) takes a dictionary of creation options, `motionVectorProcessorSelectionOptions`. You can supply [`kVTMotionEstimationSessionCreationOption_Label`](./kvtmotionestimationsessioncreationoption_label.md) with `CFString` to specify a label used in logging and resource tracking.

## See Also

### Creating a session
- [class VTMotionEstimationSession](./vtmotionestimationsession.md)
- [let kVTMotionEstimationSessionCreationOption_MotionVectorSize: CFString!](./kvtmotionestimationsessioncreationoption_motionvectorsize.md)
  The size of the search blocks that motion estimation session uses.
- [let kVTMotionEstimationSessionCreationOption_UseMultiPassSearch: CFString!](./kvtmotionestimationsessioncreationoption_usemultipasssearch.md)
  An option to use for higher quality motion estimation.
- [VTMotionEstimationSessionCreate](./vtmotionestimationsessioncreate.md)
  Creates a session you use to generate a pixel buffer of motion vectors from two pixel buffers.
- [kVTMotionEstimationSessionCreationOption_DetectTrueMotion](./kvtmotionestimationsessioncreationoption_detecttruemotion.md)
  Enable multi pass true motion detection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtmotionestimationsessioncreationoption_label)*