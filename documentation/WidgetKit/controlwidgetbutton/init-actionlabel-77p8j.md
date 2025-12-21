# init(action:label:)

**Framework**: WidgetKit  
**Kind**: init

Creates a button template for a control.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency init(action: Action, @ViewBuilder label: @escaping () -> Label) where ActionLabel == ControlWidgetButtonDefaultActionLabel, Action : AppIntent
```

## Parameters

- `action`: The action your button performs when pressed.
- `label`: A view that renders the button.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/controlwidgetbutton/init(action:label:)-77p8j)*