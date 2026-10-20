# typeKey(_:modifierFlags:)

**Framework**: XCUIAutomation  
**Kind**: method  
**Role**: Instance Method

Types a single key from the XCUIKeyboardKey enumeration with the specified modifier flags.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- Swift 4.0+
- Xcode 16.3+

## Declaration

```swift
@MainActor
@nonobjc @preconcurrency func typeKey(_ key: XCUIKeyboardKey, modifierFlags: XCUIElement.KeyModifierFlags)
```

## See Also

### Combining keystrokes
- [func typeKey(String, modifierFlags: XCUIElement.KeyModifierFlags)](./typekey%28_,modifierflags%29-9ubn.md)
  Types a single key that a string represents with the flags you specify.
- [struct XCUIKeyboardKey](../xcuikeyboardkey.md)
  Constants to represent keys that have no typewritten equivalent.
- [class func perform(withKeyModifiers: XCUIElement.KeyModifierFlags, block: () -> Void)](./perform%28withkeymodifiers,block%29.md)
  Executes a block of code while holding a combination keystroke.
- [XCUIElement.KeyModifierFlags](./keymodifierflags.md)
  Flags for simulating combination keystrokes with keys, such as Control, Option, Shift, and Command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/typekey(_:modifierflags:)-6gaoi)*