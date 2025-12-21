# url

**Framework**: Core Image  
**Kind**: property

The URL from which the image was loaded.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var url: URL? { get }
```

#### Discussion

A URL is available only if the image object was created with a URL (such as with the [`init(contentsOf:)`](ciimage/init(contentsof:).md) method or related methods). Otherwise, this property’s value is `nil`.

## See Also

- [var definition: CIFilterShape](ciimage/definition.md)
  Returns a filter shape object that represents the domain of definition of the image.
- [var extent: CGRect](ciimage/extent.md)
  A rectangle that specifies the extent of the image.
- [var properties: [String : Any]](ciimage/properties.md)
  Returns the metadata properties dictionary of the image.
- [var colorSpace: CGColorSpace?](ciimage/colorspace.md)
  The color space of the image.
- [func orientationTransform(forExifOrientation: Int32) -> CGAffineTransform](ciimage/orientationtransform(forexiforientation:).md)
  Returns the transformation needed to reorient the image to the specified orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/url)*