# ControlWidgetToggle

**Framework**: WidgetKit  
**Kind**: struct

A control template representing a toggle.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency struct ControlWidgetToggle<Label, ValueLabel, Action> where Label : View, ValueLabel : View
```

#### Overview

Toggles are controls that have two states, “off” and “on”.

## Topics

### Initializers
- [init(isOn: Bool, action: Action, label: () -> Label)](controlwidgettoggle/init(ison:action:label:).md)
  Creates a toggle template for a control widget.
- [init(isOn: Bool, action: Action, label: () -> Label, valueLabel: (Bool) -> ValueLabel)](controlwidgettoggle/init(ison:action:label:valuelabel:).md)
  Creates a toggle template for a control widget.
- [init(some StringProtocol, isOn: Bool, action: Action, valueLabel: (Bool) -> ValueLabel)](controlwidgettoggle/init(_:ison:action:valuelabel:)-33wfq.md)
  Creates a toggle template for a control widget.
- [init(LocalizedStringKey, isOn: Bool, action: Action, valueLabel: (Bool) -> ValueLabel)](controlwidgettoggle/init(_:ison:action:valuelabel:)-5o6bn.md)
  Creates a toggle template for a control widget.
- [init(LocalizedStringResource, isOn: Bool, action: Action, valueLabel: (Bool) -> ValueLabel)](controlwidgettoggle/init(_:ison:action:valuelabel:)-4lk32.md)
  Creates a toggle template for a control widget.
### Default action label
- [struct ControlWidgetToggleDefaultLabel](controlwidgettoggledefaultlabel.md)
  A view representing the default label for a `ControlWidgetToggle` if none is specified.

## Relationships

### Conforms To
- [ControlWidgetTemplate](../SwiftUI/ControlWidgetTemplate.md)

## See Also

- [Creating controls to perform actions across the system](creating-controls-to-perform-actions-across-the-system.md)
  Perform your app’s actions from Control Center, the Lock Screen, and the Action button.
- [Adding refinements and configuration to controls](adding-refinements-and-configuration-to-controls.md)
  Customize the way controls display across the system and offer people the ability to configure them.
- [class ControlCenter](controlcenter.md)
  An object that contains a list of user-configured controls and is used for reloading controls.
- [struct ControlWidgetButton](controlwidgetbutton.md)
  A control template representing a button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/controlwidgettoggle)*