# instanceAtPoint(_:)

**Framework**: Vision  
**Kind**: method

Returns an instance at the point you specify.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func instanceAtPoint(_ point: NormalizedPoint) -> IndexSet
```

## See Also

- [let allInstances: IndexSet](instancemaskobservation/allinstances.md)
  The collection that contains all instances, excluding the background.
- [let allInstancesMask: PixelBufferObservation](instancemaskobservation/allinstancesmask.md)
  The resulting mask that represents all instances.
- [struct PixelBufferObservation](pixelbufferobservation.md)
  An object that represents an image that an image-analysis request produces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/instancemaskobservation/instanceatpoint(_:))*