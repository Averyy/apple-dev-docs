# insertingTiledIntermediate()

**Framework**: Core Image  
**Kind**: method

Create an image that inserts a intermediate that is cached in tiles

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func insertingTiledIntermediate() -> CIImage
```

#### Return Value

 An autoreleased [`CIImage`](ciimage.md).

#### Discussion

This intermediate will be cacheable even if [`cacheIntermediates`](cicontextoption/cacheintermediates.md) is false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/insertingtiledintermediate())*