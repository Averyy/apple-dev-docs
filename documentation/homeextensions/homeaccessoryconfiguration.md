# HomeAccessoryConfiguration

**Framework**: HomeExtensions  
**Kind**: struct  
**Role**: Structure

Content that people use to configure an accessory.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@MainActor
struct HomeAccessoryConfiguration
```

## Overview

Provide the configuration view, and optionally a filter that limits which accessories it applies to.

## Topics

### Creating an accessory configuration
- [init(id: HomeContentID, content: () -> some View, filter: HomeAccessoryConfiguration.SupportsAccessory)](./homeaccessoryconfiguration/init%28id,content,filter%29.md)
  Creates a configuration with an identifier and a view.
- [HomeAccessoryConfiguration.SupportsAccessory](./homeaccessoryconfiguration/supportsaccessory.md)
  A closure that determines whether content applies to an accessory.
### Customizing presentation
- [func hidesNavigationTitleInLandscape(Bool) -> HomeAccessoryConfiguration](./homeaccessoryconfiguration/hidesnavigationtitleinlandscape%28_%29.md)
  Hides or shows the Home app’s navigation title and app icon in landscape.

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
- [struct HomeAccessorySettings](./homeaccessorysettings.md)
  Accessory settings that your extension provides to the Home app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessoryconfiguration)*