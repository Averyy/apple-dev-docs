# insertingTiledIntermediate()

**Framework**: Core Image  
**Kind**: method

Create an image that inserts a intermediate that is cached in tiles

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

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