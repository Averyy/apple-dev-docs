# perform(_:on:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

Performs one or more requests on an image contained within a sample buffer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func perform(_ requests: [VNRequest], on sampleBuffer: CMSampleBuffer) throws
```

```objc
- (BOOL) performRequests:(NSArray<VNRequest *> *) requests onCMSampleBuffer:(CMSampleBufferRef) sampleBuffer error:(NSError **) error;
```

## Parameters

- `requests`: The array of requests to perform.
- `sampleBuffer`: A sample buffer containing a valid [`imageBuffer`](../../CoreMedia/cmsamplebuffer/imagebuffer.md).

## See Also

### Performing a Sequence Request
- [func perform([VNRequest], on: CGImage) throws](./perform%28_,on%29-3zt7l.md)
  Schedules Vision requests to be performed on a Core Graphics image.
- [func perform([VNRequest], on: CGImage, orientation: CGImagePropertyOrientation) throws](./perform%28_,on,orientation%29-3gcmv.md)
  Schedules one or more Vision requests to be performed on a Core Graphics image with known orientation.
- [func perform([VNRequest], on: CIImage) throws](./perform%28_,on%29-9jtgj.md)
  Schedules one or more Vision requests to be performed on Core Image image data.
- [func perform([VNRequest], on: CIImage, orientation: CGImagePropertyOrientation) throws](./perform%28_,on,orientation%29-1bkm1.md)
  Schedules one or more Vision requests to be performed on Core Image image data with known orientation.
- [func perform([VNRequest], on: CVPixelBuffer) throws](./perform%28_,on%29-3d7nt.md)
  Schedules one or more Vision requests to be performed on a Core Video pixel buffer.
- [func perform([VNRequest], on: CVPixelBuffer, orientation: CGImagePropertyOrientation) throws](./perform%28_,on,orientation%29-2wvt8.md)
  Schedules one or more Vision requests to be performed on a Core Video pixel buffer with known orientation.
- [func perform([VNRequest], on: CMSampleBuffer, orientation: CGImagePropertyOrientation) throws](./perform%28_,on,orientation%29-6b7rk.md)
  Performs one or more requests on an image of a specified orientation contained within a sample buffer.
- [func perform([VNRequest], onImageData: Data) throws](./perform%28_,onimagedata%29.md)
  Schedules one or more Vision requests to be performed on raw image data.
- [func perform([VNRequest], onImageData: Data, orientation: CGImagePropertyOrientation) throws](./perform%28_,onimagedata,orientation%29.md)
  Schedules one or more Vision requests to be performed on raw data containing an image with known orientation.
- [func perform([VNRequest], onImageURL: URL) throws](./perform%28_,onimageurl%29.md)
  Schedules one or more Vision requests to be performed on an image.
- [func perform([VNRequest], onImageURL: URL, orientation: CGImagePropertyOrientation) throws](./perform%28_,onimageurl,orientation%29.md)
  Schedules one or more Vision requests to be performed on an image with known orientation, at a specific URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnsequencerequesthandler/perform(_:on:)-45e73)*