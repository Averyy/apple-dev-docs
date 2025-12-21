# imageCropAndScaleOption

**Framework**: Vision  
**Kind**: property

An optional setting that tells the algorithm how to scale an input image before generating the feature print.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var imageCropAndScaleOption: VNImageCropAndScaleOption { get set }
```

#### Discussion

Scaling is applied before generating the feature print. The default value is [`VNImageCropAndScaleOption.scaleFill`](vnimagecropandscaleoption/scalefill.md).

Scaling an image ensures that the entire image fits into the algorithm’s input image dimensions, which may require a change in aspect ratio. Each crop and scale option transforms the input image in a different way:

![A photo of a flower cropped and scaled according to Vision image options](https://docs-assets.developer.apple.com/published/f364baac9c906e2c98ec66ee3b303aab/scale-crop-options%402x.png)

## See Also

- [enum VNImageCropAndScaleOption](vnimagecropandscaleoption.md)
  Options that define how Vision crops and scales an input-image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vngenerateimagefeatureprintrequest/imagecropandscaleoption)*