# areaMinimumAlpha()

**Framework**: Core Image  
**Kind**: method

Calculates the pixel within a specified area that has the smallest alpha value.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func areaMinimumAlpha() -> any CIFilter & CIAreaMinimumAlpha
```

#### Return Value

A 1 x 1 pixel image containing the color with the smallest alpha value.

#### Discussion

This method applies the area minimum alpha filter to an image. This effect finds and returns the pixel with the lowest alpha value in the region defined by `extent`.

The area minimum alpha filter uses the following properties:

The following code creates a filter that results in a 1 x 1 pixel image containing the color with the lowest alpha value:

```swift
func areaMinimumAlpha(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.areaMinimumAlpha()
    filter.inputImage = inputImage
    filter.extent = CGRect(
        x: inputImage.extent.width/2-250,
        y: inputImage.extent.height/2-250,
        width: 500,
        height: 500)
     return filter.outputImage!
}
```

![Two images side by side arranged horizontally. The left image is a photograph of a modern brick building. An outlined square highlights a 500 x 500 pixel region in the image. The right image contains the result of running the area minimum alpha filter. It contains the color from the highlighted square that has the minimum alpha value.](https://docs-assets.developer.apple.com/published/e28011419e03c28b85437191b4877b88/media-4332169%402x.png)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/areaminimumalpha())*