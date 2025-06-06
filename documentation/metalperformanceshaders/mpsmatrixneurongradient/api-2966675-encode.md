# encode(to:gradientMatrix:inputMatrix:biasVector:resultGradientForDataMatrix:resultGradientForBiasVector:)

**Framework**: Metal Performance Shaders  
**Kind**: instm

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func encode(to commandBuffer: any MTLCommandBuffer, gradientMatrix: MPSMatrix, inputMatrix: MPSMatrix, biasVector: MPSVector?, resultGradientForDataMatrix: MPSMatrix, resultGradientForBiasVector: MPSVector?)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixneurongradient/2966675-encode)*