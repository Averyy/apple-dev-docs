# init(_:isOn:action:valueLabel:)

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
@preconcurrency init(_ title: some StringProtocol, isOn: Bool, action: Action, @ViewBuilder valueLabel: @escaping (Bool) -> ValueLabel) where Action : SetValueIntent, Action.ValueType == Bool
```

## Parameters

- `title`: A string to display as the title of the toggle.
- `isOn`: A boolean value that describes the current value of the   toggle.
- `action`: The action the toggle performs when pressed.
- `valueLabel`: A view that renders the toggle’s value. The boolean   parameter represents the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/controlwidgettoggle/init(_:ison:action:valuelabel:)-33wfq)*