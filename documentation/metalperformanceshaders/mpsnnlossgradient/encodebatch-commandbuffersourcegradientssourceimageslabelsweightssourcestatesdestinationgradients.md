# encodeBatch(commandBuffer:sourceGradients:sourceImages:labels:weights:sourceStates:destinationGradients:)

**Framework**: Metal Performance Shaders  
**Kind**: method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceGradients: [MPSImage], sourceImages: [MPSImage], labels: [MPSImage], weights: [MPSImage]?, sourceStates: [MPSState]?, destinationGradients: [MPSImage])
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnlossgradient/encodebatch(commandbuffer:sourcegradients:sourceimages:labels:weights:sourcestates:destinationgradients:))*