# calculateHDRStats(for:)

**Framework**: Core Image  
**Kind**: method

Given a Core Image image, use the receiving Core Image context to calculate its HDR statistics (content headroom and content average light level) and then return a new Core Image image that has the calculated values.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func calculateHDRStats(for image: CIImage) -> CIImage?
```

#### Return Value

 Returns a new [`CIImage`](ciimage.md) instance that has the calculated statistics attached.

#### Discussion

If the image extent is not finite, then nil will be returned.

## Parameters

- `image`: An immutable   for which to calculate statistics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/calculatehdrstats(for:)-l1rj)*