# cropped(to:)

**Framework**: Core Image  
**Kind**: method

Returns a new image with a cropped portion of the original image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func cropped(to rect: CGRect) -> CIImage
```

#### Return Value

An image object cropped to the specified rectangle.

#### Discussion

![Butterfly photo with background cropped out](https://docs-assets.developer.apple.com/published/44e39ae57f70286b7a3ea4d5a6491b8b/media-2951307%402x.png)

#### Discussion

Due to Core Image’s coordinate system mismatch with [`UIKit`](https://developer.apple.comhttps://developer.apple.com/library/archive/releasenotes/General/WhatsNewIniOS/Articles/iOS5.html#//apple_ref/doc/uid/TP30915195-SW41), this filtering approach may yield unexpected results when displayed in a [`UIImageView`](https://developer.apple.com/documentation/UIKit/UIImageView) with [`contentMode`](https://developer.apple.com/documentation/UIKit/UIView/contentMode-swift.property). Be sure to back it with a [`cgImage`](ciimage/cgimage.md) so that it handles [`contentMode`](https://developer.apple.com/documentation/UIKit/UIView/contentMode-swift.property) properly.

```swift
CIContext* context = [CIContext context];
CGImageRef cgCroppedImage = [context createCGImage:ciCroppedImage fromRect:ciCroppedImage.extent];
UIImage* croppedImage = [UIImage imageWithCGImage:cgCroppedImage];
CGImageRelease(cgCroppedImage);
```

If you are displaying or processing your image primarily as a [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) or [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage), with no additional Core Image application, consider cropping in Core Graphics using the [`cropping(to:)`](https://developer.apple.com/documentation/CoreGraphics/CGImage/cropping(to:)) function to save processing overhead from conversion of images to [`CIImage`](ciimage.md).  It makes most sense to use [`cropped(to:)`](ciimage/cropped(to:).md) when you already have [`CIImage`](ciimage.md) in your pipeline.

## Parameters

- `rect`: The rectangle, in image coordinates, to which to crop the image.

## See Also

- [func applyingFilter(String, parameters: [String : Any]) -> CIImage](ciimage/applyingfilter(_:parameters:).md)
  Returns a new image created by applying a filter to the original image with the specified name and parameters.
- [func applyingFilter(String) -> CIImage](ciimage/applyingfilter(_:).md)
  Applies the filter to an image and returns the output.
- [func transformed(by: CGAffineTransform) -> CIImage](ciimage/transformed(by:).md)
  Returns a new image that represents the original image after applying an affine transform.
- [func transformed(by: CGAffineTransform, highQualityDownsample: Bool) -> CIImage](ciimage/transformed(by:highqualitydownsample:).md)
- [func oriented(forExifOrientation: Int32) -> CIImage](ciimage/oriented(forexiforientation:).md)
  Returns a new image created by transforming the original image to the specified EXIF orientation.
- [func clampedToExtent() -> CIImage](ciimage/clampedtoextent.md)
  Returns a new image created by making the pixel colors along its edges extend infinitely in all directions.
- [func clamped(to: CGRect) -> CIImage](ciimage/clamped(to:).md)
  Returns a new image created by cropping to a specified area, then making the pixel colors along the edges of the cropped image extend infinitely in all directions.
- [func composited(over: CIImage) -> CIImage](ciimage/composited(over:).md)
  Returns a new image created by compositing the original image over the specified destination image.
- [func convertingWorkingSpaceToLab() -> CIImage](ciimage/convertingworkingspacetolab.md)
- [func convertingLabToWorkingSpace() -> CIImage](ciimage/convertinglabtoworkingspace.md)
- [func matchedToWorkingSpace(from: CGColorSpace) -> CIImage?](ciimage/matchedtoworkingspace(from:).md)
  Returns a new image created by color matching from the specified color space to the context’s working color space.
- [func matchedFromWorkingSpace(to: CGColorSpace) -> CIImage?](ciimage/matchedfromworkingspace(to:).md)
  Returns a new image created by color matching from the context’s working color space to the specified color space.
- [func premultiplyingAlpha() -> CIImage](ciimage/premultiplyingalpha.md)
  Returns a new image created by multiplying the image’s RGB values by its alpha values.
- [func unpremultiplyingAlpha() -> CIImage](ciimage/unpremultiplyingalpha.md)
  Returns a new image created by dividing the image’s RGB values by its alpha values.
- [func settingAlphaOne(in: CGRect) -> CIImage](ciimage/settingalphaone(in:).md)
  Returns a new image created by setting all alpha values to 1.0 within the specified rectangle and to 0.0 outside of that area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/cropped(to:))*