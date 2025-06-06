# perform(withKeyModifiers:block:)

**Framework**: Xcuiautomation  
**Kind**: method

Executes a block of code while holding a combination keystroke.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS ?+
- Xcode 16.3+

## Declaration

```swift
@MainActor
class func perform(withKeyModifiers flags: XCUIElement.KeyModifierFlags, block: () -> Void)
```

#### Discussion

This method sets and holds the keyboard modifiers you provide while you call methods to click on, drag from, or type into elements in the block.

## Parameters

- `flags`: A set of modifier flags ( ) to use while executing the block.
- `block`: The block to execute.

## See Also

- [func typeKey(XCUIKeyboardKey, modifierFlags: XCUIElement.KeyModifierFlags)](xcuielement/typekey(_:modifierflags:)-6gaoi.md)
  Types a single key from the XCUIKeyboardKey enumeration with the specified modifier flags.
- [func typeKey(String, modifierFlags: XCUIElement.KeyModifierFlags)](xcuielement/typekey(_:modifierflags:)-9ubn.md)
  Types a single key that a string represents with the flags you specify.
- [struct XCUIKeyboardKey](xcuikeyboardkey.md)
  Constants to represent keys that have no typewritten equivalent.
- [XCUIElement.KeyModifierFlags](xcuielement/keymodifierflags.md)
  Flags for simulating combination keystrokes with keys, such as Control, Option, Shift, and Command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/perform(withkeymodifiers:block:))*