# luminosityBlendMode()

**Framework**: Core Image  
**Kind**: clm

Blends color from two images by calculating the color, hue, and saturation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func luminosityBlendMode() -> any CIFilter & CICompositeOperation
```

#### Return_value

The modified image.

#### Discussion

This method applies the luminosity-blend mode filter to an image. The effect creates the output image by using the hue and saturation values of the background image while using the luminance values of the input image.

The luminosity-blend mode filter uses the following properties:

The following code creates a filter that results in the image having accurate gray colors while other colors are added from the background image:

```swift
func luminosityBlendMode(inputImage: CIImage, backgroundImage: CIImage) -> CIImage {
    let colorBlendFilter = CIFilter.luminosityBlendMode()
    colorBlendFilter.inputImage = inputImage
    colorBlendFilter.backgroundImage = backgroundImage
    return colorBlendFilter.outputImage!
}
```

![The image on the top left shows a beach with multiple palm trees and a rainbow arching across the blue sky.  The image below is a gradient image displaying a gradual color shift from purple to a dark orange. The image on the right shows the output from applying a luminosity-blend-mode filter. The result displays brightness of the beach image and the colors of the gradient image.](https://docs-assets.developer.apple.com/published/bc09159b5e/rendered2x-1583344224.png)

## See Also

- [class func additionCompositing() -> any CIFilter & CICompositeOperation](cifilter/3228264-additioncompositing.md)
  Blends colors from two images by addition.
- [class func colorBlendMode() -> any CIFilter & CICompositeOperation](cifilter/3228282-colorblendmode.md)
  Blends color from two images using the luminance values from the background image and the hue and saturation values from the input image.
- [class func colorBurnBlendMode() -> any CIFilter & CICompositeOperation](cifilter/3228283-colorburnblendmode.md)
  Blends color from two images while darkening the image.
- [class func colorDodgeBlendMode() -> any CIFilter & CICompositeOperation](cifilter/3228291-colordodgeblendmode.md)
  Blends color from two images using dodging.
- [class func darkenBlendMode() -> any CIFilter & CICompositeOperation](cifilter/3228307-darkenblendmode.md)
  Blends colors from two images while darkening lighter pixels.
- [class func differenceBlendMode() -> any CIFilter & CICompositeOperation](cifilter/3228310-differenceblendmode.md)
  Subtracts color values to blend colors.
- [class func divideBlendMode() -> any CIFilter & CICompositeOperation](cifilter/3228316-divideblendmode.md)
  Divides color values to blend colors.
- [class func exclusionBlendMode() -> any CIFilter & CICompositeOperation](cifilter/3228323-exclusionblendmode.md)
  Subtracts color values to blend colors with less contrast.
- [class func hardLightBlendMode() -> any CIFilter & CICompositeOperation](cifilter/3228335-hardlightblendmode.md)
  Blends colors of two images by screening and multiplying.
- [class func hueBlendMode() -> any CIFilter & CICompositeOperation](cifilter/3228341-hueblendmode.md)
  Blends colors of two images by computing the sum of image color values.
- [class func lightenBlendMode() -> any CIFilter & CICompositeOperation](cifilter/3228346-lightenblendmode.md)
  Blends colors from two images by brightening colors.
- [class func linearBurnBlendMode() -> any CIFilter & CICompositeOperation](cifilter/3228349-linearburnblendmode.md)
  Blends color from two images while increasing contrast.
- [class func linearDodgeBlendMode() -> any CIFilter & CICompositeOperation](cifilter/3228350-lineardodgeblendmode.md)
  Blends colors of two images with dodging.
- [class func linearLightBlendMode() -> any CIFilter & CICompositeOperation](cifilter/4401869-linearlightblendmode.md)
  A combination of linear burn and linear dodge blend modes.
- [class func minimumCompositing() -> any CIFilter & CICompositeOperation](cifilter/3228361-minimumcompositing.md)
  Blends colors from two images by computing minimum values.
- [class func maximumCompositing() -> any CIFilter & CICompositeOperation](cifilter/3228357-maximumcompositing.md)
  Applies a maximum compositing filter to an image.
- [class func multiplyBlendMode() -> any CIFilter & CICompositeOperation](cifilter/3228370-multiplyblendmode.md)
  Blends colors from two images by multiplying color components.
- [class func multiplyCompositing() -> any CIFilter & CICompositeOperation](cifilter/3228371-multiplycompositing.md)
  Blurs the colors of two images by multiplying color components.
- [class func overlayBlendMode() -> any CIFilter & CICompositeOperation](cifilter/3228374-overlayblendmode.md)
  Blends colors by overlaying images.
- [class func pinLightBlendMode() -> any CIFilter & CICompositeOperation](cifilter/3228392-pinlightblendmode.md)
  Blends colors of two images by replacing brighter colors.
- [class func saturationBlendMode() -> any CIFilter & CICompositeOperation](cifilter/3228400-saturationblendmode.md)
  Blends the colors and saturation values of two images.
- [class func screenBlendMode() -> any CIFilter & CICompositeOperation](cifilter/3228401-screenblendmode.md)
  Blends colors of two images by multiplying colors.
- [class func softLightBlendMode() -> any CIFilter & CICompositeOperation](cifilter/3228408-softlightblendmode.md)
  Blurs the colors of two images by calculating luminance.
- [class func sourceAtopCompositing() -> any CIFilter & CICompositeOperation](cifilter/3228409-sourceatopcompositing.md)
  Overlaps two images to create one cropped image.
- [class func sourceInCompositing() -> any CIFilter & CICompositeOperation](cifilter/3228410-sourceincompositing.md)
  Subtracts non-overlapping areas of two images, resulting in one image.
- [class func sourceOutCompositing() -> any CIFilter & CICompositeOperation](cifilter/3228411-sourceoutcompositing.md)
  Subtracts overlapping area of two images to create the output image.
- [class func sourceOverCompositing() -> any CIFilter & CICompositeOperation](cifilter/3228412-sourceovercompositing.md)
  Places one image over a second image.
- [class func subtractBlendMode() -> any CIFilter & CICompositeOperation](cifilter/3228418-subtractblendmode.md)
  Blends colors by subtracting color values from two images.
- [class func vividLightBlendMode() -> any CIFilter & CICompositeOperation](cifilter/4401881-vividlightblendmode.md)
  A combination of color-burn and color-dodge blend modes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/3228353-luminosityblendmode)*