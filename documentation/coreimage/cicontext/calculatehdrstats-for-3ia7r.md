# calculateHDRStats(for:)

**Framework**: Core Image  
**Kind**: method

Given a Core Graphics image, use the receiving Core Image context to calculate its HDR statistics (content headroom and content average light level) and then return a new Core Graphics image that has the calculated values.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func calculateHDRStats(for cgimage: CGImage) -> CGImage
```

#### Return Value

 Returns a new `CGImage` instance that has the calculated statistics attached.

## Parameters

- `cgimage`: An immutable   for which to calculate statistics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/calculatehdrstats(for:)-3ia7r)*