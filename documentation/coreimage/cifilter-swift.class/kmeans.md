# kMeans()

**Framework**: Core Image  
**Kind**: method

Applies the k-means algorithm to find the most common colors in an image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func kMeans() -> any CIFilter & CIKMeans
```

#### Return Value

A one-dimensional [`CIImage`](ciimage.md) containing the colors.

#### Discussion

This filter uses the k-means clustering algorithm to find the most common colors in an input image. The result is a [`CIImage`](ciimage.md) with `count` x 1 dimensions. Each `RGBA` pixel in the result image represents the center of a k-means cluster. The `RGB` components contain the color and the alpha component represents the weight of the color. You typically use the [`kMeans()`](cifilter-swift.class/kmeans().md) filter in conjunction with the [`palettize()`](cifilter-swift.class/palettize().md) filter to produce an image with a reduced number of colors.

> 💡 **Tip**:  The colors in the result of the [`kMeans()`](cifilter-swift.class/kmeans().md) filter have an alpha component that indicates the weight of the color. You should set this value one using [`settingAlphaOne(in:)`](ciimage/settingalphaone(in:).md) before using the palette.

The following code example uses the [`kMeans()`](cifilter-swift.class/kmeans().md) filter followed by the [`palettize()`](cifilter-swift.class/palettize().md) filter to reduce the colors in the image to four:

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

![Three images arranged horizontally. The image on the left is a closeup photograph of a cactus. The center image consists of squares arranged vertically showing the four main colors from the left image. The image on the right shows the image with the reduced colors.](https://docs-assets.developer.apple.com/published/ad1e4bae35fc0ae11f29b1c1b52fcb6e/media-4332587%402x.png)

## See Also

- [class func areaAverage() -> any CIFilter & CIAreaAverage](cifilter-swift.class/areaaverage.md)
  Returns a 1 x 1 pixel image that contains the average color for the region of interest.
- [class func areaHistogram() -> any CIFilter & CIAreaHistogram](cifilter-swift.class/areahistogram.md)
  Returns a histogram of a specified area of the image.
- [class func areaLogarithmicHistogram() -> any CIFilter & CIAreaLogarithmicHistogram](cifilter-swift.class/arealogarithmichistogram.md)
  Returns a logarithmic histogram of a specified area of the image.
- [class func areaMaximum() -> any CIFilter & CIAreaMaximum](cifilter-swift.class/areamaximum.md)
  Calculates the maximum color components of a specified area of the image.
- [class func areaMaximumAlpha() -> any CIFilter & CIAreaMaximumAlpha](cifilter-swift.class/areamaximumalpha.md)
  Finds the pixel with the highest alpha value.
- [class func areaMinimum() -> any CIFilter & CIAreaMinimum](cifilter-swift.class/areaminimum.md)
  Calculates the minimum color component values for a specified area of the image.
- [class func areaMinimumAlpha() -> any CIFilter & CIAreaMinimumAlpha](cifilter-swift.class/areaminimumalpha.md)
  Calculates the pixel within a specified area that has the smallest alpha value.
- [class func areaMinMax() -> any CIFilter & CIAreaMinMax](cifilter-swift.class/areaminmax.md)
  Calculates minimum and maximum color components for a specified area of the image.
- [class func areaMinMaxRed() -> any CIFilter & CIAreaMinMaxRed](cifilter-swift.class/areaminmaxred.md)
  Calculates the minimum and maximum red component value.
- [class func columnAverage() -> any CIFilter & CIColumnAverage](cifilter-swift.class/columnaverage.md)
  Calculates the average color for a specified column of an image.
- [class func histogramDisplay() -> any CIFilter & CIHistogramDisplay](cifilter-swift.class/histogramdisplay.md)
  Generates a histogram map from the image.
- [class func rowAverage() -> any CIFilter & CIRowAverage](cifilter-swift.class/rowaverage.md)
  Calculates the average color for the specified row of pixels in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/kmeans())*