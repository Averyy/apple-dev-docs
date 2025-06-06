# init(action:label:)

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
@preconcurrency init(action: Action, @ViewBuilder label: @escaping () -> Label) where ActionLabel == ControlWidgetButtonDefaultActionLabel, Action : AppIntent
```

## Parameters

- `action`: The action your button performs when pressed.
- `label`: A view that renders the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/controlwidgetbutton/init(action:label:)-77p8j)*