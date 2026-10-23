# HomeAccessoryHelpGuide

**Framework**: HomeExtensions  
**Kind**: struct  
**Role**: Structure

Help content about a specific topic for an accessory.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@MainActor
struct HomeAccessoryHelpGuide
```

## Topics

### Creating a help guide
- [init(id: HomeContentID, content: () -> some View, filter: HomeAccessoryHelpGuide.SupportsAccessory)](./homeaccessoryhelpguide/init%28id,content,filter%29.md)
  Creates a help guide with an identifier and a view.
- [HomeAccessoryHelpGuide.SupportsAccessory](./homeaccessoryhelpguide/supportsaccessory.md)
  A closure that determines whether a help guide applies to an accessory.
### Adding a support link
- [func contactAccessoryManufacturerLink() -> HomeAccessoryHelpGuide](./homeaccessoryhelpguide/contactaccessorymanufacturerlink%28%29.md)
  Adds a button for contacting the accessory’s manufacturer.

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
- [struct HomeAccessoryTroubleshooting](./homeaccessorytroubleshooting.md)
  Content that helps people resolve problems with an accessory.
- [class GuideStepHostViewController](./guidestephostviewcontroller.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessoryhelpguide)*