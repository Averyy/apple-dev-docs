# timeSamples(at:)

**Framework**: USDKit  
**Kind**: method

Returns the time codes for which the attribute at the given path has authored time samples.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func timeSamples(at path: USDLayer.Path) -> Set<USDLayer.TimeCode>
```

#### Return Value

The set of authored time codes.

## Parameters

- `path`: The attribute path.

## See Also

- [func timeSample(at: USDLayer.Path, time: USDLayer.TimeCode) -> USDValue?](usdlayer/timesample(at:time:).md)
  Returns the time-sampled value for the attribute at the given path at the specified time, or `nil` if none is authored at that time.
- [var allTimeSamples: Set<USDLayer.TimeCode>](usdlayer/alltimesamples.md)
  All time codes for which any attribute in the layer has an authored time sample.
- [func setTimeSample(at: USDLayer.Path, time: USDLayer.TimeCode, value: USDValue)](usdlayer/settimesample(at:time:value:)-6t3qd.md)
  Sets the time-sampled value for the attribute at the given path at the specified time.
- [func setTimeSample<T>(at: USDLayer.Path, time: USDLayer.TimeCode, value: T)](usdlayer/settimesample(at:time:value:)-3ot1j.md)
  Sets the time-sampled value for the attribute at the given path at the specified time, wrapping the typed value in a `USDValue`.
- [func eraseTimeSample(at: USDLayer.Path, time: USDLayer.TimeCode)](usdlayer/erasetimesample(at:time:).md)
  Erases the authored time sample at the given path and time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/timesamples(at:))*