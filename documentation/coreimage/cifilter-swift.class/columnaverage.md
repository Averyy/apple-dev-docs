# columnAverage()

**Framework**: Core Image  
**Kind**: method

Calculates the average color for a specified column of an image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func columnAverage() -> any CIFilter & CIColumnAverage
```

#### Return Value

The generated image.

#### Discussion

This method applies the column average filter to an image. This effect calculates the average color for a vertical column over a region defined by `extent`. The width of the resulting image is set by the width of the `extent`. The height of the resulting image is always 1 pixel.

The column average filter uses the following properties:

The following code creates an image containing the average values in the columns from the middle of the image:

```swift
func columnAverage(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.columnAverage()
    filter.inputImage = inputImage
    filter.extent = CGRect(x: 0, y: inputImage.extent.height/3, width: inputImage.extent.width, height: inputImage.extent.height/3)
    return filter.outputImage!
}
```

![Two images arranged horizontally side by side. The left image contains a photograph of three hydrangeas with a background of leaves. The middle of the image is highlighted by an outlined rectangle. The right image contains the result of the column average filter applied to the highlighted region of the image. The right image has been stretched vertically to make it easier to see. It contains colors from the flowers and the leaves.](https://docs-assets.developer.apple.com/published/5ae5fd7ed89eabeb7baf446be91f6f22/media-4331782%402x.png)

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
- [class func histogramDisplay() -> any CIFilter & CIHistogramDisplay](cifilter-swift.class/histogramdisplay.md)
  Generates a histogram map from the image.
- [class func kMeans() -> any CIFilter & CIKMeans](cifilter-swift.class/kmeans.md)
  Applies the k-means algorithm to find the most common colors in an image.
- [class func rowAverage() -> any CIFilter & CIRowAverage](cifilter-swift.class/rowaverage.md)
  Calculates the average color for the specified row of pixels in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/columnaverage())*