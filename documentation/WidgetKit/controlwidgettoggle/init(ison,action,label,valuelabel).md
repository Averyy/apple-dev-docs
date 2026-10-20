# init(isOn:action:label:valueLabel:)

**Framework**: WidgetKit  
**Kind**: init  
**Role**: Initializer

Creates a toggle template for a control.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency init(isOn: Bool, action: Action, @ViewBuilder label: @escaping () -> Label, @ViewBuilder valueLabel: @escaping (Bool) -> ValueLabel) where Action : SetValueIntent, Action.ValueType == Bool
```

Available when `Label` conforms to `View` and `ValueLabel` conforms to `View`.

## Parameters

- `isOn`: A boolean value that describes the current value of the toggle.
- `action`: The action the toggle performs when pressed.
- `label`: A view that renders the toggle’s label.
- `valueLabel`: A view that renders the toggle’s value. The boolean parameter represents the value.

## See Also

### Initializers
- [init(isOn: Bool, action: Action, label: () -> Label)](./init%28ison,action,label%29.md)
  Creates a toggle template for a control.
- [init(some StringProtocol, isOn: Bool, action: Action, valueLabel: (Bool) -> ValueLabel)](./init%28_,ison,action,valuelabel%29-33wfq.md)
  Creates a toggle template for a control.
- [init(LocalizedStringKey, isOn: Bool, action: Action, valueLabel: (Bool) -> ValueLabel)](./init%28_,ison,action,valuelabel%29-5o6bn.md)
  Creates a toggle template for a control.
- [init(LocalizedStringResource, isOn: Bool, action: Action, valueLabel: (Bool) -> ValueLabel)](./init%28_,ison,action,valuelabel%29-4lk32.md)
  Creates a toggle template for a control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/controlwidgettoggle/init(ison:action:label:valuelabel:))*