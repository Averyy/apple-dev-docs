# performCommand(for:)

**Framework**: WebKit  
**Kind**: method

Performs the command associated with the given event.

**Availability**:
- macOS 15.4+

## Declaration

```swift
@MainActor
func performCommand(for event: NSEvent) -> Bool
```

#### Return Value

Returns `YES` if a command corresponding to the event was found and performed, `NO` otherwise.

#### Discussion

This method checks for a command corresponding to the provided event and performs it, if available. The app should use this method to perform any extension commands at an appropriate time in the app’s event handling, like in [`sendEvent(_:)`](https://developer.apple.com/documentation/AppKit/NSApplication/sendEvent(_:)) of  [`NSApplication`](https://developer.apple.com/documentation/AppKit/NSApplication) or  [`sendEvent(_:)`](https://developer.apple.com/documentation/AppKit/NSWindow/sendEvent(_:)) of  [`NSWindow`](https://developer.apple.com/documentation/AppKit/NSWindow) subclasses.

## Parameters

- `event`: The event representing the user input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/performcommand(for:)-8btj0)*