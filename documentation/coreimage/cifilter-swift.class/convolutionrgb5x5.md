# convolutionRGB5X5()

**Framework**: Core Image  
**Kind**: method

Applies a convolution 5 x 5 filter to the `RGB` components of an image.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class func convolutionRGB5X5() -> any CIFilter & CIConvolution
```

#### Return Value

This method applies a 5 x 5 convolution to the `RGB` components image. The effect uses a 5 x 5 area surrounding an input pixel, the pixel itself, and those within a distance of two pixels horizontally and vertically. The effect repeats this for every pixel within the image. The work area is then combined with the weight property vector to produce the processed image. This filter differs from the [`convolution5X5()`](cifilter-swift.class/convolution5x5().md) filter, which processes all of the color components including the alpha component.

#### Discussion

The convolution-RGB 5 x 5 filter uses the following properties:

> **Note**:  When using a nonzero `bias` value, the output image has an infinite extent. You should crop the output image before attempting to render it.

The following code creates a filter that applies an unsharp kernel to the input image:

```swift
func convolutionRGB5X5(inputImage: CIImage) -> CIImage {
    let convolutionFilter = CIFilter.convolutionRGB5X5()
    convolutionFilter.inputImage = inputImage
    let blur: [CGFloat] = [
         1, 1, 1, 1, 1,
         1, 1, 1, 1, 1,
         1, 1, 1, 1, 1,
         1, 1, 1, 1, 1,
         1, 1, 1, 1, 1,
    ].map { $0/25.0 }
    let kernel = CIVector(values: blur, count: 25)
    convolutionFilter.weights = kernel
    convolutionFilter.bias = 0
    return convolutionFilter.outputImage!
}
```

![Two images arranged horizontally. The left image contains a photo of the Golden Gate Bridge with a clear sky as the background. The right image shows the result of applying a 5 x 5 box blur convolution kernel. Fine detail in the image is now blurred.](https://docs-assets.developer.apple.com/published/fc467d006355fb073a7b6b0af38f7642/media-4407325%402x.png)

## See Also

- [class func convolution3X3() -> any CIFilter & CIConvolution](cifilter-swift.class/convolution3x3.md)
  Applies a convolution 3 x 3 filter to the `RGBA` components of an image.
- [class func convolution5X5() -> any CIFilter & CIConvolution](cifilter-swift.class/convolution5x5.md)
  Applies a convolution 5 x 5 filter to the `RGBA` components image.
- [class func convolution7X7() -> any CIFilter & CIConvolution](cifilter-swift.class/convolution7x7.md)
  Applies a convolution 7 x 7 filter to the `RGBA` color components of an image.
- [class func convolution9Horizontal() -> any CIFilter & CIConvolution](cifilter-swift.class/convolution9horizontal.md)
  Applies a convolution-9 horizontal filter to the `RGBA` components of an image.
- [class func convolution9Vertical() -> any CIFilter & CIConvolution](cifilter-swift.class/convolution9vertical.md)
  Applies a convolution-9 vertical filter to the `RGBA` components of an image.
- [class func convolutionRGB3X3() -> any CIFilter & CIConvolution](cifilter-swift.class/convolutionrgb3x3.md)
  Applies a convolution 3 x 3 filter to the `RGB` components of an image.
- [class func convolutionRGB7X7() -> any CIFilter & CIConvolution](cifilter-swift.class/convolutionrgb7x7.md)
  Applies a convolution 7 x 7 filter to the RGB components of an image.
- [class func convolutionRGB9Horizontal() -> any CIFilter & CIConvolution](cifilter-swift.class/convolutionrgb9horizontal.md)
  Applies a convolution 9 x 1 filter to the RGB components of an image.
- [class func convolutionRGB9Vertical() -> any CIFilter & CIConvolution](cifilter-swift.class/convolutionrgb9vertical.md)
  Applies a convolution 1 x 9 filter to the RGB components of an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/convolutionrgb5x5())*