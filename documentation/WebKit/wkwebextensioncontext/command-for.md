# command(for:)

**Framework**: Webkit  
**Kind**: method

Retrieves the command associated with the given event without performing it.

**Availability**:
- macOS 15.4+

## Declaration

```swift
@MainActor
func command(for event: NSEvent) -> WKWebExtension.Command?
```

#### Return Value

The command associated with the event, or `nil` if there is no such command.

#### Discussion

Returns the command that corresponds to the provided event, if such a command exists. This provides a way to programmatically determine what action would occur for a given event, without triggering the command.

## Parameters

- `event`: The event for which to retrieve the corresponding command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/command(for:))*