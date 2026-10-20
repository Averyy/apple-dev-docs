# init(_:orientation:)

**Framework**: Vision  
**Kind**: init  
**Role**: Initializer

Creates a handler for performing requests on an image at the specified URL.

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
convenience init(_ imageURL: URL, orientation: CGImagePropertyOrientation? = nil)
```

## See Also

### Creating a request handler
- [convenience init(Data, orientation: CGImagePropertyOrientation?)](./init%28_,orientation%29-8cwes.md)
  Creates a handler for performing requests on an image contained in a data object.
- [convenience init(CGImage, orientation: CGImagePropertyOrientation?)](./init%28_,orientation%29-8nodt.md)
  Creates a handler for performing requests on Core Graphics images.
- [convenience init(CVPixelBuffer, depthData: AVDepthData?, orientation: CGImagePropertyOrientation?)](./init%28_,depthdata,orientation%29-3ebxg.md)
  Creates a handler for performing requests on a Core Video pixel buffer.
- [convenience init(CMSampleBuffer, depthData: AVDepthData?, orientation: CGImagePropertyOrientation?)](./init%28_,depthdata,orientation%29-5itte.md)
  Creates a request handler that performs requests on an image contained within a sample buffer.
- [convenience init(CIImage, orientation: CGImagePropertyOrientation?)](./init%28_,orientation%29-2hvfr.md)
  Creates a handler for performing requests on Core Image images.
- [convenience init(CVPixelBuffer, orientation: CGImagePropertyOrientation?)](./init%28_,orientation%29-3zrh5.md)
- [convenience init(CMSampleBuffer, orientation: CGImagePropertyOrientation?)](./init%28_,orientation%29-8q7vz.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/imagerequesthandler/init(_:orientation:)-6imw8)*