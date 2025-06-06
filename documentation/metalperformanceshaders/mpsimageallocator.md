# MPSImageAllocator

**Framework**: Metal Performance Shaders  
**Kind**: intf

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
protocol MPSImageAllocator
```

## Topics

### Instance Methods
- [func image(for: any MTLCommandBuffer, imageDescriptor: MPSImageDescriptor, kernel: MPSKernel) -> MPSImage](mpsimageallocator/2866966-image.md)
- [func imageBatch(for: any MTLCommandBuffer, imageDescriptor: MPSImageDescriptor, kernel: MPSKernel, count: Int) -> [MPSImage]](mpsimageallocator/3020685-imagebatch.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class func defaultAllocator() -> any MPSImageAllocator](mpstemporaryimage/2867130-defaultallocator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageallocator)*