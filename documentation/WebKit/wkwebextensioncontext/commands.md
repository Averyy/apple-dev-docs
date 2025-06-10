# commands

**Framework**: WebKit  
**Kind**: property

The commands associated with the extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var commands: [WKWebExtension.Command] { get }
```

#### Discussion

Provides all commands registered within the extension. Each command represents an action or behavior available for the web extension.

## See Also

- [func performCommand(WKWebExtension.Command)](wkwebextensioncontext/performcommand(_:).md)
  Performs the specified command, triggering events specific to this extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/commands)*