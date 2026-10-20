# setTimeSample(at:time:value:)

**Framework**: USDKit  
**Kind**: method  
**Role**: Instance Method

Sets the time-sampled value for the attribute at the given path at the specified time.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func setTimeSample(at path: USDLayer.Path, time: USDLayer.TimeCode, value: USDValue)
```

## Parameters

- `path`: The attribute path.
- `time`: The time at which to author.
- `value`: The new sample value.

## See Also

### Working with time samples
- [func timeSample(at: USDLayer.Path, time: USDLayer.TimeCode) -> USDValue?](./timesample%28at,time%29.md)
  Returns the time-sampled value for the attribute at the given path at the specified time, or `nil` if none is authored at that time.
- [func timeSamples(at: USDLayer.Path) -> Set<USDLayer.TimeCode>](./timesamples%28at%29.md)
  Returns the time codes for which the attribute at the given path has authored time samples.
- [var allTimeSamples: Set<USDLayer.TimeCode>](./alltimesamples.md)
  All time codes for which any attribute in the layer has an authored time sample.
- [func setTimeSample<T>(at: USDLayer.Path, time: USDLayer.TimeCode, value: T)](./settimesample%28at,time,value%29-3ot1j.md)
  Sets the time-sampled value for the attribute at the given path at the specified time, wrapping the typed value in a `USDValue`.
- [func eraseTimeSample(at: USDLayer.Path, time: USDLayer.TimeCode)](./erasetimesample%28at,time%29.md)
  Erases the authored time sample at the given path and time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/settimesample(at:time:value:)-6t3qd)*