# Loads.Enforcement

**Framework**: Siri Evaluations  
**Kind**: enum  
**Role**: Enumeration

Whether a missed skill fails the expectation or only shows in the report.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
enum Enforcement
```

## Topics

### Specifying enforcement
- [Loads.Enforcement.required](./enforcement-swift.enum/required.md)
  A miss fails the skills-loaded metric.
- [Loads.Enforcement.preferred](./enforcement-swift.enum/preferred.md)
  Shown in the report, not graded.

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

### Configuring enforcement
- [let enforcement: Loads.Enforcement](./enforcement-swift.property.md)
  Whether a missed skill fails the expectation or only shows in the report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/loads/enforcement-swift.enum)*