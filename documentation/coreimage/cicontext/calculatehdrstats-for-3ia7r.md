# calculateHDRStats(for:)

**Framework**: Core Image  
**Kind**: method

Given a Core Graphics image, use the receiving Core Image context to calculate its HDR statistics (content headroom and content average light level) and then return a new Core Graphics image that has the calculated values.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

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