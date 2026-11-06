# Calls.Ordering

**Framework**: Siri Evaluations  
**Kind**: enum  
**Role**: Enumeration

A requirement for how Siri must call the intents in an expectation, or that it doesn’t call them.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
enum Ordering
```

## Topics

### Specifying ordering
- [Calls.Ordering.ordered](./ordering-swift.enum/ordered.md)
  A requirement that Siri calls the intents in the order written.
- [Calls.Ordering.unordered](./ordering-swift.enum/unordered.md)
  A requirement that Siri calls every intent, in any order.
- [Calls.Ordering.disallowed](./ordering-swift.enum/disallowed.md)
  A requirement that Siri doesn’t call any of the intents.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring call order
- [let ordering: Calls.Ordering](./ordering-swift.property.md)
  How Siri must call the intents, or that it must not call them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/calls/ordering-swift.enum)*