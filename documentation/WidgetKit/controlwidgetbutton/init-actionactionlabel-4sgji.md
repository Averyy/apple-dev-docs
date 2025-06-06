# init(_:action:actionLabel:)

**Framework**: Widgetkit  
**Kind**: init

Creates a button template for a control.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
@MainActor
@preconcurrency init(_ title: some StringProtocol, action: Action, @ViewBuilder actionLabel: @escaping (Bool) -> ActionLabel) where Action : AppIntent
```

#### Discussion

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

The example above produces a control button that in control center will display the value of `actionName` as its title and the provided SF symbol. While the control is performing its action it will show the “Opening…” subtitle.

## Parameters

- `title`: A string to display as the title of the button.
- `action`: The action your button performs when pressed.
- `actionLabel`: A view that is rendered when the button’s action is performed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/controlwidgetbutton/init(_:action:actionlabel:)-4sgji)*