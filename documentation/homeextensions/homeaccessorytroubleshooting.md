# HomeAccessoryTroubleshooting

**Framework**: HomeExtensions  
**Kind**: struct  
**Role**: Structure

Content that helps people resolve problems with an accessory.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@MainActor
struct HomeAccessoryTroubleshooting
```

## Topics

### Creating troubleshooting content
- [init(content: () -> some View, filter: HomeAccessoryTroubleshooting.SupportsAccessory)](./homeaccessorytroubleshooting/init%28content,filter%29.md)
  Creates troubleshooting content with a view.
- [HomeAccessoryTroubleshooting.SupportsAccessory](./homeaccessorytroubleshooting/supportsaccessory.md)
  A closure that determines whether troubleshooting content applies to an accessory.
### Adding manufacturer support
- [func contactAccessoryManufacturerLink() -> HomeAccessoryTroubleshooting](./homeaccessorytroubleshooting/contactaccessorymanufacturerlink%28%29.md)
  Adds a manufacturer contact button to the troubleshooting view.

## Relationships

### Conforms To
- [HomeContent](./homecontent.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Guides and troubleshooting content
- [protocol HomeContent](./homecontent.md)
  A type that represents content that your extension provides to the Home app.
- [struct HomeContentID](./homecontentid.md)
  An identifier for a piece of content that your extension provides.
- [struct HomeAccessoryHelpGuide](./homeaccessoryhelpguide.md)
  Help content about a specific topic for an accessory.
- [class GuideStepHostViewController](./guidestephostviewcontroller.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessorytroubleshooting)*