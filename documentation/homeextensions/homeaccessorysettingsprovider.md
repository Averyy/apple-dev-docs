# HomeAccessorySettingsProvider

**Framework**: HomeExtensions  
**Kind**: protocol  
**Role**: Protocol

A type that reads and writes an accessory’s settings.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@MainActor
protocol HomeAccessorySettingsProvider
```

#### Overview

A provider has two responsibilities:

- In [`settings(context:for:)`](./homeaccessorysettingsprovider/settings%28context,for%29.md), it reads the accessory and returns a fresh snapshot of its settings.
- In [`settingsDidChange(changes:context:for:)`](./homeaccessorysettingsprovider/settingsdidchange%28changes,context,for%29.md), it applies the person’s changes to the accessory.

The provider itself doesn’t store any setting values.

Declare your settings in a [`HomeAccessorySettingsContainer`](./homeaccessorysettingscontainer.md), and create a new instance of it in [`settings(context:for:)`](./homeaccessorysettingsprovider/settings%28context,for%29.md).

When a person changes a setting, [`settingsDidChange(changes:context:for:)`](./homeaccessorysettingsprovider/settingsdidchange%28changes,context,for%29.md) receives the new values keyed by setting identifier. Cast each value to match its setting: `Bool` for a toggle, `NSNumber` for a range, and `String` for an enumeration (its raw value) or a text field. Information settings are read-only, so they never appear in the dictionary.

For example, the following provider manages a thermostat’s eco mode setting:

```swift
struct ThermostatProvider: HomeAccessorySettingsProvider {
    func settings(context: ThermostatContext, for accessory: HMAccessory) async throws -> ThermostatSettings {
        // Build a fresh snapshot each call; pass nil for anything you couldn't read.
        ThermostatSettings(ecoMode: try await context.webService.isEcoOn())
    }

    func settingsDidChange(changes: [String: Any], context: ThermostatContext, for accessory: HMAccessory) async throws {
        for (id, value) in changes {
            switch id {
            case ThermostatSettings.ecoModeID:
                try await context.webService.setEco(value as? Bool ?? false)   // await the write — see note
            default:
                break
            }
        }
    }
}
```

When implementing a provider, do the following:

- Keep your implementation of [`settings(context:for:)`](./homeaccessorysettingsprovider/settings%28context,for%29.md) fast. The framework calls it when the settings appear and again after every change.
- Write only the settings you receive in [`settingsDidChange(changes:context:for:)`](./homeaccessorysettingsprovider/settingsdidchange%28changes,context,for%29.md). Don’t rebuild or return state there.
- Await your device write before returning. The framework reads the settings again immediately afterward.
- Return `nil` for any value you can’t read reliably.
- Set custom labels and states on every snapshot. Values such as `label`, `isEnabled`, and `isHidden` are part of each snapshot, so a value you set once on a cached container doesn’t persist.
- Assign complete labels. Assigning a string, such as `$ecoMode.label = "New Title"`, clears the [`detailedLabel`](./homeaccessorysettinglabel/detailedlabel.md). To preserve it, assign both values.
- Use unique setting identifiers across all your providers. The framework uses identifiers to route each change to the provider that owns the setting.

## Topics

### Accessing the settings
- [func settings(context: Self.Context, for: HMAccessory) async throws -> Self.Container](./homeaccessorysettingsprovider/settings%28context,for%29.md)
  Reads the accessory and returns a fresh snapshot of its settings.
- [func settingsDidChange(changes: [String : Any], context: Self.Context, for: HMAccessory) async throws](./homeaccessorysettingsprovider/settingsdidchange%28changes,context,for%29.md)
  Tells the provider that a person changed settings in the Home app.
- [associatedtype Container : HomeAccessorySettingsContainer](./homeaccessorysettingsprovider/container.md)
  The type of container that holds the provider’s settings.
- [associatedtype Context : HomeAccessorySettingsContext](./homeaccessorysettingsprovider/context.md)
  The type of context that the provider receives on each call.

## See Also

### Displaying accessory configuration
- [protocol HomeAccessorySettingsContainer](./homeaccessorysettingscontainer.md)
  A snapshot of an accessory’s settings and their current values.
- [struct AnyHomeAccessorySettingsContainer](./anyhomeaccessorysettingscontainer.md)
- [protocol HomeAccessorySettingsContext](./homeaccessorysettingscontext.md)
  A type that holds the resources that your settings provider needs to communicate with an accessory.
- [struct HomeAccessorySettings](./homeaccessorysettings.md)
  Accessory settings that your extension provides to the Home app.
- [struct HomeAccessoryConfiguration](./homeaccessoryconfiguration.md)
  Content that people use to configure an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessorysettingsprovider)*