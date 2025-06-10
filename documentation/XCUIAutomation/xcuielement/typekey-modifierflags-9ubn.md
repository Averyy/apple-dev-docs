# typeKey(_:modifierFlags:)

**Framework**: XCUIAutomation  
**Kind**: method

Types a single key that a string represents with the flags you specify.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- Xcode 16.3+

## Declaration

```swift
@MainActor
func typeKey(_ key: String, modifierFlags flags: XCUIElement.KeyModifierFlags)
```

#### Discussion

Although `key` is a string, it must represent a single key on a physical keyboard. Strings that resolve to multiple keys raise an error at runtime.

In addition to literal string key representations like `"a"`, `"6"`, and `"["`, keys such as arrow keys, Command, Control, Option, and function keys can be typed using the constants in [`XCUIKeyboardKey`](xcuikeyboardkey.md).

## Parameters

- `key`: A string representation of the key to type, or a constant from   for a key that doesn’t have a single-key string equivalent.
- `flags`: A set of modifier flags ( ) to use when typing the key.

## See Also

- [func typeKey(XCUIKeyboardKey, modifierFlags: XCUIElement.KeyModifierFlags)](xcuielement/typekey(_:modifierflags:)-6gaoi.md)
  Types a single key from the XCUIKeyboardKey enumeration with the specified modifier flags.
- [struct XCUIKeyboardKey](xcuikeyboardkey.md)
  Constants to represent keys that have no typewritten equivalent.
- [class func perform(withKeyModifiers: XCUIElement.KeyModifierFlags, block: () -> Void)](xcuielement/perform(withkeymodifiers:block:).md)
  Executes a block of code while holding a combination keystroke.
- [XCUIElement.KeyModifierFlags](xcuielement/keymodifierflags.md)
  Flags for simulating combination keystrokes with keys, such as Control, Option, Shift, and Command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/typekey(_:modifierflags:)-9ubn)*