# XCTIssueReference.Severity

**Framework**: XCTest  
**Kind**: enum  
**Role**: Enumeration

An enum representing the severity of a test issue.

## Declaration

```swift
enum Severity
```

```c
enum XCTIssueSeverity : NSInteger;
```

## Overview

The numeric values of this enum’s cases are comparable. A case which represents higher severity has a larger numeric value than one which represents lower severity. Specifying a numeric severity value other than one corresponding to a case defined below when initializing an `XCTIssue` is unsupported.

## Topics

### Enumeration Cases
- [XCTIssueReference.Severity.error](./severity-swift.enum/error.md)
  The severity level for an issue which represents an error in a test.
- [XCTIssueReference.Severity.warning](./severity-swift.enum/warning.md)
  The severity level for an issue which should be noted but is not necessarily an error.
### Initializers
- [init?(rawValue: Int)](./severity-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Comparable](../../Swift/comparable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctissuereference/severity-swift.enum)*