# encodeBilateralFilter(to:stepDistance:sourceTexture:destinationTexture:sourceTexture2:destinationTexture2:depthNormalTexture:)

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
func encodeBilateralFilter(to commandBuffer: any MTLCommandBuffer, stepDistance: Int, sourceTexture: any MTLTexture, destinationTexture: any MTLTexture, sourceTexture2: (any MTLTexture)?, destinationTexture2: (any MTLTexture)?, depthNormalTexture: any MTLTexture)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpssvgf/3143561-encodebilateralfilter)*