# CIImageAccumulator

**Framework**: Core Image  
**Kind**: cl

An object that manages feedback-based image processing for tasks such as painting or fluid simulation.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CIImageAccumulator : NSObject
```

#### Overview

The `CIImageAccumulator` class enables feedback-based image processing for such things as iterative painting operations or fluid dynamics simulations. You use `CIImageAccumulator` objects in conjunction with other Core Image classes, such as  [`CIFilter`](cifilter.md), [`CIImage`](ciimage.md), [`CIVector`](civector.md), and [`CIContext`](cicontext.md), to take advantage of the built-in Core Image filters when processing images.

## Topics

### Initializing an Image Accumulator
- [init?(extent: CGRect, format: CIFormat)](ciimageaccumulator/1427718-init.md)
  Initializes an image accumulator with the specified extent and pixel format.
- [init?(extent: CGRect, format: CIFormat, colorSpace: CGColorSpace)](ciimageaccumulator/1427710-init.md)
  Initializes an image accumulator with the specified extent, pixel format, and color space.
### Setting an Image
- [func setImage(CIImage)](ciimageaccumulator/1427702-setimage.md)
  Sets the contents of the image accumulator to the contents of the specified image object.
- [func setImage(CIImage, dirtyRect: CGRect)](ciimageaccumulator/1427706-setimage.md)
  Updates an image accumulator with a subregion of an image object.
### Obtaining Data From an Image Accumulator
- [var extent: CGRect](ciimageaccumulator/1427714-extent.md)
  The extent of the image associated with the image accumulator.
- [var format: CIFormat](ciimageaccumulator/1427716-format.md)
  The pixel format of the image accumulator.
- [func image() -> CIImage](ciimageaccumulator/1427704-image.md)
  Returns the current contents of the image accumulator. 
### Resetting an Accumulator
- [func clear()](ciimageaccumulator/1427720-clear.md)
  Resets the accumulator, discarding any pending updates and the current content.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageaccumulator)*