# colorCubesMixedWithMask()

**Framework**: Core Image  
**Kind**: clm

Alters an image’s pixels using a three-dimensional color tables and a mask image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func colorCubesMixedWithMask() -> any CIFilter & CIColorCubesMixedWithMask
```

#### Return_value

The modified image.

#### Discussion

This method applies the color cubes mixed with mask filter to an image. The effect uses two color cube tables to modify the input image. The filter uses the mask image to interpolate between the two color cubes. 

The color cubes mixed with mask filter uses the following properties:

The following code creates a filter that adds colors from the mask image and brightness to the input image:

```swift
func colorCube(inputImage: CIImage, maskImage: CIImage, cube0Data: Data, cube1Data: Data) -> CIImage {
    let colorCubeEffect = CIFilter.colorCubesMixedWithMask()
    colorCubeEffect.inputImage = inputImage
    colorCubeEffect.colorSpace = CGColorSpaceCreateDeviceRGB()
    colorCubeEffect.cube0Data = cube1Data
    colorCubeEffect.cube1Data = cube0Data
    colorCubeEffect.maskImage = maskImage
    colorCubeEffect.cubeDimension = 4
    return colorCubeEffect.outputImage!
}
var colorCube0Data: [Float32] = []
var colorCube1Data: [Float32] = []
let size = 4
let step = 1.0 / Float(size - 1)
for b in 0..<size {
    for g in 0..<size {
        for r in 0..<size {
            // Calculate the normalized color component values.
            let redNormalised = Float32(r) * step
            let greenNormalised = Float32(g) * step
            let blueNormalised = Float32(b) * step
            let alpha: Float = 1.0
            colorCube0Data.append(contentsOf: [redNormalised*1.2, greenNormalised*0.8, blueNormalised*1.2, alpha])
            colorCube1Data.append(contentsOf: [redNormalised*1.2, greenNormalised*1.15, blueNormalised*0.9, alpha])
        }
    }
}
let cube0Data = Data(bytes:colorCube0Data, count: colorCube0Data.count*4)
let cube1Data = Data(bytes:colorCube1Data, count: colorCube1Data.count*4)
let maskImage = CIFilter.linearGradient()
maskImage.color0 = CIColor(red: 1.0, green: 1.0, blue: 1.0, alpha: 1.0)
maskImage.color1 = CIColor(red: 0.0, green: 0.0, blue: 0.0, alpha: 0.0)
maskImage.point0 = CGPoint(x:0, y:0)
maskImage.point1 = CGPoint(x: ciImage.extent.width, y: 0)
let result = colorCube(inputImage: ciImage, maskImage: maskImage.outputImage!, cube0Data: cube0Data, cube1Data: cube1Data)
```

![One photograph on the left above a gradient image, and a second photograph on the right. The photograph on the left shows a single flower photographed close-up, in focus, with good light and no effects. The image below it is a gradient image displaying a gradual color change from purple to a warm orange color. The photo on the right shows the same flower image with a colorCubesMixedWithMask filter applied, resulting in a brighter photograph with colors from the gradient photo. ](https://docs-assets.developer.apple.com/published/c824b645fb/rendered2x-1583359080.png)

## See Also

- [class func colorCrossPolynomial() -> any CIFilter & CIColorCrossPolynomial](cifilter/3228286-colorcrosspolynomial.md)
  Adjusts an image’s color by applying polynomial cross-products.
- [class func colorCube() -> any CIFilter & CIColorCube](cifilter/3228287-colorcube.md)
  Adjusts an image’s pixels using a three-dimensional color table.
- [class func colorCubeWithColorSpace() -> any CIFilter & CIColorCubeWithColorSpace](cifilter/3228288-colorcubewithcolorspace.md)
  Adjusts an image’s pixels using a three-dimensional color table in specified color space.
- [class func colorCurves() -> any CIFilter & CIColorCurves](cifilter/3228290-colorcurves.md)
  Adjusts an image’s color curves.
- [class func colorInvert() -> any CIFilter & CIColorInvert](cifilter/3228292-colorinvert.md)
  Inverts an image’s colors.
- [class func colorMap() -> any CIFilter & CIColorMap](cifilter/3228293-colormap.md)
  Performs a transformation of the input image colors to colors from a gradient image.
- [class func colorMonochrome() -> any CIFilter & CIColorMonochrome](cifilter/3228295-colormonochrome.md)
  Adjusts an image’s colors to shades of a single color.
- [class func colorPosterize() -> any CIFilter & CIColorPosterize](cifilter/3228297-colorposterize.md)
  Flattens an image’s colors.
- [class func convertLabToRGB() -> any CIFilter & CIConvertLab](cifilter/4401856-convertlabtorgb.md)
  Converts an image from CIELAB to RGB color space.
- [class func convertRGBtoLab() -> any CIFilter & CIConvertLab](cifilter/4401857-convertrgbtolab.md)
  Converts an image from RGB to CIELAB color space.
- [class func dither() -> any CIFilter & CIDither](cifilter/3228315-dither.md)
  Applies randomized noise to produce a processed look.
- [class func documentEnhancer() -> any CIFilter & CIDocumentEnhancer](cifilter/3228317-documentenhancer.md)
  Adjusts an image’s shadows and contrast.
- [class func falseColor() -> any CIFilter & CIFalseColor](cifilter/3228325-falsecolor.md)
  Replaces an image’s colors with specified colors.
- [class func labDeltaE() -> any CIFilter & CILabDeltaE](cifilter/3228260-labdeltae.md)
  Compares an image’s color values.
- [class func maskToAlpha() -> any CIFilter & CIMaskToAlpha](cifilter/3228354-masktoalpha.md)
  Converts an image to a white image with an alpha component.
- [class func maximumComponent() -> any CIFilter & CIMaximumComponent](cifilter/3228356-maximumcomponent.md)
  Creates a maximum RGB grayscale image.
- [class func minimumComponent() -> any CIFilter & CIMinimumComponent](cifilter/3228360-minimumcomponent.md)
  Creates a minimum RGB grayscale image.
- [class func paletteCentroid() -> any CIFilter & CIPaletteCentroid](cifilter/3228377-palettecentroid.md)
  Calculates the location of an image’s colors.
- [class func palettize() -> any CIFilter & CIPalettize](cifilter/3228378-palettize.md)
  Replaces colors with colors from a palette image.
- [class func photoEffectChrome() -> any CIFilter & CIPhotoEffect](cifilter/3228384-photoeffectchrome.md)
  Exaggerates an image’s colors.
- [class func photoEffectFade() -> any CIFilter & CIPhotoEffect](cifilter/3228385-photoeffectfade.md)
  Diminishes an image’s colors.
- [class func photoEffectInstant() -> any CIFilter & CIPhotoEffect](cifilter/3228386-photoeffectinstant.md)
  Desaturates an image’s colors.
- [class func photoEffectMono() -> any CIFilter & CIPhotoEffect](cifilter/3228387-photoeffectmono.md)
  Adjust an image’s colors to black and white.
- [class func photoEffectNoir() -> any CIFilter & CIPhotoEffect](cifilter/3228388-photoeffectnoir.md)
  Adjusts an image’s colors to black and white and intensifies the contrast.
- [class func photoEffectProcess() -> any CIFilter & CIPhotoEffect](cifilter/3228389-photoeffectprocess.md)
  Lowers the contrast of the input image.
- [class func photoEffectTonal() -> any CIFilter & CIPhotoEffect](cifilter/3228390-photoeffecttonal.md)
  Adjusts an image’s colors to black and white.
- [class func photoEffectTransfer() -> any CIFilter & CIPhotoEffect](cifilter/3228391-photoeffecttransfer.md)
  Brightens an image’s colors.
- [class func sepiaTone() -> any CIFilter & CISepiaTone](cifilter/3228402-sepiatone.md)
  Adjusts an image’s colors to shades of brown.
- [class func thermal() -> any CIFilter & CIThermal](cifilter/3228423-thermal.md)
  Alters the image to make it look like it was taken by a thermal camera.
- [class func vignette() -> any CIFilter & CIVignette](cifilter/3228431-vignette.md)
  Gradually darkens an image’s edges.
- [class func vignetteEffect() -> any CIFilter & CIVignetteEffect](cifilter/3228430-vignetteeffect.md)
  Gradually darkens a specified area of an image.
- [class func xRay() -> any CIFilter & CIXRay](cifilter/3228433-xray.md)
  Alters an image to make it look like an X-ray image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/3228289-colorcubesmixedwithmask)*