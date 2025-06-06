# encodeBatch(commandBuffer:sourceImages:labels:weights:outStates:isTemporary:)

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
func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], labels: [MPSImage], weights: [MPSImage]?, outStates: AutoreleasingUnsafeMutablePointer<NSArray?>?, isTemporary: Bool) -> [MPSImage]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnforwardloss/3131799-encodebatch)*