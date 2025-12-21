# ControlValueProvider

**Framework**: WidgetKit  
**Kind**: protocol

A type that provides a value to a control template.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 26.0+
- watchOS 26.0+

## Declaration

```swift
protocol ControlValueProvider
```

#### Overview

The provider quickly and cheaply prepares a synchronous value to be shown while previewing the control in the add sheet. When the actual control needs to be rendered, the actual, current value will be fetched asynchronously.

For instance, a control that opens and closes a garage door may show a preview of the door being closed. When the actual control is rendered, the control may fetch the door’s status from the cloud:

```swift
struct GarageDoorValueProvider: ControlValueProvider {
    var previewValue: Bool { false }

    func currentValue() async -> Bool {
        await GarageDoorManager.shared.doorStatus()
    }
}
```

## Topics

### Associated Types
- [associatedtype Value](controlvalueprovider/value.md)
  The type of value provided to the template.
### Instance Properties
- [var previewValue: Self.Value](controlvalueprovider/previewvalue.md)
  A value to be shown while previewing the control in the add sheet.
### Instance Methods
- [func currentValue() async throws -> Self.Value](controlvalueprovider/currentvalue.md)
  The current value of the control.

## See Also

- [protocol AppIntentControlValueProvider](appintentcontrolvalueprovider.md)
  A type that uses a custom intent to provide a value to a control template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/controlvalueprovider)*