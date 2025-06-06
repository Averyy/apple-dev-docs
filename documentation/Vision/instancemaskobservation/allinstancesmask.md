# allInstancesMask

**Framework**: Vision  
**Kind**: property

The resulting mask that represents all instances.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
let allInstancesMask: PixelBufferObservation
```

#### Discussion

A pixel can only correspond to one instance. A `0` represents the background, and all other values represent the indices of the instances.

## See Also

- [func instanceAtPoint(NormalizedPoint) -> IndexSet](instancemaskobservation/instanceatpoint(_:).md)
  Returns an instance at the point you specify.
- [let allInstances: IndexSet](instancemaskobservation/allinstances.md)
  The collection that contains all instances, excluding the background.
- [struct PixelBufferObservation](pixelbufferobservation.md)
  An object that represents an image that an image-analysis request produces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/instancemaskobservation/allinstancesmask)*