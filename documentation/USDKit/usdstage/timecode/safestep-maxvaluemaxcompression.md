# safeStep(maxValue:maxCompression:)

**Framework**: USDKit  
**Kind**: method

Returns a time delta small enough to represent a jump discontinuity, but large enough to survive scaling and shifting without collapsing to zero.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static func safeStep(maxValue: Double = 1e6, maxCompression: Double = 10.0) -> Double
```

#### Discussion

Use it to author paired samples at `t` and `t + SafeStep()` that stay distinct for any `t` in [-maxValue, maxValue] under compression up to `maxCompression`.

Equivalent to: `epsilon * maxValue * maxCompression * 2`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/timecode/safestep(maxvalue:maxcompression:))*