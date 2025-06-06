# precipitationAmount

**Framework**: Weatherkit  
**Kind**: property

The amount of precipitation for the hour.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var precipitationAmount: Measurement<UnitLength>
```

#### Discussion

This value refers to the liquid equivalent of all precipitation amounts. Note that since this is the amount over the hour and the precipitation intensity is also amount over the hour, this property also means precipitationIntensity


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/hourweather/precipitationamount)*