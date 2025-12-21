# imageCropAndScaleOption

**Framework**: Vision  
**Kind**: property

An optional setting that tells the Vision algorithm how to scale an input image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var imageCropAndScaleOption: VNImageCropAndScaleOption { get set }
```

#### Discussion

Scaling an image ensures that the entire image fits into the algorithm’s input image dimensions, which may require a change in aspect ratio. Each crop-and-scale option transforms the input image in a different way.

![A series of six photos that show the effects of applying a center crop, scale fit, scale fill, scale fit rotate 90 degrees counterclockwise, and scale fill rotate 90 degrees counterclockwise option to the original input image.](https://docs-assets.developer.apple.com/published/f364baac9c906e2c98ec66ee3b303aab/scale-crop-options%402x.png)

## See Also

- [enum VNImageCropAndScaleOption](vnimagecropandscaleoption.md)
  Options that define how Vision crops and scales an input-image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncoremlrequest/imagecropandscaleoption)*