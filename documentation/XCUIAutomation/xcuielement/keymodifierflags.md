# XCUIElement.KeyModifierFlags

**Framework**: Xcuiautomation  
**Kind**: struct

Flags for simulating combination keystrokes with keys, such as Control, Option, Shift, and Command.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Xcode 16.3+

## Declaration

```swift
struct KeyModifierFlags
```

#### Overview

Use these flags with the [`typeKey(_:modifierFlags:)`](xcuielement/typekey(_:modifierflags:)-6gaoi.md) and [`perform(withKeyModifiers:block:)`](xcuielement/perform(withkeymodifiers:block:).md) methods to simulate combination keystrokes while an action occurs.

## Topics

### Flags for combination keys
- [static var command: XCUIElement.KeyModifierFlags](xcuielement/keymodifierflags/command.md)
  The Command key in a combination keystroke.
- [static var control: XCUIElement.KeyModifierFlags](xcuielement/keymodifierflags/control.md)
  The Control key in a combination keystroke.
- [static var option: XCUIElement.KeyModifierFlags](xcuielement/keymodifierflags/option.md)
  The Option key in a combination keystroke.
- [static var shift: XCUIElement.KeyModifierFlags](xcuielement/keymodifierflags/shift.md)
  The Shift key in a combination keystroke.
- [static var capsLock: XCUIElement.KeyModifierFlags](xcuielement/keymodifierflags/capslock.md)
  The Caps Lock key in a combination keystroke.
- [static var function: XCUIElement.KeyModifierFlags](xcuielement/keymodifierflags/function.md)
  The Function key in a combination keystroke.
### Initializers
- [init(rawValue: UInt)](xcuielement/keymodifierflags/init(rawvalue:).md)
  Creates a flag that represents a key in a combination keystroke with the specified raw value.
### Legacy flags for combination keys
- [static var alphaShift: XCUIElement.KeyModifierFlags](xcuielement/keymodifierflags/alphashift.md)
  The Caps Lock key in a combination keystroke.
- [static var alternate: XCUIElement.KeyModifierFlags](xcuielement/keymodifierflags/alternate.md)
  The Option key in a combination keystroke.
### Default Implementations
- [Equatable Implementations](xcuielement/keymodifierflags/equatable-implementations.md)
- [OptionSet Implementations](xcuielement/keymodifierflags/optionset-implementations.md)
- [SetAlgebra Implementations](xcuielement/keymodifierflags/setalgebra-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func typeKey(XCUIKeyboardKey, modifierFlags: XCUIElement.KeyModifierFlags)](xcuielement/typekey(_:modifierflags:)-6gaoi.md)
  Types a single key from the XCUIKeyboardKey enumeration with the specified modifier flags.
- [func typeKey(String, modifierFlags: XCUIElement.KeyModifierFlags)](xcuielement/typekey(_:modifierflags:)-9ubn.md)
  Types a single key that a string represents with the flags you specify.
- [struct XCUIKeyboardKey](xcuikeyboardkey.md)
  Constants to represent keys that have no typewritten equivalent.
- [class func perform(withKeyModifiers: XCUIElement.KeyModifierFlags, block: () -> Void)](xcuielement/perform(withkeymodifiers:block:).md)
  Executes a block of code while holding a combination keystroke.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/keymodifierflags)*