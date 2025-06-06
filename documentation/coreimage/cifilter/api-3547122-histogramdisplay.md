# histogramDisplay()

**Framework**: Core Image  
**Kind**: clm

Generates a histogram map from the image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func histogramDisplay() -> any CIFilter & CIHistogramDisplay
```

#### Return_value

The generated image.

#### Discussion

This method applies the histogram display filter to the result of the output from the [`areaHistogram()`](cifilter/3547112-areahistogram.md) filter. This effect shows a graphical representation of the tonal distribution of colors in the image. 

The histogram display filter uses the following properties:

The following code creates a filter that results in a histogram diagram generated from the input image:

```swift
func areaHistogram(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.areaHistogram()
    filter.inputImage = inputImage
    filter.count = 256
    filter.scale = 50
    filter.extent = CGRect(
        x: inputImage.extent.width/2-250,
        y: inputImage.extent.height/2-250,
        width: 500,
        height: 500)
    return filter.outputImage!
}

func histogramDisplay(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.histogramDisplay()
    filter.inputImage = areaHistogram(inputImage: inputImage)
    filter.highLimit = 1
    filter.height = 100
    filter.lowLimit = 0
    return filter.outputImage!
}
```

![Two images side by side horizontally. The left image is a modern building with white concrete and tinted glass windows with a clear sky in the background. The right image is the result of applying the histogram display filter to the output of the area histogram filter. There are three overlaid charts representing the histograms for the red, green, and blue components.](https://docs-assets.developer.apple.com/published/634bab7c44/rendered2x-1707837196.png)

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
- [class func kMeans() -> any CIFilter & CIKMeans](cifilter/3547110-kmeans.md)
  Applies the k-means algorithm to find the most common colors in an image.
- [class func rowAverage() -> any CIFilter & CIRowAverage](cifilter/3547123-rowaverage.md)
  Calculates the average color for the specified row of pixels in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/3547122-histogramdisplay)*