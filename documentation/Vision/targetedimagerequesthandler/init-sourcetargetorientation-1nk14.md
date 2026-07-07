# init(source:target:orientation:)

**Framework**: Vision  
**Kind**: init

Creates a handler for performing requests on Core Image images.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
convenience init(source: CIImage, target: CIImage, orientation: CGImagePropertyOrientation? = nil)
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/targetedimagerequesthandler/init(source:target:orientation:)-1nk14)*