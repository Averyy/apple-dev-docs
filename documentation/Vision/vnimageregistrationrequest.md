# VNImageRegistrationRequest

**Framework**: Vision  
**Kind**: class

The abstract superclass for image-analysis requests that align images according to their content.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VNImageRegistrationRequest
```

#### Overview

This abstract superclass forms the basis of image alignment or registration requests. Make specific requests through one of its subclasses, [`VNTranslationalImageRegistrationRequest`](vntranslationalimageregistrationrequest.md) or [`VNHomographicImageRegistrationRequest`](vnhomographicimageregistrationrequest.md). Don’t create an instance of this superclass yourself.

## Relationships

### Inherits From
- [VNTargetedImageRequest](vntargetedimagerequest.md)
### Inherited By
- [VNHomographicImageRegistrationRequest](vnhomographicimageregistrationrequest.md)
- [VNTranslationalImageRegistrationRequest](vntranslationalimageregistrationrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Aligning Similar Images](aligning-similar-images.md)
  Construct a composite image from images that capture the same scene.
- [class VNTargetedImageRequest](vntargetedimagerequest.md)
  The abstract superclass for image analysis requests that operate on both the processed image and a secondary image.
- [class VNTranslationalImageRegistrationRequest](vntranslationalimageregistrationrequest.md)
  An image-analysis request that determines the affine transform necessary to align the content of two images.
- [class VNTrackTranslationalImageRegistrationRequest](vntracktranslationalimageregistrationrequest.md)
  An image-analysis request, as a stateful request you track over time, that determines the affine transform necessary to align the content of two images.
- [class VNHomographicImageRegistrationRequest](vnhomographicimageregistrationrequest.md)
  An image-analysis request that determines the perspective warp matrix necessary to align the content of two images.
- [class VNTrackHomographicImageRegistrationRequest](vntrackhomographicimageregistrationrequest.md)
  An image-analysis request, as a stateful request you track over time, that determines the perspective warp matrix necessary to align the content of two images.
- [class VNImageAlignmentObservation](vnimagealignmentobservation.md)
  The abstract superclass for image-analysis results that describe the relative alignment of two images.
- [class VNImageTranslationAlignmentObservation](vnimagetranslationalignmentobservation.md)
  Affine transform information that an image-alignment request produces.
- [class VNImageHomographicAlignmentObservation](vnimagehomographicalignmentobservation.md)
  An object that represents a perspective warp transformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnimageregistrationrequest)*