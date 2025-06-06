# orientationTransform(forExifOrientation:)

**Framework**: Core Image  
**Kind**: instm

Returns the transformation needed to reorient the image to the specified orientation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func orientationTransform(forExifOrientation orientation: Int32) -> CGAffineTransform
```

#### Return_value

An affine transform that will rotate or mirror the image to match the specified orientation when applied.

#### Discussion

This method determines the transformation needed to match the specified orientation, but does not apply that transformation to the image. To apply the transformation (possibly after concatenating it with other transformations), use the [`transformed(by:)`](ciimage/1438203-transformed.md) method or the `CIAffineTransform` filter. To determine and apply the transformation in a single step, use the [`oriented(forExifOrientation:)`](ciimage/1438223-oriented.md) method.

## Parameters

- `orientation`: An integer specifying an image orientation according to the EXIF specification. For details, see  .

## See Also

- [var definition: CIFilterShape](ciimage/1437804-definition.md)
  Returns a filter shape object that represents the domain of definition of the image.
- [var extent: CGRect](ciimage/1437996-extent.md)
  A rectangle that specifies the extent of the image.
- [var properties: [String : Any]](ciimage/1437733-properties.md)
  A dictionary containing metadata about the image.
- [var url: URL?](ciimage/1438195-url.md)
  The URL from which the image was loaded.
- [var colorSpace: CGColorSpace?](ciimage/1437750-colorspace.md)
  The color space of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/1437930-orientationtransform)*