# boundingBox

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The bounding box of the object.

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
var boundingBox: NormalizedRect { get }
```

#### Discussion

The coordinate system is normalized to the dimensions of the processed image, with the origin at the lower-left corner of the image.

## Default Implementations

### BoundingBoxProviding Implementations
- [var boundingBox: NormalizedRect](./boundingbox-73688.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/boundingboxproviding/boundingbox)*