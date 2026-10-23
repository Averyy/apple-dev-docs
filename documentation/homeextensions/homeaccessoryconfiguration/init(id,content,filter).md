# init(id:content:filter:)

**Framework**: HomeExtensions  
**Kind**: init  
**Role**: Initializer

Creates a configuration with an identifier and a view.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@MainActor
init(id: HomeContentID, @ContentBuilder content: @escaping () -> some View, filter: @escaping HomeAccessoryConfiguration.SupportsAccessory = { _ in true })
```

## Parameters

- `id`: The configuration’s identifier.
- `content`: A view builder that creates the configuration view.
- `filter`: A closure that returns `true` for each accessory that the configuration applies to. By default, the configuration applies to all accessories.

## See Also

### Creating an accessory configuration
- [HomeAccessoryConfiguration.SupportsAccessory](./supportsaccessory.md)
  A closure that determines whether content applies to an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessoryconfiguration/init(id:content:filter:))*