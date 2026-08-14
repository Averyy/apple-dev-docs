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

- [Detecting Human Body Poses in Images](detecting-human-body-poses-in-images.md)
- [Identifying 3D human body poses in images](identifying-3d-human-body-poses-in-images.md)
- [Recognizing Text in Images](recognizing-text-in-images.md)

#### Overview

Instantiate this handler to perform Vision requests on a single image. You specify the image and, optionally, a completion handler at the time of creation, and call [`perform(_:)`](vnimagerequesthandler/perform(_:).md) to begin executing the request.

## Topics

### Creating a Request Handler
- [init(CGImage: CGImage, options: [VNImageOption : Any])](vnimagerequesthandler/init(cgimage:options:)-5tp19.md)
- [init(cgImage: CGImage, options: [VNImageOption : Any])](vnimagerequesthandler/init(cgimage:options:)-4qda6.md)
  Creates a handler to be used for performing requests on Core Graphics images.
- [init(CGImage: CGImage, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](vnimagerequesthandler/init(cgimage:orientation:options:)-8imhf.md)
- [init(cgImage: CGImage, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](vnimagerequesthandler/init(cgimage:orientation:options:)-63ojm.md)
  Creates a handler to be used for performing requests on a Core Graphics image with known orientation.
- [init(CIImage: CIImage, options: [VNImageOption : Any])](vnimagerequesthandler/init(ciimage:options:)-55zel.md)
- [init(ciImage: CIImage, options: [VNImageOption : Any])](vnimagerequesthandler/init(ciimage:options:)-4wf33.md)
  Creates a handler to use for performing requests on Core Image image data.
- [init(CIImage: CIImage, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](vnimagerequesthandler/init(ciimage:orientation:options:)-8p8h1.md)
- [init(ciImage: CIImage, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](vnimagerequesthandler/init(ciimage:orientation:options:)-3svy6.md)
  Creates a handler to be used for performing requests on Core Image image data of a known orientation.
- [init(CVPixelBuffer: CVPixelBuffer, options: [VNImageOption : Any])](vnimagerequesthandler/init(cvpixelbuffer:options:)-3pee9.md)
- [init(cvPixelBuffer: CVPixelBuffer, options: [VNImageOption : Any])](vnimagerequesthandler/init(cvpixelbuffer:options:)-bkd7.md)
  Creates a handler for performing requests on a Core Video pixel buffer.
- [init(CVPixelBuffer: CVPixelBuffer, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](vnimagerequesthandler/init(cvpixelbuffer:orientation:options:)-160f.md)
- [init(cvPixelBuffer: CVPixelBuffer, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](vnimagerequesthandler/init(cvpixelbuffer:orientation:options:)-9fxug.md)
  Creates a handler for performing requests on a Core Video pixel buffer of a known orientation.
- [init(CVPixelBuffer: CVPixelBuffer, depthData: AVDepthData, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](vnimagerequesthandler/init(cvpixelbuffer:depthdata:orientation:options:)-3u960.md)
- [init(cvPixelBuffer: CVPixelBuffer, depthData: AVDepthData, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](vnimagerequesthandler/init(cvpixelbuffer:depthdata:orientation:options:)-3mj2d.md)
- [init(CMSampleBuffer: CMSampleBuffer, options: [VNImageOption : Any])](vnimagerequesthandler/init(cmsamplebuffer:options:)-4mpwd.md)
- [init(cmSampleBuffer: CMSampleBuffer, options: [VNImageOption : Any])](vnimagerequesthandler/init(cmsamplebuffer:options:)-2yodn.md)
  Creates a request handler that performs requests on an image contained within a sample buffer.
- [init(CMSampleBuffer: CMSampleBuffer, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](vnimagerequesthandler/init(cmsamplebuffer:orientation:options:)-6qeht.md)
- [init(cmSampleBuffer: CMSampleBuffer, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](vnimagerequesthandler/init(cmsamplebuffer:orientation:options:)-335k4.md)
  Creates a request handler that performs requests on an image of a specified orientation contained within a sample buffer.
- [init(CMSampleBuffer: CMSampleBuffer, depthData: AVDepthData, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](vnimagerequesthandler/init(cmsamplebuffer:depthdata:orientation:options:)-yi6q.md)
- [init(cmSampleBuffer: CMSampleBuffer, depthData: AVDepthData, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](vnimagerequesthandler/init(cmsamplebuffer:depthdata:orientation:options:)-8bjyh.md)
  Creates a request handler that performs requests on an image in a sample buffer that contains depth data.
- [init(data: Data, options: [VNImageOption : Any])](vnimagerequesthandler/init(data:options:).md)
  Creates a handler to use for performing requests on an image in a data object.
- [init(data: Data, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](vnimagerequesthandler/init(data:orientation:options:).md)
  Creates a handler to use for performing requests on an image of known orientation.
- [init(URL: URL, options: [VNImageOption : Any])](vnimagerequesthandler/init(url:options:)-19t0u.md)
- [init(url: URL, options: [VNImageOption : Any])](vnimagerequesthandler/init(url:options:)-4k623.md)
  Creates a handler to be used for performing requests on an image at the specified URL.
- [init(URL: URL, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](vnimagerequesthandler/init(url:orientation:options:)-ou7m.md)
- [init(url: URL, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](vnimagerequesthandler/init(url:orientation:options:)-70nta.md)
  Creates a handler to be used for performing requests on an image with known orientation, at the specified URL.
### Executing a Request Handler
- [func perform([VNRequest]) throws](vnimagerequesthandler/perform(_:).md)
  Schedules Vision requests to perform.
### Setting Image Options
- [struct VNImageOption](vnimageoption.md)
  An option key passed into an image request handler that takes an auxiliary image.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

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