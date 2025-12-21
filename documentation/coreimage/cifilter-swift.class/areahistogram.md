# areaHistogram()

**Framework**: Core Image  
**Kind**: method

Returns a histogram of a specified area of the image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func areaHistogram() -> any CIFilter & CIAreaHistogram
```

#### Return Value

A 1 pixel high image containing the calculated histogram`.`

#### Discussion

This filter calculates histograms of the red, green, blue, and alpha colors in the region defined by `extent`. The `count` property controls the number of bins (or width) of the histogram. The filter scales the histogram so that the total of all the counts in the bins equals `scale`.

The area histogram filter uses the following properties:

The following code creates a filter that results in an image that has a height of 1 pixel and a width of 256 pixels. The pixel color components contain the histogram values.

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
```

To display the histogram, you can use the [`histogramDisplay()`](cifilter-swift.class/histogramdisplay().md) filter:

```swift
func histogramDisplay(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.histogramDisplay()
    filter.inputImage = areaHistogram(inputImage: inputImage)
    filter.highLimit = 1
    filter.height = 100
    filter.lowLimit = 0
    return filter.outputImage!
}

```

![Two images arranged horizontally. The left image contains a photograph of three hydrangea flowers with leaves in the background. The image on the right shows the result of the histogram display filter. There are three overlaid charts showing the histogram of the red, green, and blue components.](https://docs-assets.developer.apple.com/published/d97a604d980184e6a74406d6098a21b4/media-4332392%402x.png)

## See Also

- [class func areaAverage() -> any CIFilter & CIAreaAverage](cifilter-swift.class/areaaverage.md)
  Returns a 1 x 1 pixel image that contains the average color for the region of interest.
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
- [class func kMeans() -> any CIFilter & CIKMeans](cifilter-swift.class/kmeans.md)
  Applies the k-means algorithm to find the most common colors in an image.
- [class func rowAverage() -> any CIFilter & CIRowAverage](cifilter-swift.class/rowaverage.md)
  Calculates the average color for the specified row of pixels in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/areahistogram())*