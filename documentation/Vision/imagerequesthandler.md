# ImageRequestHandler

**Framework**: Vision  
**Kind**: class

An object that processes one or more image-analysis requests pertaining to a single image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
final class ImageRequestHandler
```

#### Overview

Instantiate this handler to perform Vision requests on a single image. You specify the image, and then call [`perform(_:)`](imagerequesthandler/perform(_:)-7b6g5.md) to begin executing the request.

## Topics

### Creating a request handler
- [convenience init(URL, orientation: CGImagePropertyOrientation?)](imagerequesthandler/init(_:orientation:)-6imw8.md)
  Creates a handler for performing requests on an image at the specified URL.
- [convenience init(Data, orientation: CGImagePropertyOrientation?)](imagerequesthandler/init(_:orientation:)-8cwes.md)
  Creates a handler for performing requests on an image contained in a data object.
- [convenience init(CGImage, orientation: CGImagePropertyOrientation?)](imagerequesthandler/init(_:orientation:)-8nodt.md)
  Creates a handler for performing requests on Core Graphics images.
- [convenience init(CVPixelBuffer, depthData: AVDepthData?, orientation: CGImagePropertyOrientation?)](imagerequesthandler/init(_:depthdata:orientation:)-3ebxg.md)
  Creates a handler for performing requests on a Core Video pixel buffer.
- [convenience init(CMSampleBuffer, depthData: AVDepthData?, orientation: CGImagePropertyOrientation?)](imagerequesthandler/init(_:depthdata:orientation:)-5itte.md)
  Creates a request handler that performs requests on an image contained within a sample buffer.
- [convenience init(CIImage, orientation: CGImagePropertyOrientation?)](imagerequesthandler/init(_:orientation:)-2hvfr.md)
  Creates a handler for performing requests on Core Image images.
### Performing the request
- [func perform<each T>(repeat each T) async throws -> (repeat (each T).Result)](imagerequesthandler/perform(_:)-l6er.md)
  Performs one or more framework requests on the handler’s image.
- [func perform<T>(T) async throws -> T.Result](imagerequesthandler/perform(_:)-7b6g5.md)
  Performs a framework request on the handler’s image.
- [func performAll(some Collection<any VisionRequest>) -> some AsyncSequence<VisionResult, Never>
](imagerequesthandler/performall(_:).md)
  Schedules a collection of framework requests to perform on the handler’s image.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Classifying images for categorization and search](classifying-images-for-categorization-and-search.md)
  Analyze and label images using a Vision classification request.
- [struct ClassifyImageRequest](classifyimagerequest.md)
  A request to classify an image.
- [protocol ImageProcessingRequest](imageprocessingrequest.md)
  A type for image-analysis requests that focus on a specific part of an image.
- [protocol VisionRequest](visionrequest.md)
  A type for image-analysis requests.
- [protocol VisionObservation](visionobservation.md)
  A type for objects produced by image-analysis requests.
- [struct DetectLensSmudgeRequest](detectlenssmudgerequest.md)
  A request that detects a smudge on a lens from an image or video frame capture.
- [struct SmudgeObservation](smudgeobservation.md)
  An observation that provides an overall score of the presence of a smudge in an image or video frame capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/imagerequesthandler)*