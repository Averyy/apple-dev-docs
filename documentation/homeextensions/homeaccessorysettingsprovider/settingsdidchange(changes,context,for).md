# settingsDidChange(changes:context:for:)

**Framework**: HomeExtensions  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the provider that a person changed settings in the Home app.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@MainActor
func settingsDidChange(changes: [String : Any], context: Self.Context, for accessory: HMAccessory) async throws
```

## Parameters

- `changes`: The new values, keyed by setting identifier.
- `context`: The context you supplied to [`HomeAccessorySettings`](../homeaccessorysettings.md).
- `accessory`: The accessory to update.

## See Also

### Accessing the settings
- [func settings(context: Self.Context, for: HMAccessory) async throws -> Self.Container](./settings%28context,for%29.md)
  Reads the accessory and returns a fresh snapshot of its settings.
- [associatedtype Container : HomeAccessorySettingsContainer](./container.md)
  The type of container that holds the provider’s settings.
- [associatedtype Context : HomeAccessorySettingsContext](./context.md)
  The type of context that the provider receives on each call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessorysettingsprovider/settingsdidchange(changes:context:for:))*