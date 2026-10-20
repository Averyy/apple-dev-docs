# AXMenuItemModifiers

**Framework**: Application Services  
**Kind**: struct  
**Role**: Structure

Values that indicate the keyboard shortcut modifiers for a menu item (used with the kAXMenuItemCmdModifiersAttribute attribute).

**Availability**:
- macOS 10.9+

## Declaration

```swift
struct AXMenuItemModifiers
```

```c
typedef enum AXMenuItemModifiers : UInt32 {
    ...
} AXMenuItemModifiers;
```

## Topics

### Initializers
- [init(rawValue: UInt32)](./axmenuitemmodifiers/api-1460320-init.md)
### Type Properties
- [static var control: AXMenuItemModifiers](./axmenuitemmodifiers/api-1464333-control.md)
- [static var noCommand: AXMenuItemModifiers](./axmenuitemmodifiers/api-1464506-nocommand.md)
- [static var option: AXMenuItemModifiers](./axmenuitemmodifiers/api-1462352-option.md)
- [static var shift: AXMenuItemModifiers](./axmenuitemmodifiers/api-1461092-shift.md)

## Relationships

### Conforms To
- [OptionSet](../Swift/optionset.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Related Documentation
- [struct AXMenuItemModifiers](./axmenuitemmodifiers.md)
  Values that indicate the keyboard shortcut modifiers for a menu item (used with the kAXMenuItemCmdModifiersAttribute attribute).


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/axmenuitemmodifiers)*