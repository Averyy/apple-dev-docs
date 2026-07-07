# timeSamples(in:)

**Framework**: USDKit  
**Kind**: method

Returns time samples authored within the specified interval.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func timeSamples(in interval: ClosedRange<USDStage.TimeCode>) -> [USDStage.TimeCode]
```

#### Return Value

Time samples within the interval, or an empty array if none exist.

## Parameters

- `interval`: The time interval to query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdtransformoperation/timesamples(in:))*