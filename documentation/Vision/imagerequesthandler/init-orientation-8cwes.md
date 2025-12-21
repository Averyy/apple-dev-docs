# init(_:orientation:)

**Framework**: Vision  
**Kind**: init

Creates a handler for performing requests on an image contained in a data object.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
convenience init(_ data: Data, orientation: CGImagePropertyOrientation? = nil)
```

## See Also

- [convenience init(URL, orientation: CGImagePropertyOrientation?)](imagerequesthandler/init(_:orientation:)-6imw8.md)
  Creates a handler for performing requests on an image at the specified URL.
- [convenience init(CGImage, orientation: CGImagePropertyOrientation?)](imagerequesthandler/init(_:orientation:)-8nodt.md)
  Creates a handler for performing requests on Core Graphics images.
- [convenience init(CVPixelBuffer, depthData: AVDepthData?, orientation: CGImagePropertyOrientation?)](imagerequesthandler/init(_:depthdata:orientation:)-3ebxg.md)
  Creates a handler for performing requests on a Core Video pixel buffer.
- [convenience init(CMSampleBuffer, depthData: AVDepthData?, orientation: CGImagePropertyOrientation?)](imagerequesthandler/init(_:depthdata:orientation:)-5itte.md)
  Creates a request handler that performs requests on an image contained within a sample buffer.
- [convenience init(CIImage, orientation: CGImagePropertyOrientation?)](imagerequesthandler/init(_:orientation:)-2hvfr.md)
  Creates a handler for performing requests on Core Image images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/imagerequesthandler/init(_:orientation:)-8cwes)*