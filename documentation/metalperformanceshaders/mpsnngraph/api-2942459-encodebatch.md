# encodeBatch(to:sourceImages:sourceStates:intermediateImages:destinationStates:)

**Framework**: Metal Performance Shaders  
**Kind**: instm

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
func encodeBatch(to commandBuffer: any MTLCommandBuffer, sourceImages: [[MPSImage]], sourceStates: [[MPSState]]?, intermediateImages: NSMutableArray?, destinationStates: NSMutableArray?) -> [MPSImage]?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnngraph/2942459-encodebatch)*