# init(isOn:action:label:valueLabel:)

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
@preconcurrency init(isOn: Bool, action: Action, @ViewBuilder label: @escaping () -> Label, @ViewBuilder valueLabel: @escaping (Bool) -> ValueLabel) where Action : SetValueIntent, Action.ValueType == Bool
```

## Parameters

- `isOn`: A boolean value that describes the current value of the   toggle.
- `action`: The action the toggle performs when pressed.
- `label`: A view that renders the toggle’s label.
- `valueLabel`: A view that renders the toggle’s value. The boolean   parameter represents the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/controlwidgettoggle/init(ison:action:label:valuelabel:))*