# XCSourceEditorCommandInvocation

**Framework**: XcodeKit  
**Kind**: class  
**Role**: Class

An object that identifies the command issued to your extension and provides the contents of the active source editor.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class XCSourceEditorCommandInvocation
```

```objc
@interface XCSourceEditorCommandInvocation : NSObject
```

## Topics

### Responding to Commands
- [var buffer: XCSourceTextBuffer](./xcsourceeditorcommandinvocation/buffer.md)
  The buffer of source text upon which the command can operate.
- [var commandIdentifier: String](./xcsourceeditorcommandinvocation/commandidentifier.md)
  The identifier of the command that the user invoked.
### Responding to Cancelled Commands
- [var cancellationHandler: () -> Void](./xcsourceeditorcommandinvocation/cancellationhandler.md)
  A handler to be invoked by Xcode to indicate that the invocation has been canceled by the user.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Editor Commands
- [protocol XCSourceEditorCommand](./xcsourceeditorcommand.md)
  The protocol you implement to handle command invocations in a source editor extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcodekit/xcsourceeditorcommandinvocation)*