# kVTMotionEstimationSessionCreationOption_MotionVectorSize

**Framework**: Video Toolbox  
**Kind**: var  
**Role**: Global Variable

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

```c
extern CFStringRef const kVTMotionEstimationSessionCreationOption_MotionVectorSize;
```

## Discussion

[`VTMotionEstimationSessionCreate`](./vtmotionestimationsessioncreate.md) takes a dictionary of creation options, `motionVectorProcessorSelectionOptions`. You can supply [`kVTMotionEstimationSessionCreationOption_MotionVectorSize`](./kvtmotionestimationsessioncreationoption_motionvectorsize.md) with `CFNumber` to override the default search block size. Supported motion vector size is 4 or 16, meaning 4x4 or 16x16 respectively. 16x16 is the default if you don’t provide this key.

## See Also

### Creating a session
- [class VTMotionEstimationSession](./vtmotionestimationsession.md)
- [let kVTMotionEstimationSessionCreationOption_Label: CFString!](./kvtmotionestimationsessioncreationoption_label.md)
  A label you use to log and track resources.
- [let kVTMotionEstimationSessionCreationOption_UseMultiPassSearch: CFString!](./kvtmotionestimationsessioncreationoption_usemultipasssearch.md)
  An option to use for higher quality motion estimation.
- [VTMotionEstimationSessionCreate](./vtmotionestimationsessioncreate.md)
  Creates a session you use to generate a pixel buffer of motion vectors from two pixel buffers.
- [kVTMotionEstimationSessionCreationOption_DetectTrueMotion](./kvtmotionestimationsessioncreationoption_detecttruemotion.md)
  Enable multi pass true motion detection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtmotionestimationsessioncreationoption_motionvectorsize)*