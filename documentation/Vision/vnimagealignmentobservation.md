# VNImageAlignmentObservation

**Framework**: Vision  
**Kind**: class

The abstract superclass for image-analysis results that describe the relative alignment of two images.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VNImageAlignmentObservation
```

#### Overview

This abstract superclass forms the basis of image alignment or registration output. You receive its subclasses, such as [`VNImageTranslationAlignmentObservation`](vnimagetranslationalignmentobservation.md) and [`VNImageHomographicAlignmentObservation`](vnimagehomographicalignmentobservation.md), by performing specific registration requests. Don’t create one of these classes yourself.

## Relationships

### Inherits From
- [VNObservation](vnobservation.md)
### Inherited By
- [VNImageHomographicAlignmentObservation](vnimagehomographicalignmentobservation.md)
- [VNImageTranslationAlignmentObservation](vnimagetranslationalignmentobservation.md)
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

- [Aligning Similar Images](aligning-similar-images.md)
  Construct a composite image from images that capture the same scene.
- [class VNTargetedImageRequest](vntargetedimagerequest.md)
  The abstract superclass for image analysis requests that operate on both the processed image and a secondary image.
- [class VNImageRegistrationRequest](vnimageregistrationrequest.md)
  The abstract superclass for image-analysis requests that align images according to their content.
- [class VNTranslationalImageRegistrationRequest](vntranslationalimageregistrationrequest.md)
  An image-analysis request that determines the affine transform necessary to align the content of two images.
- [class VNTrackTranslationalImageRegistrationRequest](vntracktranslationalimageregistrationrequest.md)
  An image-analysis request, as a stateful request you track over time, that determines the affine transform necessary to align the content of two images.
- [class VNHomographicImageRegistrationRequest](vnhomographicimageregistrationrequest.md)
  An image-analysis request that determines the perspective warp matrix necessary to align the content of two images.
- [class VNTrackHomographicImageRegistrationRequest](vntrackhomographicimageregistrationrequest.md)
  An image-analysis request, as a stateful request you track over time, that determines the perspective warp matrix necessary to align the content of two images.
- [class VNImageTranslationAlignmentObservation](vnimagetranslationalignmentobservation.md)
  Affine transform information that an image-alignment request produces.
- [class VNImageHomographicAlignmentObservation](vnimagehomographicalignmentobservation.md)
  An object that represents a perspective warp transformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnimagealignmentobservation)*