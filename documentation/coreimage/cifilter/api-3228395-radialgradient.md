# radialGradient()

**Framework**: Core Image  
**Kind**: clm

Generates a gradient that varies radially between two circles having the same center.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func radialGradient() -> any CIFilter & CIRadialGradient
```

#### Return_value

The generated image.

#### Discussion

This method generates a radial-gradient image. The effect generates a color shift between the `radius0` and `radius1` properties. 

The radial-gradient filter uses the following properties:

The following code creates a filter that generates a gradient image:

```swift
func radial() -> CIImage {
    let radialGradient = CIFilter.radialGradient()
    radialGradient.center = CGPoint(x: 150, y: 150)
    radialGradient.radius0 = 5
    radialGradient.radius1 = 100
    radialGradient.color0 = CIColor(red: 246/255, green: 145/255, blue: 181/255)
    radialGradient.color1 = CIColor(red: 110/255, green: 81/255, blue: 161/255)
    return radialGradient.outputImage!
}
```

![An image that gradually changes in color from pink in the center to purple in the periphery.](https://docs-assets.developer.apple.com/published/5f45288f40/rendered2x-1583863323.png)

## See Also

- [class func gaussianGradient() -> any CIFilter & CIGaussianGradient](cifilter/3228332-gaussiangradient.md)
  Generates a gradient that varies from one color to another using a Gaussian distribution.
- [class func hueSaturationValueGradient() -> any CIFilter & CIHueSaturationValueGradient](cifilter/3228342-huesaturationvaluegradient.md)
  Generates a gradient representing a specified color space.
- [class func linearGradient() -> any CIFilter & CILinearGradient](cifilter/3228351-lineargradient.md)
  Generates a color gradient that varies along a linear axis between two defined endpoints.
- [class func smoothLinearGradient() -> any CIFilter & CISmoothLinearGradient](cifilter/3228407-smoothlineargradient.md)
  Generates a gradient that blends colors along a linear axis between two defined endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/3228395-radialgradient)*