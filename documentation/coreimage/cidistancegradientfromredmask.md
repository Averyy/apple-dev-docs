# CIDistanceGradientFromRedMask

**Framework**: Core Image  
**Kind**: protocol

The protocol for the Distance Gradient From Red Mask filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIDistanceGradientFromRedMask : CIFilterProtocol
```

#### Overview

Produces an infinite image where the red channel contains the distance in pixels from each pixel to the mask.

## Topics

### Instance Properties
- [var inputImage: CIImage?](cidistancegradientfromredmask/inputimage.md)
  The input image whose red channel defines a mask. If the red channel pixel value is greater than 0.5 then the point is considered in the mask and output pixel will be zero. Otherwise the output pixel will be a value between zero and one.
- [var maximumDistance: Float](cidistancegradientfromredmask/maximumdistance.md)
  Determines the maximum distance to the mask that can be measured. Distances between zero and the maximum will be normalized to zero and one.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidistancegradientfromredmask)*