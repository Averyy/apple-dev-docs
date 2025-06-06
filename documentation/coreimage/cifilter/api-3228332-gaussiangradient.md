# gaussianGradient()

**Framework**: Core Image  
**Kind**: clm

Generates a gradient that varies from one color to another using a Gaussian distribution.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func gaussianGradient() -> any CIFilter & CIGaussianGradient
```

#### Return_value

The generated image.

#### Discussion

This method generates a Gaussian gradient image. The effect uses the Gaussian kernel to calculate the even dispersal of the first color in the center to the second color in the image’s periphery.

The Gaussian gradient filter uses the following properties:

The following code creates a filter that generates a gradient image:

```swift
func gaussian() -> CIImage {
    let gaussianGradient = CIFilter.gaussianGradient()
    gaussianGradient.center = CGPoint (x: 150, y: 150)
    gaussianGradient.color0 = CIColor(red: 88/255, green: 201
/255, blue: 175/255)
    gaussianGradient.color1 = CIColor(red: 153/255, green: 153/255, blue: 204/255)
    gaussianGradient.radius = 10
    return gaussianGradient.outputImage!
}
```

![A photo of a Gaussian gradient that gradually changes in color from purple in the center and shifts to light blue in the periphery.](https://docs-assets.developer.apple.com/published/55ba95dcf6/rendered2x-1583863315.png)

## See Also

- [class func hueSaturationValueGradient() -> any CIFilter & CIHueSaturationValueGradient](cifilter/3228342-huesaturationvaluegradient.md)
  Generates a gradient representing a specified color space.
- [class func linearGradient() -> any CIFilter & CILinearGradient](cifilter/3228351-lineargradient.md)
  Generates a color gradient that varies along a linear axis between two defined endpoints.
- [class func radialGradient() -> any CIFilter & CIRadialGradient](cifilter/3228395-radialgradient.md)
  Generates a gradient that varies radially between two circles having the same center.
- [class func smoothLinearGradient() -> any CIFilter & CISmoothLinearGradient](cifilter/3228407-smoothlineargradient.md)
  Generates a gradient that blends colors along a linear axis between two defined endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/3228332-gaussiangradient)*