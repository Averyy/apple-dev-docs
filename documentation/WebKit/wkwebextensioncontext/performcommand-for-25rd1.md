# performCommand(for:)

**Framework**: WebKit  
**Kind**: method

Performs the command associated with the given key command.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func performCommand(for keyCommand: UIKeyCommand) -> Bool
```

#### Return Value

Returns `YES` if a command corresponding to the UIKeyCommand was found and performed, `NO` otherwise.

#### Discussion

This method checks for a command corresponding to the provided [`UIKeyCommand`](https://developer.apple.com/documentation/UIKit/UIKeyCommand) and performs it, if available. The app should use this method to perform any extension commands at an appropriate time in the app’s responder object that handles the [`performCommand(for:)`](wkwebextensioncontext/performcommand(for:)-25rd1.md) action.

## Parameters

- `keyCommand`: The key command received by the first responder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/performcommand(for:)-25rd1)*