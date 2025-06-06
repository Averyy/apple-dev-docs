# commandDefinitions

**Framework**: Xcodekit  
**Kind**: property

The array of command definitions used by Xcode to associate command names with their implementation in an extension.

**Availability**:
- macOS 10.12+

## Declaration

```swift
optional var commandDefinitions: [[XCSourceEditorCommandDefinitionKey : Any]] { get }
```

#### Discussion

Implement this property when you need to override the command definitions specified in your extension target’s Info.plist file. There are no guarantees about the thread or queue on which this property is accessed.

## See Also

- [struct XCSourceEditorCommandDefinitionKey](xcsourceeditorcommanddefinitionkey.md)
  A key in the dictionary that defines a source editor command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcodekit/xcsourceeditorextension/commanddefinitions)*