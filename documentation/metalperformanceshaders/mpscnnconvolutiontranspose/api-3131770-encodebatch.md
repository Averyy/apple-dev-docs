# encodeBatch(commandBuffer:sourceImages:convolutionGradientStates:destinationStates:destinationStateIsTemporary:)

**Framework**: Metal Performance Shaders  
**Kind**: instm

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], convolutionGradientStates: [MPSCNNConvolutionGradientState]?, destinationStates outStates: AutoreleasingUnsafeMutablePointer<NSArray?>, destinationStateIsTemporary isTemporary: Bool) -> [MPSImage]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiontranspose/3131770-encodebatch)*