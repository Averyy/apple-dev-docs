# init(action:label:)

**Framework**: WidgetKit  
**Kind**: init  
**Role**: Initializer

Creates a button template for a control that launches an app.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency init(action: Action, @ViewBuilder label: @escaping () -> Label) where ActionLabel == ControlWidgetButtonDefaultActionLabel, Action : OpenIntent
```

Available when `Label` conforms to `View` and `ActionLabel` conforms to `View`.

## Parameters

- `action`: The action your button performs when pressed.
- `label`: A view that renders the button.

## See Also

### Initializers
- [init(action: Action, label: () -> Label)](./init%28action,label%29-77p8j.md)
  Creates a button template for a control.
- [init(action: Action, label: () -> Label, actionLabel: (Bool) -> ActionLabel)](./init%28action,label,actionlabel%29.md)
  Creates a button template for a control.
- [init(action: Action, label: () -> Label, actionLabel: (Bool) -> ActionLabel)](./init%28action,label,actionlabel%29.md)
  Creates a button template for a control.
- [init(some StringProtocol, action: Action, actionLabel: (Bool) -> ActionLabel)](./init%28_,action,actionlabel%29-4sgji.md)
  Creates a button template for a control.
- [init(LocalizedStringKey, action: Action, actionLabel: (Bool) -> ActionLabel)](./init%28_,action,actionlabel%29-67uvw.md)
  Creates a button template for a control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/controlwidgetbutton/init(action:label:)-8oxxp)*