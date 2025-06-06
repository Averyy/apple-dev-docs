# exportData(with:to:destinationDataType:offset:rowStrides:)

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
func exportData(with cmdBuf: any MTLCommandBuffer, to buffer: any MTLBuffer, destinationDataType: MPSDataType, offset: Int, rowStrides: UnsafeMutablePointer<Int>?)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarray/3131729-exportdata)*