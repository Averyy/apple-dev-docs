# init(data:options:)

**Framework**: Vision  
**Kind**: init  
**Role**: Initializer

Creates a handler to use for performing requests on an image in a data object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(data imageData: Data, options: [VNImageOption : Any] = [:])
```

```objc
- (instancetype) initWithData:(NSData *) imageData options:(NSDictionary<NSString *,id> *) options;
```

#### Discussion

The intended use cases of this type of initializer include compressed images and network downloads, where a client may receive a JPEG from a website or the cloud.

## Parameters

- `imageData`: Data containing the image to be used for performing the requests. Image content is immutable.
- `options`: An optional dictionary containing [`VNImageOption`](../vnimageoption.md) keys to auxiliary image data.

## See Also

### Creating a Request Handler
- [init(CGImage: CGImage, options: [VNImageOption : Any])](./init%28cgimage,options%29-5tp19.md)
- [init(cgImage: CGImage, options: [VNImageOption : Any])](./init%28cgimage,options%29-4qda6.md)
  Creates a handler to be used for performing requests on Core Graphics images.
- [init(CGImage: CGImage, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](./init%28cgimage,orientation,options%29-8imhf.md)
- [init(cgImage: CGImage, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any])](./init%28cgimage,orientation,options%29-63ojm.md)
  Creates a handler to be used for performing requests on a Core Graphics image with known orientation.
- [init(CIImage: CIImage, options: [VNImageOption : Any])](./init%28ciimage,options%29-55zel.md)
- [init(ciImage: CIImage, options: [VNImageOption : Any])](./init%28ciimage,options%29-4wf33.md)
  Creates a handler to use for performing requests on Core Image image data.
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
- [- initWithCMSampleBuffer:options:](./init%28cmsamplebuffer,options%29-2yodn.md)
  Creates a request handler that performs requests on an image contained within a sample buffer.
- [- initWithCMSampleBuffer:orientation:options:](./init%28cmsamplebuffer,orientation,options%29-335k4.md)
  Creates a request handler that performs requests on an image of a specified orientation contained within a sample buffer.
- [- initWithCMSampleBuffer:depthData:orientation:options:](./init%28cmsamplebuffer,depthdata,orientation,options%29-8bjyh.md)
  Creates a request handler that performs requests on an image in a sample buffer that contains depth data.
- [- initWithData:orientation:options:](./init%28data,orientation,options%29.md)
  Creates a handler to use for performing requests on an image of known orientation.
- [- initWithURL:options:](./init%28url,options%29-4k623.md)
  Creates a handler to be used for performing requests on an image at the specified URL.
- [- initWithURL:orientation:options:](./init%28url,orientation,options%29-70nta.md)
  Creates a handler to be used for performing requests on an image with known orientation, at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnimagerequesthandler/init(data:options:))*