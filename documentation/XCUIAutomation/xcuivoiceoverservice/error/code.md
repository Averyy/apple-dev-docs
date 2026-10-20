# XCUIVoiceOverService.Error.Code

**Framework**: XCUIAutomation  
**Kind**: enum  
**Role**: Enumeration

Error codes for XCUIVoiceOverService operations.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS
- Xcode 16.3+

## Declaration

```swift
enum Code
```

```c
enum XCUIVoiceOverServiceError : NSInteger;
```

## Topics

### Enumeration Cases
- [XCUIVoiceOverService.Error.Code.failedToStart](./code/failedtostart.md)
  VoiceOver daemon did not start within the timeout.
- [XCUIVoiceOverService.Error.Code.failedToStop](./code/failedtostop.md)
  VoiceOver daemon did not stop within the timeout after @c disable().
- [XCUIVoiceOverService.Error.Code.noSpeech](./code/nospeech.md)
  VoiceOver did not produce any speech within the timeout.
- [XCUIVoiceOverService.Error.Code.notRunning](./code/notrunning.md)
  A navigation or speech method was called without first calling @c enable().
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../../Swift/bitwisecopyable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuivoiceoverservice/error/code)*