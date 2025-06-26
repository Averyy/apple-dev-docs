# cvMetalTextureCache

**Framework**: Core Image  
**Kind**: property

A Core Video Metal texture cache object to improve the performance of Core Image context renders that use Core Video pixel buffers.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
static let cvMetalTextureCache: CIContextOption
```

#### Discussion

Creating a Core Image context with this optional `CVMetalTextureCache` can improve the performance of creating a Metal texture from a `CVPixelBuffer`. It is recommended to specify this option if the context renders to or from pixel buffers that come from a `CVPixelBufferPool`.

It is the client’s responsibility to flush the cache when appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontextoption/cvmetaltexturecache)*