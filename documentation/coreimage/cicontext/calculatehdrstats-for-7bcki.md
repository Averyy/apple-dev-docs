# calculateHDRStats(for:)

**Framework**: Core Image  
**Kind**: method

Given a CVPixelBuffer, use the receiving Core Image context to calculate its HDR statistics (content headroom and content average light level) and then update the buffers’s attachments to store the values.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func calculateHDRStats(for buffer: CVPixelBuffer)
```

#### Discussion

If the `CVPixelBuffer` has a Clean Aperture rectangle then only pixels within that rectangle are considered.

## Parameters

- `buffer`: A mutable   for which to calculate and attach statistics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/calculatehdrstats(for:)-7bcki)*