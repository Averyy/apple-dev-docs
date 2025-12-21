# init(isOn:action:label:valueLabel:)

**Framework**: WidgetKit  
**Kind**: init

Creates a toggle template for a control.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 26.0+
- watchOS 26.0+

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

## See Also

- [init(isOn: Bool, action: Action, label: () -> Label)](controlwidgettoggle/init(ison:action:label:).md)
  Creates a toggle template for a control.
- [init(some StringProtocol, isOn: Bool, action: Action, valueLabel: (Bool) -> ValueLabel)](controlwidgettoggle/init(_:ison:action:valuelabel:)-33wfq.md)
  Creates a toggle template for a control.
- [init(LocalizedStringKey, isOn: Bool, action: Action, valueLabel: (Bool) -> ValueLabel)](controlwidgettoggle/init(_:ison:action:valuelabel:)-5o6bn.md)
  Creates a toggle template for a control.
- [init(LocalizedStringResource, isOn: Bool, action: Action, valueLabel: (Bool) -> ValueLabel)](controlwidgettoggle/init(_:ison:action:valuelabel:)-4lk32.md)
  Creates a toggle template for a control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/controlwidgettoggle/init(ison:action:label:valuelabel:))*