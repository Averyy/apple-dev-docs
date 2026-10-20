# init(action:label:actionLabel:)

**Framework**: WidgetKit  
**Kind**: init  
**Role**: Initializer

Creates a button template for a control.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency init(action: Action, @ViewBuilder label: @escaping () -> Label, @ViewBuilder actionLabel: @escaping (Bool) -> ActionLabel) where Action : AppIntent
```

Available when `Label` conforms to `View` and `ActionLabel` conforms to `View`.

#### Discussion

Use the action label to additionally customize the appearance of this control button while its action is performed

```swift
ControlWidgetButton(action: OpenTrunkIntent()) {
    Label("Open Trunk", systemImage: "car.side.rear.open.crop")
} actionLabel: { isActive in
    if isActive {
        Text("Opening…")
    }
}
```

The example above produces a control button that appears in Control Center with “Open Trunk” as its title and the provided SF symbol. While the control is performing its action, it shows the “Opening…” subtitle.

## Parameters

- `action`: The action your button performs when pressed.
- `label`: A view that renders the button.
- `actionLabel`: A view that is rendered when the button’s action is performed

## See Also

### Initializers
- [init(action: Action, label: () -> Label)](./init%28action,label%29-77p8j.md)
  Creates a button template for a control.
- [init(action: Action, label: () -> Label)](./init%28action,label%29-8oxxp.md)
  Creates a button template for a control that launches an app.
- [init(some StringProtocol, action: Action, actionLabel: (Bool) -> ActionLabel)](./init%28_,action,actionlabel%29-4sgji.md)
  Creates a button template for a control.
- [init(LocalizedStringKey, action: Action, actionLabel: (Bool) -> ActionLabel)](./init%28_,action,actionlabel%29-67uvw.md)
  Creates a button template for a control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/controlwidgetbutton/init(action:label:actionlabel:))*