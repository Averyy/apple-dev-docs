# DetectedDocumentObservation

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

The heat map that’s a pixel buffer in a one-component floating-point pixel format.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+

## Declaration

```swift
struct DetectedDocumentObservation
```

## Overview

The observation includes the four corner points of a document’s quadrilateral and saliency masks.

## Topics

### Creating an observation
- [init?(VNRectangleObservation)](./detecteddocumentobservation/init%28_%29.md)
  Creates a detected document observation.
### Inspecting an observation
- [enum RequestDescriptor](./requestdescriptor.md)
  A type that describes the request and revision combination.
- [var globalSegmentationMask: PixelBufferObservation](./detecteddocumentobservation/globalsegmentationmask.md)
  A pixel buffer representing a segmentation mask for the detected document.
- [struct PixelBufferObservation](./pixelbufferobservation.md)
  An object that represents an image that an image-analysis request produces.

## Relationships

### Conforms To
- [BoundingBoxProviding](./boundingboxproviding.md)
- [Copyable](../Swift/copyable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [QuadrilateralProviding](./quadrilateralproviding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [VisionObservation](./visionobservation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detecteddocumentobservation)*