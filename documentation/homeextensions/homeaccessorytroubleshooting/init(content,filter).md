# init(content:filter:)

**Framework**: HomeExtensions  
**Kind**: init  
**Role**: Initializer

Creates troubleshooting content with a view.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@MainActor
init(@ContentBuilder content: @escaping () -> some View, filter: @escaping HomeAccessoryTroubleshooting.SupportsAccessory = { _ in true })
```

## Parameters

- `content`: A view builder that creates the troubleshooting view.
- `filter`: A closure that returns `true` for each accessory that the content applies to. By default, the content applies to all accessories.

## See Also

### Creating troubleshooting content
- [HomeAccessoryTroubleshooting.SupportsAccessory](./supportsaccessory.md)
  A closure that determines whether troubleshooting content applies to an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessorytroubleshooting/init(content:filter:))*