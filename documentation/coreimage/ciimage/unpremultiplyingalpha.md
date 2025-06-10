# unpremultiplyingAlpha()

**Framework**: Core Image  
**Kind**: method

Returns a new image created by dividing the image’s RGB values by its alpha values.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func unpremultiplyingAlpha() -> CIImage
```

#### Return Value

An image object representing the result of the operation.

#### Discussion

Premultiplied alpha speeds up the rendering of images, but some custom filter routines can be expressed more efficiently with non-premultiplied RGB values. Use this method if you need to apply such a filter to an image that has premultiplied alpha.

## See Also

- [func applyingFilter(String, parameters: [String : Any]) -> CIImage](ciimage/applyingfilter(_:parameters:).md)
  Returns a new image created by applying a filter to the original image with the specified name and parameters.
- [func applyingFilter(String) -> CIImage](ciimage/applyingfilter(_:).md)
  Applies the filter to an image and returns the output.
- [func transformed(by: CGAffineTransform) -> CIImage](ciimage/transformed(by:).md)
  Returns a new image that represents the original image after applying an affine transform.
- [func transformed(by: CGAffineTransform, highQualityDownsample: Bool) -> CIImage](ciimage/transformed(by:highqualitydownsample:).md)
- [func cropped(to: CGRect) -> CIImage](ciimage/cropped(to:).md)
  Returns a new image with a cropped portion of the original image.
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
- [func settingAlphaOne(in: CGRect) -> CIImage](ciimage/settingalphaone(in:).md)
  Returns a new image created by setting all alpha values to 1.0 within the specified rectangle and to 0.0 outside of that area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/unpremultiplyingalpha())*