# areaLogarithmicHistogram()

**Framework**: Core Image  
**Kind**: clm

Returns a logarithmic histogram of a specified area of the image.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.5+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class func areaLogarithmicHistogram() -> any CIFilter & CIAreaLogarithmicHistogram
```

#### Return_value

A 1-pixel-high image containing the calculated histogram`.`

#### Discussion

This filter calculates histograms of the `red,``green,``blue,` and `alpha` colors for the specified area of an image. A base two-logarithm function is applied to the values before binning. The `count` property controls the number of bins (or width) of the histogram. The histogram is scaled so that all the values sum to `scale`. 

The following code creates a filter that results in a 1-pixel-tall image with a width of 256. The pixel color components contain the logarithmic histogram values:

```swift
func areaLogarithmicHistogram(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.areaLogarithmicHistogram()
    filter.inputImage = inputImage
    filter.count = 256
    filter.scale = 15
    filter.extent = CGRect(
        x: inputImage.extent.width/2-250,
        y: inputImage.extent.height/2-250,
        width: 500,
        height: 500)
    return filter.outputImage!
}
```

Use the [`histogramDisplay()`](cifilter/3547122-histogramdisplay.md) filter to display the histogram:

```swift
func logarithmicHistogramDisplay(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.histogramDisplay()
    filter.inputImage = areaLogarithmicHistogram(inputImage: inputImage)
    filter.highLimit = 1
    filter.height = 100
    filter.lowLimit = 0
    return filter.outputImage!
}
```

![Two images arranged horizontally. The image on the left contains a photograph of a vineyard. The lower third of the image contains gravel with a deep shadow in the foreground. The middle of the image shows the vineyard receding into the distance. The top of the image shows a partially cloudy sky. The image on the right shows the result of the logarithmic histogram display filter. There are three overlayed charts showing the histogram of the red, green and blue components.](https://docs-assets.developer.apple.com/published/66820fd19e/rendered2x-1708351134.png)

## See Also

- [class func areaAverage() -> any CIFilter & CIAreaAverage](cifilter/3547111-areaaverage.md)
  Returns a 1 x 1 pixel image that contains the average color for the region of interest.
- [class func areaHistogram() -> any CIFilter & CIAreaHistogram](cifilter/3547112-areahistogram.md)
  Returns a histogram of a specified area of the image.
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
- [class func kMeans() -> any CIFilter & CIKMeans](cifilter/3547110-kmeans.md)
  Applies the k-means algorithm to find the most common colors in an image.
- [class func rowAverage() -> any CIFilter & CIRowAverage](cifilter/3547123-rowaverage.md)
  Calculates the average color for the specified row of pixels in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/4401848-arealogarithmichistogram)*