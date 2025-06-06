# prefetchStorage(with:imageDescriptorList:)

**Framework**: Metalperformanceshaders  
**Kind**: clm

A method that helps the framework decide which allocations to make ahead of time.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func prefetchStorage(with commandBuffer: any MTLCommandBuffer, imageDescriptorList descriptorList: [MPSImageDescriptor])
```

#### Discussion

The texture cache that underlies the temporary images can automatically allocate new storage as needed, whenever you create new temporary images. However, sometimes a more global view of what you plan to make is useful for maximizing memory reuse to get the most efficient operation. Calling this class method provides a hint to the texture cache about what the list of temporary images will be.

> **Note**: Calling this method is purely a performance and memory optimization; it is never  to call this method.

## Parameters

- `commandBuffer`: The command buffer on which the temporary images will be exclusively used.
- `descriptorList`: An array of image descriptors that describe the temporary images that will be created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpstemporaryimage/2097544-prefetchstorage)*