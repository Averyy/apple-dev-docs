# HomeAccessorySettingsContext

**Framework**: HomeExtensions  
**Kind**: protocol  
**Role**: Protocol

A type that holds the resources that your settings provider needs to communicate with an accessory.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
protocol HomeAccessorySettingsContext
```

## Overview

For example, a context might hold a web service client, a Matter handle, or cached identifiers. The framework passes it to your provider on every call:

```swift
struct ThermostatContext: HomeAccessorySettingsContext {
    let webService: ThermostatWebService
}
```

If your provider doesn’t need a context, declare an empty type like the following:

```swift
struct NoContext: HomeAccessorySettingsContext { }
```

## See Also

### Displaying accessory configuration
- [protocol HomeAccessorySettingsProvider](./homeaccessorysettingsprovider.md)
  A type that reads and writes an accessory’s settings.
- [protocol HomeAccessorySettingsContainer](./homeaccessorysettingscontainer.md)
  A snapshot of an accessory’s settings and their current values.
- [struct AnyHomeAccessorySettingsContainer](./anyhomeaccessorysettingscontainer.md)
- [struct HomeAccessorySettings](./homeaccessorysettings.md)
  Accessory settings that your extension provides to the Home app.
- [struct HomeAccessoryConfiguration](./homeaccessoryconfiguration.md)
  Content that people use to configure an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessorysettingscontext)*