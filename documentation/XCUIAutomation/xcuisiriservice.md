# XCUISiriService

**Framework**: XCUIAutomation  
**Kind**: class  
**Role**: Class

A proxy that simulates a device’s Siri interface.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 10.3+
- Xcode 16.3+

## Declaration

```swift
@MainActor
class XCUISiriService
```

```objc
@interface XCUISiriService : NSObject
```

## Overview

This class allows issuing textual queries and producing element queries for UI shown by Siri.

## Topics

### Siri activation
- [func activate(voiceRecognitionText: String)](./xcuisiriservice/activate%28voicerecognitiontext%29.md)
  Presents the Siri UI, if it’s not currently active, and accepts a string that is then processed as if it’s recognized speech.
### Siri proxy state
- [var debugDescription: String](./xcuisiriservice/debugdescription.md)
  Provides debugging information about the element representing the root of the Siri UI.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [XCUIElementTypeQueryProvider](./xcuielementtypequeryprovider.md)

## See Also

### Related Documentation
- [var siriService: XCUISiriService](./xcuidevice/siriservice.md)
  An object that represents the Siri interface on the device.
### Device simulation
- [class XCUIDevice](./xcuidevice.md)
  A proxy that can simulate physical buttons, device orientation, and Siri interaction for an iOS, watchOS, or tvOS device.
- [class XCUISystem](./xcuisystem.md)
  A proxy that provides an interface to OS-specific properties and actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuisiriservice)*