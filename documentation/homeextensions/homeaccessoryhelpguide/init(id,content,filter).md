# init(id:content:filter:)

**Framework**: HomeExtensions  
**Kind**: init  
**Role**: Initializer

Creates a help guide with an identifier and a view.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@MainActor
init(id: HomeContentID, @ContentBuilder content: @escaping () -> some View, filter: @escaping HomeAccessoryHelpGuide.SupportsAccessory = { _ in true })
```

## Parameters

- `id`: The help guide’s identifier.
- `content`: A view builder that creates the help guide view.
- `filter`: A closure that returns `true` for each accessory that the help guide applies to. By default, the help guide applies to all accessories.

## See Also

### Creating a help guide
- [HomeAccessoryHelpGuide.SupportsAccessory](./supportsaccessory.md)
  A closure that determines whether a help guide applies to an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessoryhelpguide/init(id:content:filter:))*