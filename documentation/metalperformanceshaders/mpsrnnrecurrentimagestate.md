# MPSRNNRecurrentImageState

**Framework**: Metal Performance Shaders  
**Kind**: cl

A class that holds all the data that's passed from one sequence iteration of the image-based recurrent neural network layer (stack) to the next.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSRNNRecurrentImageState : MPSState
```

## Topics

### Instance Methods
- [func getMemoryCellImage(forLayerIndex: Int) -> MPSImage?](mpsrnnrecurrentimagestate/2865740-getmemorycellimage.md)
- [func getRecurrentOutputImage(forLayerIndex: Int) -> MPSImage?](mpsrnnrecurrentimagestate/2865742-getrecurrentoutputimage.md)

## Relationships

### Inherits From
- [MPSState](mpsstate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrnnrecurrentimagestate)*