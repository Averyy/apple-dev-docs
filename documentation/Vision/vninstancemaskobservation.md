# VNInstanceMaskObservation

**Framework**: Vision  
**Kind**: class

An observation that contains an instance mask that labels instances in the mask.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class VNInstanceMaskObservation
```

## Topics

### Accessing Instances
- [var allInstances: IndexSet](vninstancemaskobservation/allinstances.md)
  The collection that contains all instances, excluding the background.
- [var instanceMask: CVPixelBuffer](vninstancemaskobservation/instancemask.md)
  The resulting mask that represents all instances.
### Creating a Mask
- [func generateMask(forInstances: IndexSet) throws -> CVPixelBuffer](vninstancemaskobservation/generatemask(forinstances:).md)
  Creates a low-resolution mask from the instances you specify.
- [func generateMaskedImage(ofInstances: IndexSet, from: VNImageRequestHandler, croppedToInstancesExtent: Bool) throws -> CVPixelBuffer](vninstancemaskobservation/generatemaskedimage(ofinstances:from:croppedtoinstancesextent:).md)
  Creates a high-resolution image where everything becomes transparent black, except for the instances you specify.
- [func generateScaledMaskForImage(forInstances: IndexSet, from: VNImageRequestHandler) throws -> CVPixelBuffer](vninstancemaskobservation/generatescaledmaskforimage(forinstances:from:).md)
  Creates a high-resolution mask where everything becomes transparent black, except for the instances you specify.

## Relationships

### Inherits From
- [VNObservation](vnobservation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [VNRequestRevisionProviding](vnrequestrevisionproviding.md)

## See Also

- [Applying visual effects to foreground subjects](applying-visual-effects-to-foreground-subjects.md)
  Segment the foreground subjects of an image and composite them to a new background with visual effects.
- [class VNGenerateForegroundInstanceMaskRequest](vngenerateforegroundinstancemaskrequest.md)
  A request that generates an instance mask of noticable objects to separate from the background.
- [let VNGenerateForegroundInstanceMaskRequestRevision1: Int](vngenerateforegroundinstancemaskrequestrevision1.md)
  A constant for specifying the first revision of the foreground instance mask request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vninstancemaskobservation)*