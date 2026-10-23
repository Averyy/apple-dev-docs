# init(context:provider:filter:)

**Framework**: HomeExtensions  
**Kind**: init  
**Role**: Initializer

Creates accessory settings backed by a provider.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@MainActor
init<Provider>(context: @escaping () -> Provider.Context, provider: @escaping () -> Provider, filter: @escaping HomeAccessoryConfiguration.SupportsAccessory = { _ in true }) where Provider : HomeAccessorySettingsProvider
```

## Parameters

- `context`: A closure that creates the context passed to your provider.
- `provider`: A closure that creates your settings provider.
- `filter`: A closure that returns `true` for each accessory that the settings apply to. The framework doesn’t call your provider for other accessories. By default, the settings apply to all accessories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessorysettings/init(context:provider:filter:))*