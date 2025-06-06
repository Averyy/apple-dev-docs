# TargetedImageRequestHandler

**Framework**: Vision  
**Kind**: class

An object that performs image-analysis requests on two images.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
final class TargetedImageRequestHandler
```

## Topics

### Creating a request handler
- [convenience init(sourceURL: URL, targetURL: URL, orientation: CGImagePropertyOrientation?)](targetedimagerequesthandler/init(sourceurl:targeturl:orientation:).md)
  Creates a handler for performing requests on an image at the specified URL.
- [convenience init(source: Data, target: Data, orientation: CGImagePropertyOrientation?)](targetedimagerequesthandler/init(source:target:orientation:)-4wr1c.md)
  Creates a handler for performing requests on an image contained in a data object.
- [convenience init(source: CGImage, target: CGImage, orientation: CGImagePropertyOrientation?)](targetedimagerequesthandler/init(source:target:orientation:)-66ft9.md)
  Creates a handler for performing requests on Core Graphics images.
- [convenience init(source: CVPixelBuffer, target: CVPixelBuffer, orientation: CGImagePropertyOrientation?)](targetedimagerequesthandler/init(source:target:orientation:)-64lxw.md)
  Creates a handler for performing requests on a Core Video pixel buffer.
- [convenience init(source: CMSampleBuffer, target: CMSampleBuffer, orientation: CGImagePropertyOrientation?)](targetedimagerequesthandler/init(source:target:orientation:)-9u6ta.md)
  Creates a request handler that performs requests on an image contained within a sample buffer.
- [convenience init(source: CIImage, target: CIImage, orientation: CGImagePropertyOrientation?)](targetedimagerequesthandler/init(source:target:orientation:)-1nk14.md)
  Creates a handler for performing requests on Core Image images.
### Performing the request
- [func perform<each T>(repeat each T) async throws -> (repeat (each T).Result)](targetedimagerequesthandler/perform(_:)-1i4di.md)
  Performs one or more framework requests on the handler’s image.
- [func perform<T>(T) async throws -> T.Result](targetedimagerequesthandler/perform(_:)-2r0k8.md)
  Performs a framework request on the handler’s image.
- [func performAll(some Collection<any TargetedRequest>) -> some AsyncSequence<VisionResult, Never>
](targetedimagerequesthandler/performall(_:).md)
  Schedules a collection of framework requests to perform on the handler’s image.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [class ImageRequestHandler](imagerequesthandler.md)
  An object that processes one or more image-analysis requests pertaining to a single image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/targetedimagerequesthandler)*