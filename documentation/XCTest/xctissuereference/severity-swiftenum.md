# XCTIssueReference.Severity

**Framework**: XCTest  
**Kind**: enum

An enum representing the severity of a test issue.

## Declaration

```swift
enum Severity
```

#### Overview

The numeric values of this enum’s cases are comparable. A case which represents higher severity has a larger numeric value than one which represents lower severity. Specifying a numeric severity value other than one corresponding to a case defined below when initializing an `XCTIssue` is unsupported.

## Topics

### Enumeration Cases
- [XCTIssueReference.Severity.error](xctissuereference/severity-swift.enum/error.md)
  The severity level for an issue which represents an error in a test.
- [XCTIssueReference.Severity.warning](xctissuereference/severity-swift.enum/warning.md)
  The severity level for an issue which should be noted but is not necessarily an error.
### Initializers
- [init?(rawValue: Int)](xctissuereference/severity-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctissuereference/severity-swift.enum)*