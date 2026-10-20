# VNImageCropAndScaleOption.scaleFillRotate90CCW

**Framework**: Vision  
**Kind**: case  
**Role**: Case

An option that rotates the image 90 degrees counterclockwise and then scales it to fill the input dimensions.

## Declaration

```swift
case scaleFillRotate90CCW
```

```c
VNImageCropAndScaleOptionScaleFillRotate90CCW
```

#### Discussion

This option optimizes portrait images to fill into landscape buffers for algorithms that are rotation agnostic.

## See Also

### Crop and Scale Options
- [VNImageCropAndScaleOption.centerCrop](./centercrop.md)
  An option that scales the image to fit its shorter side within the input dimensions, while preserving its aspect ratio, and center-crops the image.
- [VNImageCropAndScaleOption.scaleFit](./scalefit.md)
  An option that scales the image to fit its longer side within the input dimensions, while preserving its aspect ratio, and center-crops the image.
- [VNImageCropAndScaleOption.scaleFill](./scalefill.md)
  An option that scales the image to fill the input dimensions, resizing it if necessary.
- [VNImageCropAndScaleOption.scaleFitRotate90CCW](./scalefitrotate90ccw.md)
  An option that rotates the image 90 degrees counterclockwise and then scales it, while preserving its aspect ratio, to fit on the long side.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnimagecropandscaleoption/scalefillrotate90ccw)*