# init(extent:format:)

**Framework**: Core Image  
**Kind**: init

Initializes an image accumulator with the specified extent and pixel format.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init?(extent: CGRect, format: CIFormat)
```

#### Return Value

The initialized image accumulator object.

## Parameters

- `extent`: A rectangle that specifies the x-value of the rectangle origin, the y-value of the rectangle origin, and the width and height.
- `format`: The format and size of each pixel. You must supply a pixel format constant, such askCIFormatARGB8  (32 bit-per-pixel, fixed-point pixel format) or kCIFormatRGBAf (128 bit-per-pixel, floating-point pixel format). See   for more information about pixel format constants.

## See Also

- [init?(extent: CGRect, format: CIFormat, colorSpace: CGColorSpace)](ciimageaccumulator/init(extent:format:colorspace:).md)
  Initializes an image accumulator with the specified extent, pixel format, and color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/init(extent:format:))*