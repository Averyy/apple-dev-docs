# safeStep(maxValue:maxCompression:)

**Framework**: USDKit  
**Kind**: method

Returns a time delta small enough to represent a jump discontinuity, but large enough to survive scaling and shifting without collapsing to zero.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func safeStep(maxValue: Double = 1e6, maxCompression: Double = 10.0) -> Double
```

#### Discussion

Use it to author paired samples at `t` and `t + SafeStep()` that stay distinct for any `t` in [-maxValue, maxValue] under compression up to `maxCompression`.

Equivalent to: `epsilon * maxValue * maxCompression * 2`..


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/timecode/safestep(maxvalue:maxcompression:))*