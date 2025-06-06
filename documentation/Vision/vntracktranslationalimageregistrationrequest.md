# VNTrackTranslationalImageRegistrationRequest

**Framework**: Vision  
**Kind**: class

An image-analysis request, as a stateful request you track over time, that determines the affine transform necessary to align the content of two images.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class VNTrackTranslationalImageRegistrationRequest
```

#### Overview

This request is similar to [`VNTranslationalImageRegistrationRequest`](vntranslationalimageregistrationrequest.md). However, as a [`VNStatefulRequest`](vnstatefulrequest.md), it automatically computes the registration against the previous frame.

## Topics

### Creating a Translational Image
- [init()](vntracktranslationalimageregistrationrequest/init.md)
  Creates a new request that tracks the translational registration of two images.
- [init(completionHandler: VNRequestCompletionHandler?)](vntracktranslationalimageregistrationrequest/init(completionhandler:).md)
  Creates a new request that tracks the translational registration of two images, with a system callback on completion.
### Accessing the Results
- [var results: [VNImageTranslationAlignmentObservation]?](vntracktranslationalimageregistrationrequest/results.md)
  The observed translational image alignment request.

## Relationships

### Inherits From
- [VNStatefulRequest](vnstatefulrequest.md)
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
- [class VNImageRegistrationRequest](vnimageregistrationrequest.md)
  The abstract superclass for image-analysis requests that align images according to their content.
- [class VNTranslationalImageRegistrationRequest](vntranslationalimageregistrationrequest.md)
  An image-analysis request that determines the affine transform necessary to align the content of two images.
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

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntracktranslationalimageregistrationrequest)*