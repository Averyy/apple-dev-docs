# properties

**Framework**: Core Image  
**Kind**: instp

A dictionary containing metadata about the image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var properties: [String : Any] { get }
```

#### Discussion

If the [`CIImage`](ciimage.md) object is the output of a filter (or filter chain), this property’s value is the metadata from the filter’s original input image.

## See Also

- [var definition: CIFilterShape](ciimage/1437804-definition.md)
  Returns a filter shape object that represents the domain of definition of the image.
- [var extent: CGRect](ciimage/1437996-extent.md)
  A rectangle that specifies the extent of the image.
- [var url: URL?](ciimage/1438195-url.md)
  The URL from which the image was loaded.
- [var colorSpace: CGColorSpace?](ciimage/1437750-colorspace.md)
  The color space of the image.
- [func orientationTransform(forExifOrientation: Int32) -> CGAffineTransform](ciimage/1437930-orientationtransform.md)
  Returns the transformation needed to reorient the image to the specified orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/1437733-properties)*