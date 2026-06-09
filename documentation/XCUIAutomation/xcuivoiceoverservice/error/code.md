# XCUIVoiceOverService.Error.Code

**Framework**: XCUIAutomation  
**Kind**: enum

Error codes for XCUIVoiceOverService operations.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Xcode 16.3+

## Declaration

```swift
enum Code
```

## Topics

### Enumeration Cases
- [XCUIVoiceOverService.Error.Code.failedToStart](xcuivoiceoverservice/error/code/failedtostart.md)
  VoiceOver daemon did not start within the timeout.
- [XCUIVoiceOverService.Error.Code.failedToStop](xcuivoiceoverservice/error/code/failedtostop.md)
  VoiceOver daemon did not stop within the timeout after @c disable().
- [XCUIVoiceOverService.Error.Code.noSpeech](xcuivoiceoverservice/error/code/nospeech.md)
  VoiceOver did not produce any speech within the timeout.
- [XCUIVoiceOverService.Error.Code.notRunning](xcuivoiceoverservice/error/code/notrunning.md)
  A navigation or speech method was called without first calling @c enable().
### Initializers
- [init?(rawValue: Int)](xcuivoiceoverservice/error/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuivoiceoverservice/error/code)*