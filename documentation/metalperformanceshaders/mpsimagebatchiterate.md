# MPSImageBatchIterate(_:_:)

**Framework**: Metal Performance Shaders  
**Kind**: func

Executes a callback block once for each unique image in a batch.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func MPSImageBatchIterate(_ batch: [MPSImage], _ iteratorBlock: @escaping (MPSImage, Int) -> Int) -> Int
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagebatchiterate(_:_:))*