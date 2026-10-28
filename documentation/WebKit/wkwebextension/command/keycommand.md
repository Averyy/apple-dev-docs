# keyCommand

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A key command representation of the web extension command for use in the responder chain.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- visionOS 2.4+

## Declaration

```swift
@NSCopying
var keyCommand: UIKeyCommand? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) UIKeyCommand * keyCommand;
```

## Discussion

Provides a [`UIKeyCommand`](../../../UIKit/uikeycommand.md) instance representing the web extension command, ready for integration in the app.

The property is `nil` if no shortcut is defined. Otherwise, the key command is fully configured with the necessary input key and modifier flags to perform the associated command upon activation. It can be included in a view controller or other responder’s [`keyCommands`](../../../UIKit/uiresponder/keycommands.md) property, enabling keyboard activation and discoverability of the web extension command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/command/keycommand)*