# ImageRequestHandler

**Framework**: Vision  
**Kind**: class  
**Role**: Class

An object that processes one or more image-analysis requests pertaining to a single image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+

## Declaration

```swift
final class ImageRequestHandler
```

## Mentions

- [Isolating an object from a tap, box, or scribble](./segmenting-objects-with-iterative-refinement.md)

#### Overview

Instantiate this handler to perform Vision requests on a single image. You specify the image, and then call [`perform(_:)`](./imagerequesthandler/perform%28_%29-7b6g5.md) to begin executing the request.

## Topics

### Creating a request handler
- [convenience init(URL, orientation: CGImagePropertyOrientation?)](./imagerequesthandler/init%28_,orientation%29-6imw8.md)
  Creates a handler for performing requests on an image at the specified URL.
- [convenience init(Data, orientation: CGImagePropertyOrientation?)](./imagerequesthandler/init%28_,orientation%29-8cwes.md)
  Creates a handler for performing requests on an image contained in a data object.
- [convenience init(CGImage, orientation: CGImagePropertyOrientation?)](./imagerequesthandler/init%28_,orientation%29-8nodt.md)
  Creates a handler for performing requests on Core Graphics images.
- [convenience init(CVPixelBuffer, depthData: AVDepthData?, orientation: CGImagePropertyOrientation?)](./imagerequesthandler/init%28_,depthdata,orientation%29-3ebxg.md)
  Creates a handler for performing requests on a Core Video pixel buffer.
- [convenience init(CMSampleBuffer, depthData: AVDepthData?, orientation: CGImagePropertyOrientation?)](./imagerequesthandler/init%28_,depthdata,orientation%29-5itte.md)
  Creates a request handler that performs requests on an image contained within a sample buffer.
- [convenience init(CIImage, orientation: CGImagePropertyOrientation?)](./imagerequesthandler/init%28_,orientation%29-2hvfr.md)
  Creates a handler for performing requests on Core Image images.
- [convenience init(CVPixelBuffer, orientation: CGImagePropertyOrientation?)](./imagerequesthandler/init%28_,orientation%29-3zrh5.md)
- [convenience init(CMSampleBuffer, orientation: CGImagePropertyOrientation?)](./imagerequesthandler/init%28_,orientation%29-8q7vz.md)
### Performing the request
- [func perform<each T>(repeat each T) async throws -> (repeat (each T).Result)](./imagerequesthandler/perform%28_%29-l6er.md)
  Performs one or more framework requests on the handler’s image.
- [func perform<T>(T) async throws -> T.Result](./imagerequesthandler/perform%28_%29-7b6g5.md)
  Performs a framework request on the handler’s image.
- [func performAll(some Collection<any VisionRequest>) -> some AsyncSequence<VisionResult, Never>
](./imagerequesthandler/performall%28_%29.md)
  Schedules a collection of framework requests to perform on the handler’s image.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Request handlers
- [class TargetedImageRequestHandler](./targetedimagerequesthandler.md)
  An object that performs image-analysis requests on two images.
- [class VideoProcessor](./videoprocessor.md)
  An object that performs offline analysis of video content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/imagerequesthandler)*