# PartRenderer.PartParameters

**Framework**: hvf  
**Kind**: class  
**Role**: Class

All the parameters applied to a part, including nested subparts

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
class PartParameters
```

## Topics

### Instance Properties
- [var axisValues: PartRenderer.AxisValues](./partparameters/axisvalues.md)
  The axis values applied to the part
- [var blendedRotation: Double](./partparameters/blendedrotation.md)
  After rendering, the blended rotation applied to the part
- [var blendedTranslation: PartRenderer.Translation](./partparameters/blendedtranslation.md)
  After rendering, the blended translation applied to the part
- [let partIndex: Int](./partparameters/partindex.md)
  The part index of the part these parameters refer to
- [var rotation: Double](./partparameters/rotation.md)
  The rotation applied to the part, counterclockwise, in radians
- [var subparts: PartRenderer.Subparts](./partparameters/subparts.md)
  Collection of PartParameters applied to subparts of the part (if any)
- [var translation: PartRenderer.Translation](./partparameters/translation.md)
  The translation applied to the part


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf/partrenderer/partparameters)*