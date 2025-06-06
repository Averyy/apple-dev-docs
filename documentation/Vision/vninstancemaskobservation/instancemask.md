# instanceMask

**Framework**: Vision  
**Kind**: property

The resulting mask that represents all instances.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var instanceMask: CVPixelBuffer { get }
```

#### Discussion

A pixel can only correspond to one instance. A `0` represents the background, and all other values represent the indices of the instances.

## See Also

- [var allInstances: IndexSet](vninstancemaskobservation/allinstances.md)
  The collection that contains all instances, excluding the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vninstancemaskobservation/instancemask)*