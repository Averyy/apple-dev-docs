# kMeans()

**Framework**: Core Image  
**Kind**: clm

Applies the k-means algorithm to find the most common colors in an image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func kMeans() -> any CIFilter & CIKMeans
```

#### Return_value

A one-dimensional [`CIImage`](ciimage.md) containing the colors.

#### Discussion

This filter uses the k-means clustering algorithm to find the most common colors in an input image. The result is a [`CIImage`](ciimage.md) with `count` x 1 dimensions. Each `RGBA` pixel in the result image represents the center of a k-means cluster. The `RGB` components contain the color and the alpha component represents the weight of the color. You typically use the [`kMeans()`](cifilter/3547110-kmeans.md) filter in conjunction with the [`palettize()`](cifilter/3228378-palettize.md) filter to produce an image with a reduced number of colors.

> 💡 **Tip**: The colors in the result of the [`kMeans()`](cifilter/3547110-kmeans.md) filter have an alpha component that indicates the weight of the color. You should set this value one using [`settingAlphaOne(in:)`](ciimage/1645891-settingalphaone.md) before using the palette.

The colors in the result of the [`kMeans()`](cifilter/3547110-kmeans.md) filter have an alpha component that indicates the weight of the color. You should set this value one using [`settingAlphaOne(in:)`](ciimage/1645891-settingalphaone.md) before using the palette.

The following code example uses the [`kMeans()`](cifilter/3547110-kmeans.md) filter followed by the [`palettize()`](cifilter/3228378-palettize.md) filter to reduce the colors in the image to four:

```swift
func kMeans(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.kMeans()
    filter.inputImage = inputImage
    filter.extent = inputImage.extent
    filter.count = 4
    filter.passes = 5
    return filter.outputImage!
}

func palettize(inputImage: CIImage, paletteImage: CIImage) -> CIImage {
    let palettize = CIFilter.palettize()
    palettize.inputImage = inputImage
    palettize.paletteImage = paletteImage
    return palettize.outputImage!
}

let palette = kMeans(inputImage: image)
let palettized = palettize(inputImage: image, palette.settingAlphaOne(in: palette.extent))
```

![Three images arranged horizontally. The image on the left is a closeup photograph of a cactus. The center image consists of squares arranged vertically showing the four main colors from the left image. The image on the right shows the image with the reduced colors.](https://docs-assets.developer.apple.com/published/26ae0752d4/rendered2x-1708099650.png)

## See Also

- [class func areaAverage() -> any CIFilter & CIAreaAverage](cifilter/3547111-areaaverage.md)
  Returns a 1 x 1 pixel image that contains the average color for the region of interest.
- [class func areaHistogram() -> any CIFilter & CIAreaHistogram](cifilter/3547112-areahistogram.md)
  Returns a histogram of a specified area of the image.
- [class func areaLogarithmicHistogram() -> any CIFilter & CIAreaLogarithmicHistogram](cifilter/4401848-arealogarithmichistogram.md)
  Returns a logarithmic histogram of a specified area of the image.
- [class func areaMaximum() -> any CIFilter & CIAreaMaximum](cifilter/3547114-areamaximum.md)
  Calculates the maximum color components of a specified area of the image.
- [class func areaMaximumAlpha() -> any CIFilter & CIAreaMaximumAlpha](cifilter/3547113-areamaximumalpha.md)
  Finds the pixel with the highest alpha value.
- [class func areaMinimum() -> any CIFilter & CIAreaMinimum](cifilter/3547118-areaminimum.md)
  Calculates the minimum color component values for a specified area of the image.
- [class func areaMinimumAlpha() -> any CIFilter & CIAreaMinimumAlpha](cifilter/3547117-areaminimumalpha.md)
  Calculates the pixel within a specified area that has the smallest alpha value.
- [class func areaMinMax() -> any CIFilter & CIAreaMinMax](cifilter/3547115-areaminmax.md)
  Calculates minimum and maximum color components for a specified area of the image.
- [class func areaMinMaxRed() -> any CIFilter & CIAreaMinMaxRed](cifilter/3547116-areaminmaxred.md)
  Calculates the minimum and maximum red component value.
- [class func columnAverage() -> any CIFilter & CIColumnAverage](cifilter/3547121-columnaverage.md)
  Calculates the average color for a specified column of an image.
- [class func histogramDisplay() -> any CIFilter & CIHistogramDisplay](cifilter/3547122-histogramdisplay.md)
  Generates a histogram map from the image.
- [class func rowAverage() -> any CIFilter & CIRowAverage](cifilter/3547123-rowaverage.md)
  Calculates the average color for the specified row of pixels in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/3547110-kmeans)*