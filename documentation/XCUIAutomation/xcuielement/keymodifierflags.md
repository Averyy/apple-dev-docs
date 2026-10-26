# XCUIElement.KeyModifierFlags

**Framework**: XCUIAutomation  
**Kind**: struct  
**Role**: Structure

Flags for simulating combination keystrokes with keys, such as Control, Option, Shift, and Command.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS
- Xcode 16.3+

## Declaration

```swift
struct KeyModifierFlags
```

```c
enum XCUIKeyModifierFlags : NSUInteger;
```

#### Overview

Use these flags with the [`typeKey(_:modifierFlags:)`](./typekey%28_,modifierflags%29-6gaoi.md) and [`perform(withKeyModifiers:block:)`](./perform%28withkeymodifiers,block%29.md) methods to simulate combination keystrokes while an action occurs.

## Topics

### Flags for combination keys
- [static var command: XCUIElement.KeyModifierFlags](./keymodifierflags/command.md)
  The Command key in a combination keystroke.
- [static var control: XCUIElement.KeyModifierFlags](./keymodifierflags/control.md)
  The Control key in a combination keystroke.
- [static var option: XCUIElement.KeyModifierFlags](./keymodifierflags/option.md)
  The Option key in a combination keystroke.
- [static var shift: XCUIElement.KeyModifierFlags](./keymodifierflags/shift.md)
  The Shift key in a combination keystroke.
- [static var capsLock: XCUIElement.KeyModifierFlags](./keymodifierflags/capslock.md)
  The Caps Lock key in a combination keystroke.
- [static var function: XCUIElement.KeyModifierFlags](./keymodifierflags/function.md)
  The Function key in a combination keystroke.
### Initializers
- [init(rawValue: UInt)](./keymodifierflags/init%28rawvalue%29.md)
  Creates a flag that represents a key in a combination keystroke with the specified raw value.
### Legacy flags for combination keys
- [static var alphaShift: XCUIElement.KeyModifierFlags](./keymodifierflags/alphashift.md)
  The Caps Lock key in a combination keystroke.
- [static var alternate: XCUIElement.KeyModifierFlags](./keymodifierflags/alternate.md)
  The Option key in a combination keystroke.
### Enumeration Cases
- [XCUIKeyModifierNone](../xcuikeymodifierflags/xcuikeymodifiernone.md)
  Indicates no key modifier.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Combining keystrokes
- [func typeKey(XCUIKeyboardKey, modifierFlags: XCUIElement.KeyModifierFlags)](./typekey%28_,modifierflags%29-6gaoi.md)
  Types a single key from the XCUIKeyboardKey enumeration with the specified modifier flags.
- [func typeKey(String, modifierFlags: XCUIElement.KeyModifierFlags)](./typekey%28_,modifierflags%29-9ubn.md)
  Types a single key that a string represents with the flags you specify.
- [struct XCUIKeyboardKey](../xcuikeyboardkey.md)
  Constants to represent keys that have no typewritten equivalent.
- [class func perform(withKeyModifiers: XCUIElement.KeyModifierFlags, block: () -> Void)](./perform%28withkeymodifiers,block%29.md)
  Executes a block of code while holding a combination keystroke.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/keymodifierflags)*