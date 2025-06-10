# settingProperties(_:)

**Framework**: Core Image  
**Kind**: method

Returns a new image created by adding the specified metadata properties to the image.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func settingProperties(_ properties: [AnyHashable : Any]) -> CIImage
```

#### Return Value

An image object with the specified properties.

#### Discussion

When you create an image, Core Image sets an image’s [`properties`](ciimage/properties.md) dictionary to the metadata you specify (using the [`properties`](ciimageoption/properties.md) key in an `options` dictionary), or to the underlying image’s metadata (by calling the [`CGImageSourceCopyPropertiesAtIndex(_:_:_:)`](https://developer.apple.com/documentation/ImageIO/CGImageSourceCopyPropertiesAtIndex(_:_:_:)) function). Use this method to override an image’s metadata properties with new values.

## Parameters

- `properties`: A dictionary of metadata properties to associate with the image.

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
- [func unpremultiplyingAlpha() -> CIImage](ciimage/unpremultiplyingalpha.md)
  Returns a new image created by dividing the image’s RGB values by its alpha values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/settingproperties(_:))*