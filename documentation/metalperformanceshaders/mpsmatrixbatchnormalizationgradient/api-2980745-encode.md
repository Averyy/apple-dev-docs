# encode(to:gradientMatrix:inputMatrix:mean:varianceVector:gammaVector:betaVector:resultGradientForDataMatrix:resultGradientForGammaVector:resultGradientForBetaVector:)

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
func encode(to commandBuffer: any MTLCommandBuffer, gradientMatrix: MPSMatrix, inputMatrix: MPSMatrix, mean meanVector: MPSVector, varianceVector: MPSVector, gammaVector: MPSVector?, betaVector: MPSVector?, resultGradientForDataMatrix: MPSMatrix, resultGradientForGammaVector: MPSVector?, resultGradientForBetaVector: MPSVector?)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixbatchnormalizationgradient/2980745-encode)*