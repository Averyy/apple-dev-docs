# HomeAccessorySettings

**Framework**: HomeExtensions  
**Kind**: struct  
**Role**: Structure

Accessory settings that your extension provides to the Home app.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@MainActor
struct HomeAccessorySettings
```

## Overview

Provide a [`HomeAccessorySettingsProvider`](./homeaccessorysettingsprovider.md) that reads and writes the settings, and a [`HomeAccessorySettingsContext`](./homeaccessorysettingscontext.md) that the provider uses to communicate with the accessory.

## Topics

### Creating an accessory setting
- [init<Provider>(context: () -> Provider.Context, provider: () -> Provider, filter: HomeAccessoryConfiguration.SupportsAccessory)](./homeaccessorysettings/init%28context,provider,filter%29.md)
  Creates accessory settings backed by a provider.

## Relationships

### Conforms To
- [HomeContent](./homecontent.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Displaying accessory configuration
- [protocol HomeAccessorySettingsProvider](./homeaccessorysettingsprovider.md)
  A type that reads and writes an accessory’s settings.
- [protocol HomeAccessorySettingsContainer](./homeaccessorysettingscontainer.md)
  A snapshot of an accessory’s settings and their current values.
- [struct AnyHomeAccessorySettingsContainer](./anyhomeaccessorysettingscontainer.md)
- [protocol HomeAccessorySettingsContext](./homeaccessorysettingscontext.md)
  A type that holds the resources that your settings provider needs to communicate with an accessory.
- [struct HomeAccessoryConfiguration](./homeaccessoryconfiguration.md)
  Content that people use to configure an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessorysettings)*