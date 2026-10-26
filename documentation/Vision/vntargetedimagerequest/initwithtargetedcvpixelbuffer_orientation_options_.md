# initWithTargetedCVPixelBuffer:orientation:options:

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

Creates a new request targeting an image in a pixel buffer of known orientation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```objc
- (instancetype) initWithTargetedCVPixelBuffer:(CVPixelBufferRef) pixelBuffer orientation:(CGImagePropertyOrientation) orientation options:(NSDictionary<NSString *,id> *) options;
```

## Parameters

- `pixelBuffer`: The pixel buffer containing the targeted image.
- `orientation`: The orientation of the image buffer, based on EXIF specification and superseding other orientation information. The value must be an integer from `1` to `8`; see [`kCGImagePropertyOrientation`](../../ImageIO/kcgimagepropertyorientation.md) for details.
- `options`: A dictionary with options specifying auxiliary information for the image.

## See Also

### Creating a Request
- [- initWithTargetedCGImage:options:](./initwithtargetedcgimage_options_.md)
  Creates a new request targeting a Core Graphics image.
- [init(targetedCGImage: CGImage, options: [VNImageOption : Any], completionHandler: VNRequestCompletionHandler?)](./init%28targetedcgimage,options,completionhandler%29.md)
  Creates a new request targeting a Core Graphics image, executing the completion handler when done.
- [- initWithTargetedCGImage:orientation:options:](./initwithtargetedcgimage_orientation_options_.md)
  Creates a new request targeting a Core Graphics image of known orientation.
- [init(targetedCGImage: CGImage, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any], completionHandler: VNRequestCompletionHandler?)](./init%28targetedcgimage,orientation,options,completionhandler%29.md)
  Creates a new request targeting a Core Graphics image of known orientation, executing the completion handler when done.
- [- initWithTargetedCIImage:options:](./initwithtargetedciimage_options_.md)
  Creates a new request targeting a Core Image image.
- [init(targetedCIImage: CIImage, options: [VNImageOption : Any], completionHandler: VNRequestCompletionHandler?)](./init%28targetedciimage,options,completionhandler%29.md)
  Creates a new request targeting a Core Image image.
- [- initWithTargetedCIImage:orientation:options:](./initwithtargetedciimage_orientation_options_.md)
  Creates a new request targeting a Core Image image of known orientation.
- [init(targetedCIImage: CIImage, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any], completionHandler: VNRequestCompletionHandler?)](./init%28targetedciimage,orientation,options,completionhandler%29.md)
  Creates a new request targeting a Core Image image of known orientation, executing the completion handler when done.
- [- initWithTargetedCVPixelBuffer:options:](./initwithtargetedcvpixelbuffer_options_.md)
  Creates a new request targeting an image in a pixel buffer.
- [init(targetedCVPixelBuffer: CVPixelBuffer, options: [VNImageOption : Any], completionHandler: VNRequestCompletionHandler?)](./init%28targetedcvpixelbuffer,options,completionhandler%29.md)
  Creates a new request targeting an image in a pixel buffer.
- [init(targetedCVPixelBuffer: CVPixelBuffer, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any], completionHandler: VNRequestCompletionHandler?)](./init%28targetedcvpixelbuffer,orientation,options,completionhandler%29.md)
  Creates a new request targeting an image in a pixel buffer of known orientation.
- [- initWithTargetedCMSampleBuffer:options:](./initwithtargetedcmsamplebuffer_options_.md)
  Creates a new request that targets an image in a sample buffer.
- [init(targetedCMSampleBuffer: CMSampleBuffer, options: [VNImageOption : Any], completionHandler: VNRequestCompletionHandler?)](./init%28targetedcmsamplebuffer,options,completionhandler%29.md)
  Creates a new request with a completion handler that targets an image in a sample buffer.
- [- initWithTargetedCMSampleBuffer:orientation:options:](./initwithtargetedcmsamplebuffer_orientation_options_.md)
  Creates a new request that targets an image of a known orientation in a sample buffer.
- [init(targetedCMSampleBuffer: CMSampleBuffer, orientation: CGImagePropertyOrientation, options: [VNImageOption : Any], completionHandler: VNRequestCompletionHandler?)](./init%28targetedcmsamplebuffer,orientation,options,completionhandler%29.md)
  Creates a new request with a completion handler that targets an image of a known orientation in a sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntargetedimagerequest/initwithtargetedcvpixelbuffer:orientation:options:)*