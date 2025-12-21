# convolutionRGB9Horizontal()

**Framework**: Core Image  
**Kind**: method

Applies a convolution 9 x 1 filter to the RGB components of an image.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class func convolutionRGB9Horizontal() -> any CIFilter & CIConvolution
```

#### Return Value

The convolved image.

#### Discussion

This method applies a 9 x 1 convolution to the `RGB` components of an image. The effect uses a 9 x 1 area surrounding an input pixel, the pixel itself, and those within a distance of 4 pixels horizontally. The effect repeats this for every pixel within the image. Unlike the convolution filters, which use square matrices, this filter can only produce effects along a vertical axis. You can combine this filter with the [`convolutionRGB9Vertical()`](cifilter-swift.class/convolutionrgb9vertical().md) to apply separable 9 x 9 convolutions. This filter differs from the [`convolution9Horizontal()`](cifilter-swift.class/convolution9horizontal().md) filter, which processes all of the color components including the alpha component.

The convolution-RGB-9-vertical filter uses the following properties:

> **Note**:  When using a nonzero `bias` value, the output image has an infinite extent. You should crop the image before attempting to render it.

The following code creates a filter that blurs the image in the horizontal direction:

```swift
func convolutionRGB9Horizontal(inputImage: CIImage) -> CIImage {
    let convolutionFilter = CIFilter.convolutionRGB9Horizontal()
    convolutionFilter.inputImage = inputImage
    let weights: [CGFloat] = [1, 1, 1, 1, 1, 1, 1, 1, 1].map { $0/9.0 }
    let kernel = CIVector(values: weights, count: 9)
    convolutionFilter.weights = kernel
    convolutionFilter.bias = 0.0
    return convolutionFilter.outputImage!
}
```

![Two images arranged horizontally. The left image contains a photo of the Golden Gate Bridge with a clear sky as the background. The right image shows the result of applying a horizontal convolution kernel that blurs the image. Fine detail in the horizontal direction is blurred.](https://docs-assets.developer.apple.com/published/3ec68c7a5b27c365d4a22f7cee1473ad/media-4407285%402x.png)

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
- [class func convolutionRGB5X5() -> any CIFilter & CIConvolution](cifilter-swift.class/convolutionrgb5x5.md)
  Applies a convolution 5 x 5 filter to the `RGB` components of an image.
- [class func convolutionRGB7X7() -> any CIFilter & CIConvolution](cifilter-swift.class/convolutionrgb7x7.md)
  Applies a convolution 7 x 7 filter to the RGB components of an image.
- [class func convolutionRGB9Vertical() -> any CIFilter & CIConvolution](cifilter-swift.class/convolutionrgb9vertical.md)
  Applies a convolution 1 x 9 filter to the RGB components of an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/convolutionrgb9horizontal())*