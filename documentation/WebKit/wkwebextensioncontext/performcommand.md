# performCommand(_:)

**Framework**: WebKit  
**Kind**: method

Performs the specified command, triggering events specific to this extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func performCommand(_ command: WKWebExtension.Command)
```

#### Discussion

This method performs the given command as if it was triggered by a user gesture within the context of the focused window and active tab.

## Parameters

- `command`: The command to be performed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/performcommand(_:))*