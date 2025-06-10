# XCSourceEditorCommandDefinitionKey

**Framework**: XcodeKit  
**Kind**: struct

A key in the dictionary that defines a source editor command.

**Availability**:
- macOS 10.12+

## Declaration

```swift
struct XCSourceEditorCommandDefinitionKey
```

## Mentions

- [Creating a Source Editor Extension](creating-a-source-editor-extension.md)

#### Overview

Source editor commands are defined via an array of dictionaries under the `XCSourceEditorCommandDefinitions` key of a Xcode Source Editor Extension’s `NSExtensionAttributes` within its `Info.plist` file. Commands can also be specified via the [`commandDefinitions`](xcsourceeditorextension/commanddefinitions.md) property in an extension’s conformance to the [`XCSourceEditorExtension`](xcsourceeditorextension.md) protocol.

## Topics

### Populating a Command Definition Dictionary
- [static let classNameKey: XCSourceEditorCommandDefinitionKey](xcsourceeditorcommanddefinitionkey/classnamekey.md)
  The class of the source editor command, in its attributes.
- [static let identifierKey: XCSourceEditorCommandDefinitionKey](xcsourceeditorcommanddefinitionkey/identifierkey.md)
  The identifier of the source editor command in its attributes.
- [static let nameKey: XCSourceEditorCommandDefinitionKey](xcsourceeditorcommanddefinitionkey/namekey.md)
  The name of the source editor command in its attributes.
### Creating a Key Using a Raw String
- [init(rawValue: String)](xcsourceeditorcommanddefinitionkey/init(rawvalue:).md)
  Creates the key for a source-editor command by using the string value you specify.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcodekit/xcsourceeditorcommanddefinitionkey)*