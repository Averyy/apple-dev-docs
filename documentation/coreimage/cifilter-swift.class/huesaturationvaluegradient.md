# hueSaturationValueGradient()

**Framework**: Core Image  
**Kind**: method

Generates a gradient representing a specified color space.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func hueSaturationValueGradient() -> any CIFilter & CIHueSaturationValueGradient
```

#### Return Value

The generated image.

#### Discussion

This method generates a hue-saturation-value gradient image. The filter creates a color wheel that shows the hues and saturations for a specified [`CGColorSpace`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace).

The hue-saturation-value gradient uses the following properties:

The following code creates a filter that generates a color-space image:

```swift
func hueSaturationValue() -> CIImage {
    let hueSaturationValueGradient = CIFilter.hueSaturationValueGradient()
    hueSaturationValueGradient.colorSpace = CGColorSpaceCreateDeviceRGB()
    hueSaturationValueGradient.dither = 1
    hueSaturationValueGradient.radius = 100
    hueSaturationValueGradient.softness = 2
    hueSaturationValueGradient.value = 1
    return hueSaturationValueGradient.outputImage!
}
```

![A circular image containing every color in the represented colorspace.](https://docs-assets.developer.apple.com/published/4b541509a4c108f25456602cd8636210/media-3558798%402x.png)

## See Also

- [class func gaussianGradient() -> any CIFilter & CIGaussianGradient](cifilter-swift.class/gaussiangradient.md)
  Generates a gradient that varies from one color to another using a Gaussian distribution.
- [class func linearGradient() -> any CIFilter & CILinearGradient](cifilter-swift.class/lineargradient.md)
  Generates a color gradient that varies along a linear axis between two defined endpoints.
- [class func radialGradient() -> any CIFilter & CIRadialGradient](cifilter-swift.class/radialgradient.md)
  Generates a gradient that varies radially between two circles having the same center.
- [class func smoothLinearGradient() -> any CIFilter & CISmoothLinearGradient](cifilter-swift.class/smoothlineargradient.md)
  Generates a gradient that blends colors along a linear axis between two defined endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/huesaturationvaluegradient())*