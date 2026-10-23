# Context

**Framework**: HomeExtensions  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

The type of context that the provider receives on each call.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
associatedtype Context : HomeAccessorySettingsContext
```

## See Also

### Accessing the settings
- [func settings(context: Self.Context, for: HMAccessory) async throws -> Self.Container](./settings%28context,for%29.md)
  Reads the accessory and returns a fresh snapshot of its settings.
- [func settingsDidChange(changes: [String : Any], context: Self.Context, for: HMAccessory) async throws](./settingsdidchange%28changes,context,for%29.md)
  Tells the provider that a person changed settings in the Home app.
- [associatedtype Container : HomeAccessorySettingsContainer](./container.md)
  The type of container that holds the provider’s settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessorysettingsprovider/context)*