# XCSourceEditorExtension

**Framework**: Xcodekit  
**Kind**: protocol

The protocol you implement to create Xcode source editor extensions.

**Availability**:
- macOS 10.12+

## Declaration

```swift
protocol XCSourceEditorExtension : NSObjectProtocol
```

#### Overview

There are no guarantees about the thread or queue on which any Xcode Source Editor Extension methods are executed, including the designated initializer.

## Topics

### Defining Extension Commands
- [var commandDefinitions: [[XCSourceEditorCommandDefinitionKey : Any]]](xcsourceeditorextension/commanddefinitions.md)
  The array of command definitions used by Xcode to associate command names with their implementation in an extension.
### Handling Extension Launches
- [func extensionDidFinishLaunching()](xcsourceeditorextension/extensiondidfinishlaunching.md)
  Tells the extension that it successfully launched and may begin to receive editor commands.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Creating a Source Editor Extension](creating-a-source-editor-extension.md)
  Add and configure a source editor extension in your Xcode project.
- [Testing Your Source Editor Extension](testing-your-source-editor-extension.md)
  Launch a special instance of Xcode to test your source editor extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcodekit/xcsourceeditorextension)*