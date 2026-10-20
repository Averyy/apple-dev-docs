# perform(_:on:orientation:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

Schedules one or more Vision requests to be performed on a Core Video pixel buffer with known orientation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func perform(_ requests: [VNRequest], on pixelBuffer: CVPixelBuffer, orientation: CGImagePropertyOrientation) throws
```

```objc
- (BOOL) performRequests:(NSArray<VNRequest *> *) requests onCVPixelBuffer:(CVPixelBufferRef) pixelBuffer orientation:(CGImagePropertyOrientation) orientation error:(NSError **) error;
```

## Parameters

- `requests`: An array of [`VNRequest`](../vnrequest.md) requests to perform.
- `pixelBuffer`: The input [`CVPixelBuffer`](../../CoreVideo/cvpixelbuffer.md) on which to perform the request.
- `orientation`: The orientation of the input `image`.

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
- [func perform([VNRequest], on: CMSampleBuffer) throws](./perform%28_,on%29-45e73.md)
  Performs one or more requests on an image contained within a sample buffer.
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

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnsequencerequesthandler/perform(_:on:orientation:)-2wvt8)*