# rowAverage()

**Framework**: Core Image  
**Kind**: clm

Calculates the average color for the specified row of pixels in an image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func rowAverage() -> any CIFilter & CIRowAverage
```

#### Return_value

#### Discussion

This method applies the row average filter to an image. This effect calculates the average color for a horizontal row over a region defined by `extent`. The height of the extent determines the width of the resulting image. The height is always 1 pixel.

The row average filter uses the following properties:

The following code creates a filter that calculates the row average for the middle section of an image:

```swift
func rowAverage(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.rowAverage()
    filter.inputImage = inputImage
    filter.extent = CGRect(x: inputImage.extent.width/3, y: 0, width: inputImage.extent.width/3, height: inputImage.extent.height)
    return filter.outputImage!
}
```

![Two images arranged horizontally side by side. The left image contains a photograph of a modern brick building. The middle of the image is highlighted by a rectangle. The right image contains the result of the row average filter applied to the highlighted region of the image. The right image has been rotated by 90 degrees and then stretched horizontally to make is easier to see. It contains colors from the highlighted region of the left image.](https://docs-assets.developer.apple.com/published/9b827e15fe/rendered2x-1707834661.png)

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
- [class func kMeans() -> any CIFilter & CIKMeans](cifilter/3547110-kmeans.md)
  Applies the k-means algorithm to find the most common colors in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/3547123-rowaverage)*