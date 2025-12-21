# AppIntentControlValueProvider

**Framework**: WidgetKit  
**Kind**: protocol

A type that uses a custom intent to provide a value to a control template.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 26.0+
- watchOS 26.0+

## Declaration

```swift
protocol AppIntentControlValueProvider
```

#### Overview

The provider quickly and cheaply prepares a synchronous value to be shown while previewing the control in the add sheet. When the actual control needs to be rendered, the actual, current value will be fetched asynchronously.

The provider prepares these values using an intent containing user-editable parameters.

For instance, a control that opens and closes various doors in a user’s home may show a preview of the door being closed. When the actual control is rendered, the control may fetch the configured door’s status from the cloud:

```swift
struct DoorValueProvider: AppIntentControlValueProvider {
    func previewValue(configuration: SelectDoorIntent) -> Door {
        Door(id: configuration.doorId, isOpen: false)
    }

    func currentValue(configuration: SelectDoorIntent) async -> Door {
        let isOpen = await DoorManager.shared
            .status(doorId: configuration.doorId)
        return Door(id: configuration.doorId, isOpen: isOpen)
    }
}
```

## Topics

### Associated Types
- [associatedtype Configuration : ControlConfigurationIntent](appintentcontrolvalueprovider/configuration.md)
  The type of intent used to prepare the value.
- [associatedtype Value](appintentcontrolvalueprovider/value.md)
  The type of value provided to the template.
### Instance Methods
- [func currentValue(configuration: Self.Configuration) async throws -> Self.Value](appintentcontrolvalueprovider/currentvalue(configuration:).md)
  The current value of the control.
- [func previewValue(configuration: Self.Configuration) -> Self.Value](appintentcontrolvalueprovider/previewvalue(configuration:).md)
  A value to be shown while previewing the control in the add sheet.

## See Also

- [protocol ControlValueProvider](controlvalueprovider.md)
  A type that provides a value to a control template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/appintentcontrolvalueprovider)*