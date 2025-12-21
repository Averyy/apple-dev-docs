# colorCubeWithColorSpace()

**Framework**: Core Image  
**Kind**: method

Adjusts an image’s pixels using a three-dimensional color table in specified color space.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func colorCubeWithColorSpace() -> any CIFilter & CIColorCubeWithColorSpace
```

#### Return Value

The modified image.

#### Discussion

This method applies the color cube with color space filter to an image. The effect applies a mapping from `rgb` space within the color space defined to color values the cubeData defines. For each pixel, it matches the data and adjusts the color on the output image.

The color cube with color space filter uses the following properties:

The following code creates a filter that adds brightness to the input image:

```swift
func colorCube(inputImage: CIImage, cubeData: Data) -> CIImage {
    let colorCubeEffect = CIFilter.colorCubeWithColorSpace()
    colorCubeEffect.inputImage = inputImage
    colorCubeEffect.colorSpace = CGColorSpaceCreateDeviceRGB()
    colorCubeEffect.cubeData = cubeData
    colorCubeEffect.cubeDimension = 4
    return colorCubeEffect.outputImage!
}
// Create a color cube with size 4.
var colorCubeData: [Float32] = []
let size = 4
let step = 1.0 / Float32(size - 1)
for b in 0..<size {
    for g in 0..<size {
        for r in 0..<size {
            // Calculate the normalized color component values.
            let redNormalised = Float32(r) * step
            let greenNormalised = Float32(g) * step
            let blueNormalised = Float32(b) * step
            let red = pow(redNormalised, 0.5)
            let green = pow(greenNormalised, 0.5)
            let blue = pow(blueNormalised, 0.5)
            let alpha: Float = 1.0
            colorCubeData.append(contentsOf: [red, green, blue, alpha])
        }
    }
}
let cubeData = Data(bytes:colorCubeData, count: colorCubeData.count*4)
let result = colorCube(inputImage: ciImage, cubeData: cubeData)
```

![Two pictures of a pink flower surrounded by foliage. The photo on the left shows a single flower photographed close-up, in focus, with good light and no effects. In the photo on the right, a color cube with color space filter is applied, resulting in the photo becoming lighter and the flower becoming darker.](https://docs-assets.developer.apple.com/published/0d8b301bc3f49b8387ed6c820e74dfe0/media-3545016%402x.png)

## See Also

- [class func colorCrossPolynomial() -> any CIFilter & CIColorCrossPolynomial](cifilter-swift.class/colorcrosspolynomial.md)
  Adjusts an image’s color by applying polynomial cross-products.
- [class func colorCube() -> any CIFilter & CIColorCube](cifilter-swift.class/colorcube.md)
  Adjusts an image’s pixels using a three-dimensional color table.
- [class func colorCubesMixedWithMask() -> any CIFilter & CIColorCubesMixedWithMask](cifilter-swift.class/colorcubesmixedwithmask.md)
  Alters an image’s pixels using a three-dimensional color tables and a mask image.
- [class func colorCurves() -> any CIFilter & CIColorCurves](cifilter-swift.class/colorcurves.md)
  Adjusts an image’s color curves.
- [class func colorInvert() -> any CIFilter & CIColorInvert](cifilter-swift.class/colorinvert.md)
  Inverts an image’s colors.
- [class func colorMap() -> any CIFilter & CIColorMap](cifilter-swift.class/colormap.md)
  Performs a transformation of the input image colors to colors from a gradient image.
- [class func colorMonochrome() -> any CIFilter & CIColorMonochrome](cifilter-swift.class/colormonochrome.md)
  Adjusts an image’s colors to shades of a single color.
- [class func colorPosterize() -> any CIFilter & CIColorPosterize](cifilter-swift.class/colorposterize.md)
  Flattens an image’s colors.
- [class func convertLabToRGB() -> any CIFilter & CIConvertLab](cifilter-swift.class/convertlabtorgb.md)
  Converts an image from CIELAB to RGB color space.
- [class func convertRGBtoLab() -> any CIFilter & CIConvertLab](cifilter-swift.class/convertrgbtolab.md)
  Converts an image from RGB to CIELAB color space.
- [class func dither() -> any CIFilter & CIDither](cifilter-swift.class/dither.md)
  Applies randomized noise to produce a processed look.
- [class func documentEnhancer() -> any CIFilter & CIDocumentEnhancer](cifilter-swift.class/documentenhancer.md)
  Adjusts an image’s shadows and contrast.
- [class func falseColor() -> any CIFilter & CIFalseColor](cifilter-swift.class/falsecolor.md)
  Replaces an image’s colors with specified colors.
- [class func labDeltaE() -> any CIFilter & CILabDeltaE](cifilter-swift.class/labdeltae.md)
  Compares an image’s color values.
- [class func maskToAlpha() -> any CIFilter & CIMaskToAlpha](cifilter-swift.class/masktoalpha.md)
  Converts an image to a white image with an alpha component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/colorcubewithcolorspace())*