# settings(context:for:)

**Framework**: HomeExtensions  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Reads the accessory and returns a fresh snapshot of its settings.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@MainActor
func settings(context: Self.Context, for accessory: HMAccessory) async throws -> Self.Container
```

#### Return Value

The accessory’s current settings.

## Parameters

- `context`: The context you supplied to [`HomeAccessorySettings`](../homeaccessorysettings.md).
- `accessory`: The accessory to read settings from.

## See Also

### Accessing the settings
- [func settingsDidChange(changes: [String : Any], context: Self.Context, for: HMAccessory) async throws](./settingsdidchange%28changes,context,for%29.md)
  Tells the provider that a person changed settings in the Home app.
- [associatedtype Container : HomeAccessorySettingsContainer](./container.md)
  The type of container that holds the provider’s settings.
- [associatedtype Context : HomeAccessorySettingsContext](./context.md)
  The type of context that the provider receives on each call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessorysettingsprovider/settings(context:for:))*