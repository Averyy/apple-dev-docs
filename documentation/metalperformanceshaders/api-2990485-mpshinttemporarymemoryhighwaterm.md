# MPSHintTemporaryMemoryHighWaterMark(_:_:)

**Framework**: Metal Performance Shaders  
**Kind**: func

Triggers Metal Performance Shaders to prefetch a Metal heap of the indicated size into its internal cache.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func MPSHintTemporaryMemoryHighWaterMark(_ cmdBuf: any MTLCommandBuffer, _ bytes: Int)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/2990485-mpshinttemporarymemoryhighwaterm)*