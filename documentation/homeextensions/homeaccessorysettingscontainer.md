# HomeAccessorySettingsContainer

**Framework**: HomeExtensions  
**Kind**: protocol  
**Role**: Protocol

A snapshot of an accessory’s settings and their current values.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@MainActor
protocol HomeAccessorySettingsContainer
```

## Overview

Create a type that adopts this protocol, with a property for each setting. Declare each property with one of the setting property wrappers: [`HomeAccessoryToggleSetting`](./homeaccessorytogglesetting.md), [`HomeAccessoryRangeSetting`](./homeaccessoryrangesetting.md), [`HomeAccessoryEnumSetting`](./homeaccessoryenumsetting.md), [`HomeAccessoryTextFieldSetting`](./homeaccessorytextfieldsetting.md), or [`HomeAccessoryInformationSetting`](./homeaccessoryinformationsetting.md). Each wrapper stores details such as the setting’s identifier and label.

List the settings’ projected values (with the `$` prefix) in [`availableSettings`](./homeaccessorysettingscontainer/availablesettings.md), in the order you want them to appear. For example:

```swift
struct ThermostatSettings: HomeAccessorySettingsContainer {
    static let ecoModeID = "eco-mode"

    @HomeAccessoryToggleSetting(id: Self.ecoModeID, label: "Eco Mode")
    var ecoMode: Bool?

    var availableSettings: [any HomeAccessorySetting] { [$ecoMode] }

    init(ecoMode: Bool? = nil) { self.ecoMode = ecoMode }
}
```

Store identifiers as static constants so your provider can reuse them. Your provider should create a new container each time [`settings(context:for:)`](./homeaccessorysettingsprovider/settings%28context,for%29.md) runs, rather than retaining one.

## Topics

### Listing the available settings
- [var availableSettings: [any HomeAccessorySetting]](./homeaccessorysettingscontainer/availablesettings.md)
  The settings to display, in order.

## Relationships

### Conforming Types
- [AnyHomeAccessorySettingsContainer](./anyhomeaccessorysettingscontainer.md)

## See Also

### Displaying accessory configuration
- [protocol HomeAccessorySettingsProvider](./homeaccessorysettingsprovider.md)
  A type that reads and writes an accessory’s settings.
- [struct AnyHomeAccessorySettingsContainer](./anyhomeaccessorysettingscontainer.md)
- [protocol HomeAccessorySettingsContext](./homeaccessorysettingscontext.md)
  A type that holds the resources that your settings provider needs to communicate with an accessory.
- [struct HomeAccessorySettings](./homeaccessorysettings.md)
  Accessory settings that your extension provides to the Home app.
- [struct HomeAccessoryConfiguration](./homeaccessoryconfiguration.md)
  Content that people use to configure an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessorysettingscontainer)*