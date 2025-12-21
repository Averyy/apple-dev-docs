# ControlWidgetButton

**Framework**: WidgetKit  
**Kind**: struct

A control template representing a button.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency struct ControlWidgetButton<Label, ActionLabel, Action> where Label : View, ActionLabel : View
```

#### Overview

Buttons don’t have state; use them for fire-and-forget actions such as playing a sound or launching an app.

## Topics

### Initializers
- [init(action: Action, label: () -> Label)](controlwidgetbutton/init(action:label:)-77p8j.md)
  Creates a button template for a control.
- [init(action: Action, label: () -> Label)](controlwidgetbutton/init(action:label:)-8oxxp.md)
  Creates a button template for a control that launches an app.
- [init(action: Action, label: () -> Label, actionLabel: (Bool) -> ActionLabel)](controlwidgetbutton/init(action:label:actionlabel:).md)
  Creates a button template for a control.
- [init(action: Action, label: () -> Label, actionLabel: (Bool) -> ActionLabel)](controlwidgetbutton/init(action:label:actionlabel:).md)
  Creates a button template for a control.
- [init(some StringProtocol, action: Action, actionLabel: (Bool) -> ActionLabel)](controlwidgetbutton/init(_:action:actionlabel:)-4sgji.md)
  Creates a button template for a control.
- [init(LocalizedStringKey, action: Action, actionLabel: (Bool) -> ActionLabel)](controlwidgetbutton/init(_:action:actionlabel:)-67uvw.md)
  Creates a button template for a control.
- [init(LocalizedStringResource, action: Action, actionLabel: (Bool) -> ActionLabel)](controlwidgetbutton/init(_:action:actionlabel:)-1kxch.md)
  Creates a button template for a control.
### Default action label
- [struct ControlWidgetButtonDefaultActionLabel](controlwidgetbuttondefaultactionlabel.md)
  A view representing the default action label for a `ControlWidgetButton` if none is specified.

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
- [struct ControlWidgetToggle](controlwidgettoggle.md)
  A control template representing a toggle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/controlwidgetbutton)*