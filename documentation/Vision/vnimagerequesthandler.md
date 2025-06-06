# VNImageRequestHandler

**Framework**: Vision  
**Kind**: class

An object that processes one or more image-analysis request pertaining to a single image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VNImageRequestHandler
```

## Mentions

- [Recognizing Text in Images](recognizing-text-in-images.md)
- [Identifying 3D human body poses in images](identifying-3d-human-body-poses-in-images.md)
- [Detecting Human Body Poses in Images](detecting-human-body-poses-in-images.md)

#### Overview

Instantiate this handler to perform Vision requests on a single image. You specify the image and, optionally, a completion handler at the time of creation, and call [`perform(_:)`](vnimagerequesthandler/perform(_:).md) to begin executing the request.

## Topics

### Creating a Request Handler
- [init(cgImage: CGImage, options: [VNImageOption : Any])](vnimagerequesthandler/init(cgimage:options:).md)
  Creates a handler to be used for performing requests on Core Graphics images.
- [init(cgImage: CGImage, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](vnimagerequesthandler/init(cgimage:orientation:options:).md)
  Creates a handler to be used for performing requests on a Core Graphics image with known orientation.
- [init(ciImage: CIImage, options: [VNImageOption : Any])](vnimagerequesthandler/init(ciimage:options:).md)
  Creates a handler to use for performing requests on Core Image image data.
- [init(ciImage: CIImage, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](vnimagerequesthandler/init(ciimage:orientation:options:).md)
  Creates a handler to be used for performing requests on Core Image image data of a known orientation.
- [init(cvPixelBuffer: CVPixelBuffer, options: [VNImageOption : Any])](vnimagerequesthandler/init(cvpixelbuffer:options:).md)
  Creates a handler for performing requests on a Core Video pixel buffer.
- [init(cvPixelBuffer: CVPixelBuffer, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](vnimagerequesthandler/init(cvpixelbuffer:orientation:options:).md)
  Creates a handler for performing requests on a Core Video pixel buffer of a known orientation.
- [init(cvPixelBuffer: CVPixelBuffer, depthData: AVDepthData, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](vnimagerequesthandler/init(cvpixelbuffer:depthdata:orientation:options:).md)
- [init(cmSampleBuffer: CMSampleBuffer, options: [VNImageOption : Any])](vnimagerequesthandler/init(cmsamplebuffer:options:).md)
  Creates a request handler that performs requests on an image contained within a sample buffer.
- [init(cmSampleBuffer: CMSampleBuffer, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](vnimagerequesthandler/init(cmsamplebuffer:orientation:options:).md)
  Creates a request handler that performs requests on an image of a specified orientation contained within a sample buffer.
- [init(cmSampleBuffer: CMSampleBuffer, depthData: AVDepthData, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](vnimagerequesthandler/init(cmsamplebuffer:depthdata:orientation:options:).md)
  Creates a request handler that performs requests on an image in a sample buffer that contains depth data.
- [init(data: Data, options: [VNImageOption : Any])](vnimagerequesthandler/init(data:options:).md)
  Creates a handler to use for performing requests on an image in a data object.
- [init(data: Data, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](vnimagerequesthandler/init(data:orientation:options:).md)
  Creates a handler to use for performing requests on an image of known orientation.
- [init(url: URL, options: [VNImageOption : Any])](vnimagerequesthandler/init(url:options:).md)
  Creates a handler to be used for performing requests on an image at the specified URL.
- [init(url: URL, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](vnimagerequesthandler/init(url:orientation:options:).md)
  Creates a handler to be used for performing requests on an image with known orientation, at the specified URL.
### Executing a Request Handler
- [func perform([VNRequest]) throws](vnimagerequesthandler/perform(_:).md)
  Schedules Vision requests to perform.
### Setting Image Options
- [struct VNImageOption](vnimageoption.md)
  An option key passed into an image request handler that takes an auxiliary image.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Detecting Objects in Still Images](detecting-objects-in-still-images.md)
  Locate and demarcate rectangles, faces, barcodes, and text in images using the Vision framework.
- [Classifying images for categorization and search](classifying-images-for-categorization-and-search.md)
  Analyze and label images using a Vision classification request.
- [Analyzing Image Similarity with Feature Print](analyzing-image-similarity-with-feature-print.md)
  Generate a feature print to compute distance between images.
- [class VNRequest](vnrequest.md)
  The abstract superclass for analysis requests.
- [class VNImageBasedRequest](vnimagebasedrequest.md)
  The abstract superclass for image-analysis requests that focus on a specific part of an image.
- [class VNClassifyImageRequest](vnclassifyimagerequest.md)
  A request to classify an image.
- [class VNGenerateImageFeaturePrintRequest](vngenerateimagefeatureprintrequest.md)
  An image-based request to generate feature prints from an image.
- [class VNFeaturePrintObservation](vnfeatureprintobservation.md)
  An observation that provides the recognized feature print.
- [class VNObservation](vnobservation.md)
  The abstract superclass for analysis results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnimagerequesthandler)*