# init(_:orientation:)

**Framework**: Vision  
**Kind**: init

Creates a handler for performing requests on Core Image images.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
convenience init(_ image: CIImage, orientation: CGImagePropertyOrientation? = nil)
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/imagerequesthandler/init(_:orientation:)-2hvfr)*