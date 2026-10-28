# performCommand(for:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Performs the command associated with the given event.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func performCommand(for event: NSEvent) -> Bool
```

```objc
- (BOOL) performCommandForEvent:(NSEvent *) event;
```

## Return Value

Returns `YES` if a command corresponding to the event was found and performed, `NO` otherwise.

## Discussion

This method checks for a command corresponding to the provided event and performs it, if available. The app should use this method to perform any extension commands at an appropriate time in the app’s event handling, like in [`sendEvent(_:)`](../../AppKit/nsapplication/sendevent%28_%29.md) of  [`NSApplication`](../../AppKit/nsapplication.md) or  [`sendEvent(_:)`](../../AppKit/nswindow/sendevent%28_%29.md) of  [`NSWindow`](../../AppKit/nswindow.md) subclasses.

## Parameters

- `event`: The event representing the user input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/performcommand(for:)-8btj0)*