# XCUIVoiceOverService

**Framework**: XCUIAutomation  
**Kind**: class

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)
- Xcode 16.3+

## Declaration

```swift
@MainActor
class XCUIVoiceOverService
```

#### Overview

Provides programmatic control of VoiceOver for UI testing.

Access this service through the @c voiceOverService property on @c XCUIDevice.

## Topics

### Classes
- [XCUIVoiceOverService.Output](xcuivoiceoverservice/output.md)
### Structures
- [XCUIVoiceOverService.Error](xcuivoiceoverservice/error.md)
### Instance Properties
- [var debugDescription: String](xcuivoiceoverservice/debugdescription.md)
  Provides debugging information about the service.
- [var isEnabled: Bool](xcuivoiceoverservice/isenabled.md)
  Whether VoiceOver is currently enabled.
### Instance Methods
- [func currentSpeech() throws -> XCUIVoiceOverService.Output](xcuivoiceoverservice/currentspeech.md)
  Return the speech for the currently focused element.
- [func disable() throws](xcuivoiceoverservice/disable.md)
  Disable VoiceOver.
- [func enable() throws](xcuivoiceoverservice/enable.md)
  Enable VoiceOver.
- [func moveBackward() throws -> XCUIVoiceOverService.Output](xcuivoiceoverservice/movebackward.md)
  Move VoiceOver to the previous element and return its speech.
- [func moveForward() throws -> XCUIVoiceOverService.Output](xcuivoiceoverservice/moveforward.md)
  Move VoiceOver to the next element and return its speech.
- [func moveIn() throws -> XCUIVoiceOverService.Output](xcuivoiceoverservice/movein.md)
  Move VoiceOver into the current container and return its speech.
- [func moveOut() throws -> XCUIVoiceOverService.Output](xcuivoiceoverservice/moveout.md)
  Move VoiceOver out of the current container and return its speech.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuivoiceoverservice)*