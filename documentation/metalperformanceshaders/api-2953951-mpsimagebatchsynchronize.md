# MPSImageBatchSynchronize(_:_:)

**Framework**: Metal Performance Shaders  
**Kind**: func

Removes any copy of the specified image batch from the device's caches, and, if needed, invalidates any CPU caches.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
func MPSImageBatchSynchronize(_ batch: [MPSImage], _ cmdBuf: any MTLCommandBuffer)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/2953951-mpsimagebatchsynchronize)*