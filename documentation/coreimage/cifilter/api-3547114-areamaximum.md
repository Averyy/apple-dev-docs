# areaMaximum()

**Framework**: Core Image  
**Kind**: clm

Calculates the maximum color components of a specified area of the image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func areaMaximum() -> any CIFilter & CIAreaMaximum
```

#### Return_value

A 1 x 1 size image containing the maximum color components.

#### Discussion

This filter returns the maximum color components in the region defined by `extent`.

The area maximum filter uses the following properties:.

The following code creates a filter that calculates the maximum color components of a 500 x 500 set of pixels from the center of the image:

```swift
func areaMaximum(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.areaMaximum()
    filter.inputImage = inputImage
    filter.extent = CGRect(
        x: inputImage.extent.width/2,
        y: inputImage.extent.height/2,
        width: 100,
        height: 100)
     return filter.outputImage!
}
```

![Two images arranged horizontally. The left image contains a photograph of three hydrangea flowers with leaves in the background. A 500 x 500 pixel square in the center of the image is highlighted using an outlined box. The image on the right shows the result of applying the area maximum filter to the 500 x 500 pixel square. The result is a 1 x 1 pixel image containing a color made up of the maximum color components from the highlighted square.](https://docs-assets.developer.apple.com/published/ea9700be83/rendered2x-1707832721.png)

## See Also

- [class func areaAverage() -> any CIFilter & CIAreaAverage](cifilter/3547111-areaaverage.md)
  Returns a 1 x 1 pixel image that contains the average color for the region of interest.
- [class func areaHistogram() -> any CIFilter & CIAreaHistogram](cifilter/3547112-areahistogram.md)
  Returns a histogram of a specified area of the image.
- [class func areaLogarithmicHistogram() -> any CIFilter & CIAreaLogarithmicHistogram](cifilter/4401848-arealogarithmichistogram.md)
  Returns a logarithmic histogram of a specified area of the image.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/3547114-areamaximum)*