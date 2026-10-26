# init(targetedCGImage:orientation:options:completionHandler:)

**Framework**: Vision  
**Kind**: init  
**Role**: Initializer

Creates a new request targeting a Core Graphics image of known orientation, executing the completion handler when done.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(targetedCGImage cgImage: CGImage, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any] = [:], completionHandler: VNRequestCompletionHandler? = nil)
```

```objc
- (instancetype) initWithTargetedCGImage:(CGImageRef) cgImage orientation:(CGImagePropertyOrientation) orientation options:(NSDictionary<NSString *,id> *) options completionHandler:(VNRequestCompletionHandler) completionHandler;
```

## Parameters

- `cgImage`: The targeted Core Graphics image.
- `orientation`: The orientation of the image buffer, based on EXIF specification and superseding other orientation information. The value must be an integer from `1` to `8`; see [`kCGImagePropertyOrientation`](../../ImageIO/kcgimagepropertyorientation.md) for details.
- `options`: A dictionary with options specifying auxiliary information for the image.
- `completionHandler`: The block to invoke when the request has finished executing.

## See Also

### Creating a Request
- [init(targetedCGImage: CGImage, options: [VNImageOption : Any], completionHandler: VNRequestCompletionHandler?)](./init%28targetedcgimage,options,completionhandler%29.md)
  Creates a new request targeting a Core Graphics image, executing the completion handler when done.
- [init(targetedCIImage: CIImage, options: [VNImageOption : Any], completionHandler: VNRequestCompletionHandler?)](./init%28targetedciimage,options,completionhandler%29.md)
  Creates a new request targeting a Core Image image.
- [init(targetedCIImage: CIImage, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any], completionHandler: VNRequestCompletionHandler?)](./init%28targetedciimage,orientation,options,completionhandler%29.md)
  Creates a new request targeting a Core Image image of known orientation, executing the completion handler when done.
- [init(targetedCVPixelBuffer: CVPixelBuffer, options: [VNImageOption : Any], completionHandler: VNRequestCompletionHandler?)](./init%28targetedcvpixelbuffer,options,completionhandler%29.md)
  Creates a new request targeting an image in a pixel buffer.
- [init(targetedCVPixelBuffer: CVPixelBuffer, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any], completionHandler: VNRequestCompletionHandler?)](./init%28targetedcvpixelbuffer,orientation,options,completionhandler%29.md)
  Creates a new request targeting an image in a pixel buffer of known orientation.
- [init(targetedCMSampleBuffer: CMSampleBuffer, options: [VNImageOption : Any], completionHandler: VNRequestCompletionHandler?)](./init%28targetedcmsamplebuffer,options,completionhandler%29.md)
  Creates a new request with a completion handler that targets an image in a sample buffer.
- [init(targetedCMSampleBuffer: CMSampleBuffer, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any], completionHandler: VNRequestCompletionHandler?)](./init%28targetedcmsamplebuffer,orientation,options,completionhandler%29.md)
  Creates a new request with a completion handler that targets an image of a known orientation in a sample buffer.
- [init(targetedImageData: Data, options: [VNImageOption : Any], completionHandler: VNRequestCompletionHandler?)](./init%28targetedimagedata,options,completionhandler%29.md)
  Creates a new request targeting an image as raw data, executing the completion handler when done.
- [init(targetedImageData: Data, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any], completionHandler: VNRequestCompletionHandler?)](./init%28targetedimagedata,orientation,options,completionhandler%29.md)
  Creates a new request targeting a raw data image of known orientation, executing the completion handler when done.
- [init(targetedImageURL: URL, options: [VNImageOption : Any], completionHandler: VNRequestCompletionHandler?)](./init%28targetedimageurl,options,completionhandler%29.md)
  Creates a new request targeting an image at the specified URL, executing the completion handler when done.
- [init(targetedImageURL: URL, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any], completionHandler: VNRequestCompletionHandler?)](./init%28targetedimageurl,orientation,options,completionhandler%29.md)
  Creates a new request targeting an image of known orientation, at the specified URL, executing the completion handler when done.
- [- initWithTargetedCGImage:options:](./initwithtargetedcgimage_options_.md)
  Creates a new request targeting a Core Graphics image.
- [- initWithTargetedCGImage:orientation:options:](./initwithtargetedcgimage_orientation_options_.md)
  Creates a new request targeting a Core Graphics image of known orientation.
- [- initWithTargetedCIImage:options:](./initwithtargetedciimage_options_.md)
  Creates a new request targeting a Core Image image.
- [- initWithTargetedCIImage:orientation:options:](./initwithtargetedciimage_orientation_options_.md)
  Creates a new request targeting a Core Image image of known orientation.
- [- initWithTargetedCVPixelBuffer:options:](./initwithtargetedcvpixelbuffer_options_.md)
  Creates a new request targeting an image in a pixel buffer.
- [- initWithTargetedCVPixelBuffer:orientation:options:](./initwithtargetedcvpixelbuffer_orientation_options_.md)
  Creates a new request targeting an image in a pixel buffer of known orientation.
- [- initWithTargetedCMSampleBuffer:options:](./initwithtargetedcmsamplebuffer_options_.md)
  Creates a new request that targets an image in a sample buffer.
- [- initWithTargetedCMSampleBuffer:orientation:options:](./initwithtargetedcmsamplebuffer_orientation_options_.md)
  Creates a new request that targets an image of a known orientation in a sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntargetedimagerequest/init(targetedcgimage:orientation:options:completionhandler:))*