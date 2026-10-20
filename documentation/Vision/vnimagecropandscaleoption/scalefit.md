# VNImageCropAndScaleOption.scaleFit

**Framework**: Vision  
**Kind**: case  
**Role**: Case

An option that scales the image to fit its longer side within the input dimensions, while preserving its aspect ratio, and center-crops the image.

## Declaration

```swift
case scaleFit
```

```c
VNImageCropAndScaleOptionScaleFit
```

#### Discussion

This option fills the remaining space with transparent pixels to maintain aspect ratio.

## See Also

### Crop and Scale Options
- [VNImageCropAndScaleOption.centerCrop](./centercrop.md)
  An option that scales the image to fit its shorter side within the input dimensions, while preserving its aspect ratio, and center-crops the image.
- [VNImageCropAndScaleOption.scaleFill](./scalefill.md)
  An option that scales the image to fill the input dimensions, resizing it if necessary.
- [VNImageCropAndScaleOption.scaleFitRotate90CCW](./scalefitrotate90ccw.md)
  An option that rotates the image 90 degrees counterclockwise and then scales it, while preserving its aspect ratio, to fit on the long side.
- [VNImageCropAndScaleOption.scaleFillRotate90CCW](./scalefillrotate90ccw.md)
  An option that rotates the image 90 degrees counterclockwise and then scales it to fill the input dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnimagecropandscaleoption/scalefit)*