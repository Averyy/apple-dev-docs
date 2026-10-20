# XCSourceEditorCommand

**Framework**: XcodeKit  
**Kind**: protocol  
**Role**: Protocol

The protocol you implement to handle command invocations in a source editor extension.

**Availability**:
- macOS 10.12+

## Declaration

```swift
protocol XCSourceEditorCommand : NSObjectProtocol
```

```objc
@protocol XCSourceEditorCommand <NSObject>
```

## Mentions

- [Creating a Source Editor Extension](./creating-a-source-editor-extension.md)

#### Overview

A one-to-one mapping between command classes and commands is not required—multiple commands can be handled by a single class, by checking their invocation’s `commandIdentifier` at runtime.

## Topics

### Defining Editor Commands
- [struct XCSourceEditorCommandDefinitionKey](./xcsourceeditorcommanddefinitionkey.md)
  A key in the dictionary that defines a source editor command.
### Handling Editor Commands
- [func perform(with: XCSourceEditorCommandInvocation, completionHandler: ((any Error)?) -> Void)](./xcsourceeditorcommand/perform%28with,completionhandler%29.md)
  Performs the action associated with the command using the information in an invocation.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Editor Commands
- [class XCSourceEditorCommandInvocation](./xcsourceeditorcommandinvocation.md)
  An object that identifies the command issued to your extension and provides the contents of the active source editor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcodekit/xcsourceeditorcommand)*