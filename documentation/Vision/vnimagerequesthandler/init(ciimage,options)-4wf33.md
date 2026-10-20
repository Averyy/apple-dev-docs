# init(ciImage:options:)

**Framework**: Vision  
**Kind**: init  
**Role**: Initializer

Creates a handler to use for performing requests on Core Image image data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(ciImage image: CIImage, options: [VNImageOption : Any] = [:])
```

```objc
- (instancetype) initWithCIImage:(CIImage *) image options:(NSDictionary<NSString *,id> *) options;
```

## Parameters

- `image`: A [`CIImage`](../../CoreImage/ciimage.md) containing the image to be used for performing the requests. Image content is immutable.
- `options`: An optional dictionary containing [`properties`](../vnimageoption/properties.md) keys to auxiliary image data.

## See Also

### Creating a Request Handler
- [init(CGImage: CGImage, options: [VNImageOption : Any])](./init%28cgimage,options%29-5tp19.md)
- [init(cgImage: CGImage, options: [VNImageOption : Any])](./init%28cgimage,options%29-4qda6.md)
  Creates a handler to be used for performing requests on Core Graphics images.
- [init(CGImage: CGImage, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](./init%28cgimage,orientation,options%29-8imhf.md)
- [init(cgImage: CGImage, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](./init%28cgimage,orientation,options%29-63ojm.md)
  Creates a handler to be used for performing requests on a Core Graphics image with known orientation.
- [init(CIImage: CIImage, options: [VNImageOption : Any])](./init%28ciimage,options%29-55zel.md)
- [init(CIImage: CIImage, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](./init%28ciimage,orientation,options%29-8p8h1.md)
- [init(ciImage: CIImage, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](./init%28ciimage,orientation,options%29-3svy6.md)
  Creates a handler to be used for performing requests on Core Image image data of a known orientation.
- [init(CVPixelBuffer: CVPixelBuffer, options: [VNImageOption : Any])](./init%28cvpixelbuffer,options%29-3pee9.md)
- [init(cvPixelBuffer: CVPixelBuffer, options: [VNImageOption : Any])](./init%28cvpixelbuffer,options%29-bkd7.md)
  Creates a handler for performing requests on a Core Video pixel buffer.
- [init(CVPixelBuffer: CVPixelBuffer, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](./init%28cvpixelbuffer,orientation,options%29-160f.md)
- [init(cvPixelBuffer: CVPixelBuffer, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](./init%28cvpixelbuffer,orientation,options%29-9fxug.md)
  Creates a handler for performing requests on a Core Video pixel buffer of a known orientation.
- [init(CVPixelBuffer: CVPixelBuffer, depthData: AVDepthData, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](./init%28cvpixelbuffer,depthdata,orientation,options%29-3u960.md)
- [init(cvPixelBuffer: CVPixelBuffer, depthData: AVDepthData, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](./init%28cvpixelbuffer,depthdata,orientation,options%29-3mj2d.md)
- [init(CMSampleBuffer: CMSampleBuffer, options: [VNImageOption : Any])](./init%28cmsamplebuffer,options%29-4mpwd.md)
- [init(cmSampleBuffer: CMSampleBuffer, options: [VNImageOption : Any])](./init%28cmsamplebuffer,options%29-2yodn.md)
  Creates a request handler that performs requests on an image contained within a sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnimagerequesthandler/init(ciimage:options:)-4wf33)*