# Aligning Similar Images

**Framework**: Vision

Construct a composite image from images that capture the same scene.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- Xcode 12.4+

#### Overview

This sample app uses image registration requests from the Vision framework to calculate an alignment transform between two images of the same scene that are slightly different. The sample app uses the alignment transform to construct a single, composite image that contains the aligned content of both images.

##### Provide Input Images

Image registration requests require two images, a reference image and a floating image. The best alignment occurs when the content of the input images is very similar. In this sample app, the input images simulate an image capture of the same scene from a slightly different perspective. The two images are nearly identical — one has a slight warp and is offset from the other. The sample app displays the input images next to the aligned composite image for visual comparison in the `registrationImages` view.

##### Select a Registration Mechanism

The Vision framework provides a translational image registration mechanism, [`VNTranslationalImageRegistrationRequest`](https://developer.apple.comhttps://developer.apple.com/documentation/vision/vntranslationalimageregistrationrequest), and a homographic image registration mechanism, [`VNHomographicImageRegistrationRequest`](https://developer.apple.comhttps://developer.apple.com/documentation/vision/vnhomographicimageregistrationrequest). The sample app provides a toggle between these two image registration mechanisms to visually demonstrate the differences in their image alignment observations.

##### Apply the Alignment Observation

This project applies the alignment observation for each image registration mechanism in the `register` function, and returns an image that contains the composited result. The `register` function uses the `makeAlignedImage` function to transform the floating image.  The sample uses the [`transformed(by:)`](https://developer.apple.comhttps://developer.apple.com/documentation/coreimage/ciimage/1438203-transformed) method to apply the translational transform for the translational image registration mechanism, and uses the [`CIPerspectiveTransform`](https://developer.apple.comhttps://developer.apple.com/documentation/coreimage/ciperspectivetransform) filter to apply the pespective transform for the homographic image registration mechanism.

## See Also

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
- [class VNImageAlignmentObservation](vnimagealignmentobservation.md)
  The abstract superclass for image-analysis results that describe the relative alignment of two images.
- [class VNImageTranslationAlignmentObservation](vnimagetranslationalignmentobservation.md)
  Affine transform information that an image-alignment request produces.
- [class VNImageHomographicAlignmentObservation](vnimagehomographicalignmentobservation.md)
  An object that represents a perspective warp transformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/aligning-similar-images)*