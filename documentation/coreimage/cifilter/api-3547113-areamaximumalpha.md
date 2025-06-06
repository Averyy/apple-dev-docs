# areaMaximumAlpha()

**Framework**: Core Image  
**Kind**: clm

Finds the pixel with the highest alpha value.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func areaMaximumAlpha() -> any CIFilter & CIAreaMaximumAlpha
```

#### Return_value

A 1 x 1 size image containing the pixel with the maximum alpha value.

#### Discussion

This filter returns the pixel with highest alpha value in the region defined by `extent`. 

The area maximum alpha filter uses the following properties:

The following code creates a filter that results in a single pixel image containing the pixel with the highest alpha value:

```swift
func areaMaximumAlpha(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.areaMaximumAlpha()
    filter.inputImage = inputImage
    filter.extent = CGRect(
        x: inputImage.extent.width/2-250,
        y: inputImage.extent.height/2-250,
        width: 500,
        height: 500)
    return filter.outputImage!
}
```

![Two images side by side arranged horizontally. The left image is a photograph of a modern brick building. A square outline highlights a 500 x 500 pixel region in the image. The right image contains the result of running the area maximum alpha filter. It contains the color with the highest alpha value from the highlighted square.](https://docs-assets.developer.apple.com/published/286e18fc4e/rendered2x-1707835545.png)

## See Also

- [class func areaAverage() -> any CIFilter & CIAreaAverage](cifilter/3547111-areaaverage.md)
  Returns a 1 x 1 pixel image that contains the average color for the region of interest.
- [class func areaHistogram() -> any CIFilter & CIAreaHistogram](cifilter/3547112-areahistogram.md)
  Returns a histogram of a specified area of the image.
- [class func areaLogarithmicHistogram() -> any CIFilter & CIAreaLogarithmicHistogram](cifilter/4401848-arealogarithmichistogram.md)
  Returns a logarithmic histogram of a specified area of the image.
- [class func areaMaximum() -> any CIFilter & CIAreaMaximum](cifilter/3547114-areamaximum.md)
  Calculates the maximum color components of a specified area of the image.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/3547113-areamaximumalpha)*