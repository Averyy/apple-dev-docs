# VNTargetedImageRequest

**Framework**: Vision  
**Kind**: class  
**Role**: Class

The abstract superclass for image analysis requests that operate on both the processed image and a secondary image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VNTargetedImageRequest
```

```objc
@interface VNTargetedImageRequest : VNImageBasedRequest
```

## Overview

Other Vision request handlers that operate on both the processed image and a secondary image inherit from this abstract base class. Instantiate one of its subclasses to perform image analysis, and pass in auxiliary image data by filling in the `options` dictionary at initialization.

## Topics

### Creating a Request
- [init(targetedCGImage: CGImage, options: [VNImageOption : Any], completionHandler: VNRequestCompletionHandler?)](./vntargetedimagerequest/init%28targetedcgimage,options,completionhandler%29.md)
  Creates a new request targeting a Core Graphics image, executing the completion handler when done.
- [init(targetedCGImage: CGImage, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any], completionHandler: VNRequestCompletionHandler?)](./vntargetedimagerequest/init%28targetedcgimage,orientation,options,completionhandler%29.md)
  Creates a new request targeting a Core Graphics image of known orientation, executing the completion handler when done.
- [init(targetedCIImage: CIImage, options: [VNImageOption : Any], completionHandler: VNRequestCompletionHandler?)](./vntargetedimagerequest/init%28targetedciimage,options,completionhandler%29.md)
  Creates a new request targeting a Core Image image.
- [init(targetedCIImage: CIImage, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any], completionHandler: VNRequestCompletionHandler?)](./vntargetedimagerequest/init%28targetedciimage,orientation,options,completionhandler%29.md)
  Creates a new request targeting a Core Image image of known orientation, executing the completion handler when done.
- [init(targetedCVPixelBuffer: CVPixelBuffer, options: [VNImageOption : Any], completionHandler: VNRequestCompletionHandler?)](./vntargetedimagerequest/init%28targetedcvpixelbuffer,options,completionhandler%29.md)
  Creates a new request targeting an image in a pixel buffer.
- [init(targetedCVPixelBuffer: CVPixelBuffer, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any], completionHandler: VNRequestCompletionHandler?)](./vntargetedimagerequest/init%28targetedcvpixelbuffer,orientation,options,completionhandler%29.md)
  Creates a new request targeting an image in a pixel buffer of known orientation.
- [init(targetedCMSampleBuffer: CMSampleBuffer, options: [VNImageOption : Any], completionHandler: VNRequestCompletionHandler?)](./vntargetedimagerequest/init%28targetedcmsamplebuffer,options,completionhandler%29.md)
  Creates a new request with a completion handler that targets an image in a sample buffer.
- [init(targetedCMSampleBuffer: CMSampleBuffer, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any], completionHandler: VNRequestCompletionHandler?)](./vntargetedimagerequest/init%28targetedcmsamplebuffer,orientation,options,completionhandler%29.md)
  Creates a new request with a completion handler that targets an image of a known orientation in a sample buffer.
- [init(targetedImageData: Data, options: [VNImageOption : Any], completionHandler: VNRequestCompletionHandler?)](./vntargetedimagerequest/init%28targetedimagedata,options,completionhandler%29.md)
  Creates a new request targeting an image as raw data, executing the completion handler when done.
- [init(targetedImageData: Data, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any], completionHandler: VNRequestCompletionHandler?)](./vntargetedimagerequest/init%28targetedimagedata,orientation,options,completionhandler%29.md)
  Creates a new request targeting a raw data image of known orientation, executing the completion handler when done.
- [init(targetedImageURL: URL, options: [VNImageOption : Any], completionHandler: VNRequestCompletionHandler?)](./vntargetedimagerequest/init%28targetedimageurl,options,completionhandler%29.md)
  Creates a new request targeting an image at the specified URL, executing the completion handler when done.
- [init(targetedImageURL: URL, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any], completionHandler: VNRequestCompletionHandler?)](./vntargetedimagerequest/init%28targetedimageurl,orientation,options,completionhandler%29.md)
  Creates a new request targeting an image of known orientation, at the specified URL, executing the completion handler when done.
- [- initWithTargetedCGImage:options:](./vntargetedimagerequest/initwithtargetedcgimage_options_.md)
  Creates a new request targeting a Core Graphics image.
- [- initWithTargetedCGImage:orientation:options:](./vntargetedimagerequest/initwithtargetedcgimage_orientation_options_.md)
  Creates a new request targeting a Core Graphics image of known orientation.
- [- initWithTargetedCIImage:options:](./vntargetedimagerequest/initwithtargetedciimage_options_.md)
  Creates a new request targeting a Core Image image.
- [- initWithTargetedCIImage:orientation:options:](./vntargetedimagerequest/initwithtargetedciimage_orientation_options_.md)
  Creates a new request targeting a Core Image image of known orientation.
- [- initWithTargetedCVPixelBuffer:options:](./vntargetedimagerequest/initwithtargetedcvpixelbuffer_options_.md)
  Creates a new request targeting an image in a pixel buffer.
- [- initWithTargetedCVPixelBuffer:orientation:options:](./vntargetedimagerequest/initwithtargetedcvpixelbuffer_orientation_options_.md)
  Creates a new request targeting an image in a pixel buffer of known orientation.
- [- initWithTargetedCMSampleBuffer:options:](./vntargetedimagerequest/initwithtargetedcmsamplebuffer_options_.md)
  Creates a new request that targets an image in a sample buffer.
- [- initWithTargetedCMSampleBuffer:orientation:options:](./vntargetedimagerequest/initwithtargetedcmsamplebuffer_orientation_options_.md)
  Creates a new request that targets an image of a known orientation in a sample buffer.
- [- initWithTargetedImageData:options:](./vntargetedimagerequest/initwithtargetedimagedata_options_.md)
  Creates a new request targeting an image as raw data.
- [- initWithTargetedImageData:orientation:options:](./vntargetedimagerequest/initwithtargetedimagedata_orientation_options_.md)
  Creates a new request targeting a raw data image of known orientation.
- [- initWithTargetedImageURL:options:](./vntargetedimagerequest/initwithtargetedimageurl_options_.md)
  Creates a new request targeting an image at the specified URL.
- [- initWithTargetedImageURL:orientation:options:](./vntargetedimagerequest/initwithtargetedimageurl_orientation_options_.md)
  Creates a new request targeting an image of known orientation, at the specified URL.

## Relationships

### Inherits From
- [VNImageBasedRequest](./vnimagebasedrequest.md)
### Inherited By
- [VNGenerateOpticalFlowRequest](./vngenerateopticalflowrequest.md)
- [VNImageRegistrationRequest](./vnimageregistrationrequest.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Image alignment
- [Aligning Similar Images](./aligning-similar-images.md)
  Construct a composite image from images that capture the same scene.
- [class VNImageRegistrationRequest](./vnimageregistrationrequest.md)
  The abstract superclass for image-analysis requests that align images according to their content.
- [class VNTranslationalImageRegistrationRequest](./vntranslationalimageregistrationrequest.md)
  An image-analysis request that determines the affine transform necessary to align the content of two images.
- [class VNTrackTranslationalImageRegistrationRequest](./vntracktranslationalimageregistrationrequest.md)
  An image-analysis request, as a stateful request you track over time, that determines the affine transform necessary to align the content of two images.
- [class VNHomographicImageRegistrationRequest](./vnhomographicimageregistrationrequest.md)
  An image-analysis request that determines the perspective warp matrix necessary to align the content of two images.
- [class VNTrackHomographicImageRegistrationRequest](./vntrackhomographicimageregistrationrequest.md)
  An image-analysis request, as a stateful request you track over time, that determines the perspective warp matrix necessary to align the content of two images.
- [class VNImageAlignmentObservation](./vnimagealignmentobservation.md)
  The abstract superclass for image-analysis results that describe the relative alignment of two images.
- [class VNImageTranslationAlignmentObservation](./vnimagetranslationalignmentobservation.md)
  Affine transform information that an image-alignment request produces.
- [class VNImageHomographicAlignmentObservation](./vnimagehomographicalignmentobservation.md)
  An object that represents a perspective warp transformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntargetedimagerequest)*