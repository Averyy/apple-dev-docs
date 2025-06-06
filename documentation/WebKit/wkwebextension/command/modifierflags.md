# modifierFlags

**Framework**: Webkit  
**Kind**: property

The modifier flags used with the activation key to trigger the command.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var modifierFlags: UIKeyModifierFlags { get set }
```

#### Discussion

This property can be customized within the app to avoid conflicts with existing shortcuts or to enable user personalization. It should accurately represent the modifier keys as used by the app, which the extension can use to display the complete shortcut in its interface.

If no modifiers are desired for the command, the property should be set to `0`. This value should be saved and restored as needed by the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/command/modifierflags)*