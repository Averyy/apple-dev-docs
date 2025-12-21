# ControlWidgetToggle

**Framework**: WidgetKit  
**Kind**: struct

A control template representing a toggle.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 26.0+
- watchOS 26.0+

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
  Creates a toggle template for a control.
- [init(isOn: Bool, action: Action, label: () -> Label, valueLabel: (Bool) -> ValueLabel)](controlwidgettoggle/init(ison:action:label:valuelabel:).md)
  Creates a toggle template for a control.
- [init(some StringProtocol, isOn: Bool, action: Action, valueLabel: (Bool) -> ValueLabel)](controlwidgettoggle/init(_:ison:action:valuelabel:)-33wfq.md)
  Creates a toggle template for a control.
- [init(LocalizedStringKey, isOn: Bool, action: Action, valueLabel: (Bool) -> ValueLabel)](controlwidgettoggle/init(_:ison:action:valuelabel:)-5o6bn.md)
  Creates a toggle template for a control.
- [init(LocalizedStringResource, isOn: Bool, action: Action, valueLabel: (Bool) -> ValueLabel)](controlwidgettoggle/init(_:ison:action:valuelabel:)-4lk32.md)
  Creates a toggle template for a control.
### Default action label
- [struct ControlWidgetToggleDefaultLabel](controlwidgettoggledefaultlabel.md)
  A view that represents the default label for a toggle control if you don’t provide a label.

## Relationships

### Conforms To
- [ControlWidgetTemplate](../SwiftUI/ControlWidgetTemplate.md)

## See Also

- [Creating controls to perform actions across the system](creating-controls-to-perform-actions-across-the-system.md)
  Perform your app’s actions from Control Center, the Lock Screen, and the Action button.
- [Adding refinements and configuration to controls](adding-refinements-and-configuration-to-controls.md)
  Customize the way controls display across the system and offer people the ability to configure them.
- [struct StaticControlConfiguration](staticcontrolconfiguration.md)
  The description of a control that has no user-configurable options.
- [struct AppIntentControlConfiguration](appintentcontrolconfiguration.md)
  The description of a control that uses a custom app intent to provide user-configurable options.
- [class ControlCenter](controlcenter.md)
  An object you use to access configuration information for controls and reload them.
- [struct ControlInfo](controlinfo.md)
  A structure that contains information about user-configured controls.
- [struct ControlWidgetButton](controlwidgetbutton.md)
  A control template representing a button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/controlwidgettoggle)*