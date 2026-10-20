# performCommand(for:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Performs the command associated with the given key command.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- visionOS 2.4+

## Declaration

```swift
func performCommand(for keyCommand: UIKeyCommand) -> Bool
```

```objc
- (BOOL) performCommandForKeyCommand:(UIKeyCommand *) keyCommand;
```

#### Return Value

Returns `YES` if a command corresponding to the UIKeyCommand was found and performed, `NO` otherwise.

#### Discussion

This method checks for a command corresponding to the provided [`UIKeyCommand`](../../UIKit/uikeycommand.md) and performs it, if available. The app should use this method to perform any extension commands at an appropriate time in the app’s responder object that handles the [`performCommand(for:)`](./performcommand%28for%29-25rd1.md) action.

## Parameters

- `keyCommand`: The key command received by the first responder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/performcommand(for:)-25rd1)*