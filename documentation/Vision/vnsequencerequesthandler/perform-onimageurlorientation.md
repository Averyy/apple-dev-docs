# perform(_:onImageURL:orientation:)

**Framework**: Vision  
**Kind**: method

Schedules one or more Vision requests to be performed on an image with known orientation, at a specific URL.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func perform(_ requests: [VNRequest], onImageURL imageURL: URL, orientation: CGImagePropertyOrientation) throws
```

## Parameters

- `requests`: An array of   requests to perform.
- `imageURL`: A URL pointing to the image on which to perform the request.
- `orientation`: The orientation of the input image.

## See Also

- [func perform([VNRequest], on: CGImage) throws](vnsequencerequesthandler/perform(_:on:)-3zt7l.md)
  Schedules Vision requests to be performed on a Core Graphics image.
- [func perform([VNRequest], on: CGImage, orientation: CGImagePropertyOrientation) throws](vnsequencerequesthandler/perform(_:on:orientation:)-3gcmv.md)
  Schedules one or more Vision requests to be performed on a Core Graphics image with known orientation.
- [func perform([VNRequest], on: CIImage) throws](vnsequencerequesthandler/perform(_:on:)-9jtgj.md)
  Schedules one or more Vision requests to be performed on Core Image image data.
- [func perform([VNRequest], on: CIImage, orientation: CGImagePropertyOrientation) throws](vnsequencerequesthandler/perform(_:on:orientation:)-1bkm1.md)
  Schedules one or more Vision requests to be performed on Core Image image data with known orientation.
- [func perform([VNRequest], on: CVPixelBuffer) throws](vnsequencerequesthandler/perform(_:on:)-3d7nt.md)
  Schedules one or more Vision requests to be performed on a Core Video pixel buffer.
- [func perform([VNRequest], on: CVPixelBuffer, orientation: CGImagePropertyOrientation) throws](vnsequencerequesthandler/perform(_:on:orientation:)-2wvt8.md)
  Schedules one or more Vision requests to be performed on a Core Video pixel buffer with known orientation.
- [func perform([VNRequest], on: CMSampleBuffer) throws](vnsequencerequesthandler/perform(_:on:)-45e73.md)
  Performs one or more requests on an image contained within a sample buffer.
- [func perform([VNRequest], on: CMSampleBuffer, orientation: CGImagePropertyOrientation) throws](vnsequencerequesthandler/perform(_:on:orientation:)-6b7rk.md)
  Performs one or more requests on an image of a specified orientation contained within a sample buffer.
- [func perform([VNRequest], onImageData: Data) throws](vnsequencerequesthandler/perform(_:onimagedata:).md)
  Schedules one or more Vision requests to be performed on raw image data.
- [func perform([VNRequest], onImageData: Data, orientation: CGImagePropertyOrientation) throws](vnsequencerequesthandler/perform(_:onimagedata:orientation:).md)
  Schedules one or more Vision requests to be performed on raw data containing an image with known orientation.
- [func perform([VNRequest], onImageURL: URL) throws](vnsequencerequesthandler/perform(_:onimageurl:).md)
  Schedules one or more Vision requests to be performed on an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnsequencerequesthandler/perform(_:onimageurl:orientation:))*