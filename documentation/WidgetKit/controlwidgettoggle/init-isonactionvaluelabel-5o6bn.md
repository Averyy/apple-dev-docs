# init(_:isOn:action:valueLabel:)

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
@preconcurrency init(_ titleKey: LocalizedStringKey, isOn: Bool, action: Action, @ViewBuilder valueLabel: @escaping (Bool) -> ValueLabel) where Action : SetValueIntent, Action.ValueType == Bool
```

## Parameters

- `titleKey`: The key to a localized string to display as the title of   the toggle.
- `isOn`: A boolean value that describes the current value of the   toggle.
- `action`: The action the toggle performs when pressed.
- `valueLabel`: A view that renders the toggle’s value. The boolean   parameter represents the value.

## See Also

- [init(isOn: Bool, action: Action, label: () -> Label)](controlwidgettoggle/init(ison:action:label:).md)
  Creates a toggle template for a control.
- [init(isOn: Bool, action: Action, label: () -> Label, valueLabel: (Bool) -> ValueLabel)](controlwidgettoggle/init(ison:action:label:valuelabel:).md)
  Creates a toggle template for a control.
- [init(some StringProtocol, isOn: Bool, action: Action, valueLabel: (Bool) -> ValueLabel)](controlwidgettoggle/init(_:ison:action:valuelabel:)-33wfq.md)
  Creates a toggle template for a control.
- [init(LocalizedStringResource, isOn: Bool, action: Action, valueLabel: (Bool) -> ValueLabel)](controlwidgettoggle/init(_:ison:action:valuelabel:)-4lk32.md)
  Creates a toggle template for a control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/controlwidgettoggle/init(_:ison:action:valuelabel:)-5o6bn)*