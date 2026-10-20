# XCUIVoiceOverService

**Framework**: XCUIAutomation  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Xcode 16.3+

## Declaration

```swift
@MainActor
class XCUIVoiceOverService
```

```objc
@interface XCUIVoiceOverService : NSObject
```

#### Overview

Provides programmatic control of VoiceOver for UI testing.

Access this service through the @c voiceOverService property on @c XCUIDevice.

## Topics

### Classes
- [XCUIVoiceOverService.Output](./xcuivoiceoverservice/output.md)
### Structures
- [XCUIVoiceOverService.Error](./xcuivoiceoverservice/error.md)
### Instance Properties
- [var debugDescription: String](./xcuivoiceoverservice/debugdescription.md)
  Provides debugging information about the service.
- [var isEnabled: Bool](./xcuivoiceoverservice/isenabled.md)
  Whether VoiceOver is currently enabled.
### Instance Methods
- [func currentSpeech() throws -> XCUIVoiceOverService.Output](./xcuivoiceoverservice/currentspeech%28%29.md)
  Return the speech for the currently focused element.
- [func disable() throws](./xcuivoiceoverservice/disable%28%29.md)
  Disable VoiceOver.
- [func enable() throws](./xcuivoiceoverservice/enable%28%29.md)
  Enable VoiceOver.
- [func moveBackward() throws -> XCUIVoiceOverService.Output](./xcuivoiceoverservice/movebackward%28%29.md)
  Move VoiceOver to the previous element and return its speech.
- [func moveForward() throws -> XCUIVoiceOverService.Output](./xcuivoiceoverservice/moveforward%28%29.md)
  Move VoiceOver to the next element and return its speech.
- [func moveIn() throws -> XCUIVoiceOverService.Output](./xcuivoiceoverservice/movein%28%29.md)
  Move VoiceOver into the current container and return its speech.
- [func moveOut() throws -> XCUIVoiceOverService.Output](./xcuivoiceoverservice/moveout%28%29.md)
  Move VoiceOver out of the current container and return its speech.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuivoiceoverservice)*