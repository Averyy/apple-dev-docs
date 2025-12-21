# colorCube()

**Framework**: Core Image  
**Kind**: method

Adjusts an image’s pixels using a three-dimensional color table.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func colorCube() -> any CIFilter & CIColorCube
```

## Mentions

- [Applying a Chroma Key Effect](applying-a-chroma-key-effect.md)

#### Return Value

The modified image.

#### Discussion

This method applies the color cube filter to an image. The effect maps color values in the input image to new color values using a three-dimensional color look-up table, also called a color cube. For each `RGBA` pixel in the input image, the filter uses the pixel’s `red`, `green`, and `blue` component values to identify a location in the table. The `RGBA` value at that location becomes the `RGBA` value of the output pixel.

The color cube filter uses the following properties:

The following code creates a filter that adds a blue hue to the input image:

```swift
func colorCube(inputImage: CIImage, cubeData: Data) -> CIImage {
    let colorCubeEffect = CIFilter.colorCube()
    colorCubeEffect.inputImage = inputImage
    colorCubeEffect.cubeData = cubeData
    colorCubeEffect.cubeDimension = 4
    return colorCubeEffect.outputImage!
}
// Create a color cube with size 4.
var colorCubeData: [Float32] = []
let size = 4
let step = 1.0 / Float(size - 1)
for b in 0..<size {
    for g in 0..<size {
        for r in 0..<size {
            // Calculate the normalized color component values.
            let red = Float32(r) * step
            let green = Float32(g) * step
            // Shift the blue component to add a blue tint.
            let blue = min(1.0, Float32(b) * step + 0.5)
            let alpha: Float = 1.0
            colorCubeData.append(contentsOf: [red, green, blue, alpha])
        }
    }
}
let cubeData = Data(bytes: colorCubeData, count: colorCubeData.count * 4)
let result = colorCube(inputImage: ciImage, cubeData: cubeData)
imageView.image = UIImage(ciImage: result)
```

![Two pictures of a pink flower surrounded by foliage. The photo on the left shows a single flower photographed close-up, in focus, with good light and no effects. In the photo on the right, a color cube filter is applied, and the image has a blue hue.](https://docs-assets.developer.apple.com/published/3dc4c495b255d0d18002af18f99b7cec/media-3545026%402x.png)

## See Also

- [class func colorCrossPolynomial() -> any CIFilter & CIColorCrossPolynomial](cifilter-swift.class/colorcrosspolynomial.md)
  Adjusts an image’s color by applying polynomial cross-products.
- [class func colorCubeWithColorSpace() -> any CIFilter & CIColorCubeWithColorSpace](cifilter-swift.class/colorcubewithcolorspace.md)
  Adjusts an image’s pixels using a three-dimensional color table in specified color space.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/colorcube())*