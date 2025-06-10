# keyCommand

**Framework**: WebKit  
**Kind**: property

A key command representation of the web extension command for use in the responder chain.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- visionOS 2.4+

## Declaration

```swift
@NSCopying
@MainActor var keyCommand: UIKeyCommand? { get }
```

#### Discussion

Provides a [`UIKeyCommand`](https://developer.apple.com/documentation/UIKit/UIKeyCommand) instance representing the web extension command, ready for integration in the app.

The property is `nil` if no shortcut is defined. Otherwise, the key command is fully configured with the necessary input key and modifier flags to perform the associated command upon activation. It can be included in a view controller or other responder’s [`keyCommands`](https://developer.apple.com/documentation/UIKit/UIResponder/keyCommands) property, enabling keyboard activation and discoverability of the web extension command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/command/keycommand)*