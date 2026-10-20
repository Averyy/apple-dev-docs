# VNImageCropAndScaleOption

**Framework**: Vision  
**Kind**: enum  
**Role**: Enumeration

Options that define how Vision crops and scales an input-image.

## Declaration

```swift
enum VNImageCropAndScaleOption
```

```c
enum VNImageCropAndScaleOption : NSUInteger;
```

#### Overview

Scaling an image ensures that it fits within the algorithm’s input image dimensions, which may require a change in aspect ratio. The figure below shows how each crop-and-scale option transforms the input image:

![A series of six photos that show the effects of applying a center crop, scale fit, scale fill, scale fit rotate 90 degrees counterclockwise, and scale fill rotate 90 degrees counterclockwise option to the original input image.](https://developer.apple.com/tutorials/images/Vision/scale-crop-options@2x.png)

## Topics

### Crop and Scale Options
- [VNImageCropAndScaleOption.centerCrop](./vnimagecropandscaleoption/centercrop.md)
  An option that scales the image to fit its shorter side within the input dimensions, while preserving its aspect ratio, and center-crops the image.
- [VNImageCropAndScaleOption.scaleFit](./vnimagecropandscaleoption/scalefit.md)
  An option that scales the image to fit its longer side within the input dimensions, while preserving its aspect ratio, and center-crops the image.
- [VNImageCropAndScaleOption.scaleFill](./vnimagecropandscaleoption/scalefill.md)
  An option that scales the image to fill the input dimensions, resizing it if necessary.
- [VNImageCropAndScaleOption.scaleFitRotate90CCW](./vnimagecropandscaleoption/scalefitrotate90ccw.md)
  An option that rotates the image 90 degrees counterclockwise and then scales it, while preserving its aspect ratio, to fit on the long side.
- [VNImageCropAndScaleOption.scaleFillRotate90CCW](./vnimagecropandscaleoption/scalefillrotate90ccw.md)
  An option that rotates the image 90 degrees counterclockwise and then scales it to fill the input dimensions.
### Creating a Scale Option
- [init?(rawValue: UInt)](./vnimagecropandscaleoption/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring Image Options
- [var imageCropAndScaleOption: VNImageCropAndScaleOption](./vncoremlrequest/imagecropandscaleoption.md)
  An optional setting that tells the Vision algorithm how to scale an input image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnimagecropandscaleoption)*