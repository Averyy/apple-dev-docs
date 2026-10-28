# init(_:action:actionLabel:)

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
@preconcurrency init(_ title: some StringProtocol, action: Action, @ViewBuilder actionLabel: @escaping (Bool) -> ActionLabel) where Action : AppIntent
```

Available when `Label` is `Text` and `ActionLabel` conforms to `View`.

## Discussion

Use the action label to additionally customize the appearance of this control button while its action is performed

```swift
ControlWidgetButton(
    configuration.actionName,
    action: OpenTrunkIntent(configuration.id)
) { isActive in
    Image(systemName: "car.side.rear.open.crop")
    if isActive {
        Text("Opening...")
    }
}
```

The example above produces a control button that appears in Control Center with the value of `actionName` as its title and the provided SF symbol. While the control is performing, its action it shows the “Opening…” subtitle.

## Parameters

- `title`: A string to display as the title of the button.
- `action`: The action your button performs when pressed.
- `actionLabel`: A view that is rendered when the button’s action is performed.

## See Also

### Initializers
- [init(action: Action, label: () -> Label)](./init%28action,label%29-77p8j.md)
  Creates a button template for a control.
- [init(action: Action, label: () -> Label)](./init%28action,label%29-8oxxp.md)
  Creates a button template for a control that launches an app.
- [init(action: Action, label: () -> Label, actionLabel: (Bool) -> ActionLabel)](./init%28action,label,actionlabel%29.md)
  Creates a button template for a control.
- [init(action: Action, label: () -> Label, actionLabel: (Bool) -> ActionLabel)](./init%28action,label,actionlabel%29.md)
  Creates a button template for a control.
- [init(LocalizedStringKey, action: Action, actionLabel: (Bool) -> ActionLabel)](./init%28_,action,actionlabel%29-67uvw.md)
  Creates a button template for a control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/controlwidgetbutton/init(_:action:actionlabel:)-4sgji)*