# init(_:depthData:orientation:)

**Framework**: Vision  
**Kind**: init  
**Role**: Initializer

Creates a handler for performing requests on a Core Video pixel buffer.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
convenience init(_ pixelBuffer: CVPixelBuffer, depthData: AVDepthData? = nil, orientation: CGImagePropertyOrientation? = nil)
```

## See Also

### Creating a request handler
- [convenience init(URL, orientation: CGImagePropertyOrientation?)](./init%28_,orientation%29-6imw8.md)
  Creates a handler for performing requests on an image at the specified URL.
- [convenience init(Data, orientation: CGImagePropertyOrientation?)](./init%28_,orientation%29-8cwes.md)
  Creates a handler for performing requests on an image contained in a data object.
- [convenience init(CGImage, orientation: CGImagePropertyOrientation?)](./init%28_,orientation%29-8nodt.md)
  Creates a handler for performing requests on Core Graphics images.
- [convenience init(CMSampleBuffer, depthData: AVDepthData?, orientation: CGImagePropertyOrientation?)](./init%28_,depthdata,orientation%29-5itte.md)
  Creates a request handler that performs requests on an image contained within a sample buffer.
- [convenience init(CIImage, orientation: CGImagePropertyOrientation?)](./init%28_,orientation%29-2hvfr.md)
  Creates a handler for performing requests on Core Image images.
- [convenience init(CVPixelBuffer, orientation: CGImagePropertyOrientation?)](./init%28_,orientation%29-3zrh5.md)
- [convenience init(CMSampleBuffer, orientation: CGImagePropertyOrientation?)](./init%28_,orientation%29-8q7vz.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/imagerequesthandler/init(_:depthdata:orientation:)-3ebxg)*