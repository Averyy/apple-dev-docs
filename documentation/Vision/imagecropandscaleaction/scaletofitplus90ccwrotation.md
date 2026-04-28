# ImageCropAndScaleAction.scaleToFitPlus90CCWRotation

**Framework**: Vision  
**Kind**: case

An action that scales the image and maintains the aspect ratio to fit on the long side, and rotates the image by 90 degrees counter clockwise.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
case scaleToFitPlus90CCWRotation
```

#### Discussion

Rotation helps to optimize portrait images fit into landscape buffers for algorithms that are rotation agnostic.

## See Also

- [ImageCropAndScaleAction.centerCrop](imagecropandscaleaction/centercrop.md)
  An action that scales the image and maintains the aspect ratio to fit on the short side and crop centered on the long side.
- [ImageCropAndScaleAction.scaleToFit](imagecropandscaleaction/scaletofit.md)
  An action that scales to the size the algorithm requires while maintaining the original aspect ratio.
- [ImageCropAndScaleAction.scaleToFill](imagecropandscaleaction/scaletofill.md)
  An action that scales the image to fill the input dimensions and resizing it, if necessary.
- [ImageCropAndScaleAction.scaleToFillPlus90CCWRotation](imagecropandscaleaction/scaletofillplus90ccwrotation.md)
  An action that scales the image and rotates it by 90 degrees counter clockwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/imagecropandscaleaction/scaletofitplus90ccwrotation)*