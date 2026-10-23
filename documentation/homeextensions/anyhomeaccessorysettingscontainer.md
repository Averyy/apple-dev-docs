# AnyHomeAccessorySettingsContainer

**Framework**: HomeExtensions  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@MainActor
struct AnyHomeAccessorySettingsContainer
```

## Topics

### Initializers
- [init(erasing: some HomeAccessorySettingsContainer)](./anyhomeaccessorysettingscontainer/init%28erasing%29.md)

## Relationships

### Conforms To
- [HomeAccessorySettingsContainer](./homeaccessorysettingscontainer.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Displaying accessory configuration
- [protocol HomeAccessorySettingsProvider](./homeaccessorysettingsprovider.md)
  A type that reads and writes an accessory’s settings.
- [protocol HomeAccessorySettingsContainer](./homeaccessorysettingscontainer.md)
  A snapshot of an accessory’s settings and their current values.
- [protocol HomeAccessorySettingsContext](./homeaccessorysettingscontext.md)
  A type that holds the resources that your settings provider needs to communicate with an accessory.
- [struct HomeAccessorySettings](./homeaccessorysettings.md)
  Accessory settings that your extension provides to the Home app.
- [struct HomeAccessoryConfiguration](./homeaccessoryconfiguration.md)
  Content that people use to configure an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/anyhomeaccessorysettingscontainer)*