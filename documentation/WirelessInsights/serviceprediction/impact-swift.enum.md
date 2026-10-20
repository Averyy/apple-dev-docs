# ServicePrediction.Impact

**Framework**: WirelessInsights  
**Kind**: enum  
**Role**: Enumeration

An enumeration of levels of impact for a predicted event.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
enum Impact
```

## Topics

### Working with impact values
- [ServicePrediction.Impact.high](./impact-swift.enum/high.md)
  An impact level for severe interruption, including substantially lowered throughput and the potential to lose data capability.
- [ServicePrediction.Impact.medium](./impact-swift.enum/medium.md)
  An impact level for moderately lower throughput and service interruption.
- [ServicePrediction.Impact.low](./impact-swift.enum/low.md)
  An impact level for slightly lower throughput and possibly some service interruption.

## Relationships

### Conforms To
- [Comparable](../../Swift/comparable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing prediction impact
- [let impact: ServicePrediction.Impact](./impact-swift.property.md)
  The expected impact of the predicted event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wirelessinsights/serviceprediction/impact-swift.enum)*