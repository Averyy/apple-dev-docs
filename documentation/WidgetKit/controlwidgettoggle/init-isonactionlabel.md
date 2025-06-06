# init(isOn:action:label:)

**Framework**: Widgetkit  
**Kind**: init

Creates a toggle template for a control widget.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
@MainActor
@preconcurrency init(isOn: Bool, action: Action, @ViewBuilder label: @escaping () -> Label) where ValueLabel == ControlWidgetToggleDefaultLabel, Action : SetValueIntent, Action.ValueType == Bool
```

#### Discussion

The toggle will use “On” and “Off” as default value label.

## Parameters

- `isOn`: A boolean value that describes the current value of the   toggle.
- `action`: The action the toggle performs when pressed.
- `label`: A view that renders the toggle’s label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/controlwidgettoggle/init(ison:action:label:))*