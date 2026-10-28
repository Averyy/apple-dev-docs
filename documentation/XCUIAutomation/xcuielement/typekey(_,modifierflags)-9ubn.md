# typeKey(_:modifierFlags:)

**Framework**: XCUIAutomation  
**Kind**: method  
**Role**: Instance Method

Types a single key that a string represents with the flags you specify.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- Xcode 16.3+

## Declaration

```swift
@MainActor
func typeKey(_ key: String, modifierFlags flags: XCUIElement.KeyModifierFlags)
```

```objc
- (void) typeKey:(NSString *) key modifierFlags:(XCUIKeyModifierFlags) flags;
```

## Discussion

Although `key` is a string, it must represent a single key on a physical keyboard. Strings that resolve to multiple keys raise an error at runtime.

In addition to literal string key representations like `"a"`, `"6"`, and `"["`, keys such as arrow keys, Command, Control, Option, and function keys can be typed using the constants in [`XCUIKeyboardKey`](../xcuikeyboardkey.md).

## Parameters

- `key`: A string representation of the key to type, or a constant from [`XCUIKeyboardKey`](../xcuikeyboardkey.md) for a key that doesn’t have a single-key string equivalent.
- `flags`: A set of modifier flags ([`XCUIElement.KeyModifierFlags`](./keymodifierflags.md)) to use when typing the key.

## See Also

### Combining keystrokes
- [func typeKey(XCUIKeyboardKey, modifierFlags: XCUIElement.KeyModifierFlags)](./typekey%28_,modifierflags%29-6gaoi.md)
  Types a single key from the XCUIKeyboardKey enumeration with the specified modifier flags.
- [struct XCUIKeyboardKey](../xcuikeyboardkey.md)
  Constants to represent keys that have no typewritten equivalent.
- [class func perform(withKeyModifiers: XCUIElement.KeyModifierFlags, block: () -> Void)](./perform%28withkeymodifiers,block%29.md)
  Executes a block of code while holding a combination keystroke.
- [XCUIElement.KeyModifierFlags](./keymodifierflags.md)
  Flags for simulating combination keystrokes with keys, such as Control, Option, Shift, and Command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/typekey(_:modifierflags:)-9ubn)*