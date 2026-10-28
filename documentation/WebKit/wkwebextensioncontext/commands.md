# commands

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The commands associated with the extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
var commands: [WKWebExtension.Command] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<WKWebExtensionCommand *> * commands;
```

## Discussion

Provides all commands registered within the extension. Each command represents an action or behavior available for the web extension.

## See Also

### Related Documentation
- [func performCommand(WKWebExtension.Command)](./performcommand%28_%29.md)
  Performs the specified command, triggering events specific to this extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/commands)*