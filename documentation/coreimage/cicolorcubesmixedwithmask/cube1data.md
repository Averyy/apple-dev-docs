# cube1Data

**Framework**: Core Image  
**Kind**: property  
**Required**: Yes

The cube texture data to use as a color lookup table.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var cube1Data: Data { get set }
```

#### Discussion

This filter maps color values in the input image to new color values using a three-dimensional color lookup table. For each RGBA pixel in the input image, the filter uses the R, G, and B component values as indices to identify a location in the table; the RGBA value at that location becomes the RGBA value of the output pixel.

Use the [`cubeData`](cicolorcube/cubedata.md) parameter to provide data formatted for use as a color lookup table, and the inputCubeDimension parameter to specify the size of the table. This data should be an array of texel values in 32-bit floating-point RGBA linear premultiplied format. The inputCubeDimension parameter identifies the size of the cube by specifying the length of one side, so the size of the array should be [`cubeDimension`](cicolorcube/cubedimension.md) cubed times the size of a single texel value. In the color table, the R component varies fastest, followed by G, then B.

## See Also

- [var colorSpace: CGColorSpace?](cicolorcubesmixedwithmask/colorspace.md)
  The working color space.
- [var cube0Data: Data](cicolorcubesmixedwithmask/cube0data.md)
  The cube texture data to use as a color lookup table.
- [var cubeDimension: Float](cicolorcubesmixedwithmask/cubedimension.md)
  The length, in texels, of each side of the cube texture.
- [var inputImage: CIImage?](cicolorcubesmixedwithmask/inputimage.md)
  The image to use as an input image.
- [var maskImage: CIImage?](cicolorcubesmixedwithmask/maskimage.md)
  A masking image.
- [var extrapolate: Bool](cicolorcubesmixedwithmask/extrapolate.md)
  If true, then the filter extrapolates the color cube for any RGB component values outside the range 0.0 to 1.0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolorcubesmixedwithmask/cube1data)*