# ImageCropAndScaleAction

**Framework**: Vision  
**Kind**: enum

A scale to apply to an input image before performing a request.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
enum ImageCropAndScaleAction
```

## Topics

### Getting the actions
- [ImageCropAndScaleAction.centerCrop](imagecropandscaleaction/centercrop.md)
  An action that scales the image and maintains the aspect ratio to fit on the short side and crop centered on the long side.
- [ImageCropAndScaleAction.scaleToFit](imagecropandscaleaction/scaletofit.md)
  An action that scales to the size the algorithm requires while maintaining the original aspect ratio.
- [ImageCropAndScaleAction.scaleToFill](imagecropandscaleaction/scaletofill.md)
  An action that scales the image to fill the input dimensions and resizing it, if necessary.
- [ImageCropAndScaleAction.scaleToFitPlus90CCWRotation](imagecropandscaleaction/scaletofitplus90ccwrotation.md)
  An action that scales the image and maintains the aspect ratio to fit on the long side, and rotates the image by 90 degrees counter clockwise.
- [ImageCropAndScaleAction.scaleToFillPlus90CCWRotation](imagecropandscaleaction/scaletofillplus90ccwrotation.md)
  An action that scales the image and rotates it by 90 degrees counter clockwise.

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var cropAndScaleAction: ImageCropAndScaleAction](calculateimageaestheticsscoresrequest/cropandscaleaction.md)
  An optional setting that tells the algorithm how to scale an input image before generating the result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/imagecropandscaleaction)*