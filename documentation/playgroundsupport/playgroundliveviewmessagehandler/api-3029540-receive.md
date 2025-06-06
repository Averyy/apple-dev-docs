# receive(_:)

**Framework**: Playground Support  
**Kind**: intfm  
**Required**: Yes

Allows the handler to receive a live view message from a remote object.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
func receive(_ message: PlaygroundValue)
```

#### Discussion

The example below implements this method to receive a dictionary with a command from a remote object.

```swift
func receive(_ message: PlaygroundValue) {
       guard case let .dictionary(dict) = message else { return }
       guard case let .string(commandName)? = dict["command"] else { return }

       // Use commandName to perform the specified command.
}
```

## Parameters

- `message`: A message sent to a live view from a remote object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundsupport/playgroundliveviewmessagehandler/3029540-receive)*