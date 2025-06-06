# applyingFilter(_:)

**Framework**: Core Image  
**Kind**: instm

Applies the filter to an image and returns the output.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func applyingFilter(_ filterName: String) -> CIImage
```

#### Discussion

A convenience method for applying a single filter to the method receiver and returning the output image.  Identical to [`applyingFilter(_:parameters:)`](ciimage/1437589-applyingfilter.md) with default parameters.

> ❗ **Important**: This method, though convenient, is inefficient if used multiple times in succession.  Achieve better performance by chaining filters without asking for the outputs of individual filters.

This method, though convenient, is inefficient if used multiple times in succession.  Achieve better performance by chaining filters without asking for the outputs of individual filters.

## See Also

- [func applyingFilter(String, parameters: [String : Any]) -> CIImage](ciimage/1437589-applyingfilter.md)
  Returns a new image created by applying a filter to the original image with the specified name and parameters.
- [func transformed(by: CGAffineTransform) -> CIImage](ciimage/1438203-transformed.md)
  Returns a new image that represents the original image after applying an affine transform.
- [func transformed(by: CGAffineTransform, highQualityDownsample: Bool) -> CIImage](ciimage/3334939-transformed.md)
- [func cropped(to: CGRect) -> CIImage](ciimage/1437833-cropped.md)
  Returns a new image with a cropped portion of the original image.
- [func oriented(forExifOrientation: Int32) -> CIImage](ciimage/1438223-oriented.md)
  Returns a new image created by transforming the original image to the specified EXIF orientation.
- [func clampedToExtent() -> CIImage](ciimage/1437628-clampedtoextent.md)
  Returns a new image created by making the pixel colors along its edges extend infinitely in all directions.
- [func clamped(to: CGRect) -> CIImage](ciimage/1645893-clamped.md)
  Returns a new image created by cropping to a specified area, then making the pixel colors along the edges of the cropped image extend infinitely in all directions.
- [func composited(over: CIImage) -> CIImage](ciimage/1437837-composited.md)
  Returns a new image created by compositing the original image over the specified destination image.
- [func convertingWorkingSpaceToLab() -> CIImage](ciimage/3975704-convertingworkingspacetolab.md)
- [func convertingLabToWorkingSpace() -> CIImage](ciimage/3975703-convertinglabtoworkingspace.md)
- [func matchedToWorkingSpace(from: CGColorSpace) -> CIImage?](ciimage/1645896-matchedtoworkingspace.md)
  Returns a new image created by color matching from the specified color space to the context’s working color space.
- [func matchedFromWorkingSpace(to: CGColorSpace) -> CIImage?](ciimage/1645898-matchedfromworkingspace.md)
  Returns a new image created by color matching from the context’s working color space to the specified color space.
- [func premultiplyingAlpha() -> CIImage](ciimage/1645894-premultiplyingalpha.md)
  Returns a new image created by multiplying the image’s RGB values by its alpha values.
- [func unpremultiplyingAlpha() -> CIImage](ciimage/1645892-unpremultiplyingalpha.md)
  Returns a new image created by dividing the image’s RGB values by its alpha values.
- [func settingAlphaOne(in: CGRect) -> CIImage](ciimage/1645891-settingalphaone.md)
  Returns a new image created by setting all alpha values to 1.0 within the specified rectangle and to 0.0 outside of that area.
- [func applyingGaussianBlur(sigma: Double) -> CIImage](ciimage/1645897-applyinggaussianblur.md)
  Returns a new image created by applying a Gaussian Blur filter to the image.
- [func settingProperties([AnyHashable : Any]) -> CIImage](ciimage/1645895-settingproperties.md)
  Returns a new image created by adding the specified metadata properties to the image.
- [func insertingIntermediate() -> CIImage](ciimage/2966521-insertingintermediate.md)
  Returns a new image created by inserting an intermediate.
- [func insertingIntermediate(cache: Bool) -> CIImage](ciimage/2966522-insertingintermediate.md)
  Returns a new image created by inserting a cacheable intermediate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/2915368-applyingfilter)*