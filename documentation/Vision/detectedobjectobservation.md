# DetectedObjectObservation

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

An observation that provides the position and extent of an image feature that an image-analysis request detects.

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
struct DetectedObjectObservation
```

## Overview

This class is the observation type that [`TrackObjectRequest`](./trackobjectrequest.md) generates. It represents an object that the Vision request detects and tracks.

## Topics

### Creating an observation
- [init(VNDetectedObjectObservation)](./detectedobjectobservation/init%28_%29.md)
  Creates a detected object observation.
- [init(boundingBox: NormalizedRect)](./detectedobjectobservation/init%28boundingbox%29.md)
  Creates a detected object observation with the bounding box you specify.
### Inspecting an observation
- [enum RequestDescriptor](./requestdescriptor.md)
  A type that describes the request and revision combination.

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
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [VisionObservation](./visionobservation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detectedobjectobservation)*