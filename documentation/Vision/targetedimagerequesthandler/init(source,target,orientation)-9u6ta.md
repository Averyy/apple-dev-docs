# init(source:target:orientation:)

**Framework**: Vision  
**Kind**: init  
**Role**: Initializer

Creates a request handler that performs requests on an image contained within a sample buffer.

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
convenience init(source: CMSampleBuffer, target: CMSampleBuffer, orientation: CGImagePropertyOrientation? = nil)
```

## See Also

### Creating a request handler
- [convenience init(sourceURL: URL, targetURL: URL, orientation: CGImagePropertyOrientation?)](./init%28sourceurl,targeturl,orientation%29.md)
  Creates a handler for performing requests on an image at the specified URL.
- [convenience init(source: Data, target: Data, orientation: CGImagePropertyOrientation?)](./init%28source,target,orientation%29-4wr1c.md)
  Creates a handler for performing requests on an image contained in a data object.
- [convenience init(source: CGImage, target: CGImage, orientation: CGImagePropertyOrientation?)](./init%28source,target,orientation%29-66ft9.md)
  Creates a handler for performing requests on Core Graphics images.
- [convenience init(source: CVPixelBuffer, target: CVPixelBuffer, orientation: CGImagePropertyOrientation?)](./init%28source,target,orientation%29-64lxw.md)
  Creates a handler for performing requests on a Core Video pixel buffer.
- [convenience init(source: CIImage, target: CIImage, orientation: CGImagePropertyOrientation?)](./init%28source,target,orientation%29-1nk14.md)
  Creates a handler for performing requests on Core Image images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/targetedimagerequesthandler/init(source:target:orientation:)-9u6ta)*