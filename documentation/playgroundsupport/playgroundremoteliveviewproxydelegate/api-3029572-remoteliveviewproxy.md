# remoteLiveViewProxy(_:received:)

**Framework**: Playground Support  
**Kind**: intfm  
**Required**: Yes

Tells the delegate that a message was received from the always-on live view.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
func remoteLiveViewProxy(_ remoteLiveViewProxy: PlaygroundRemoteLiveViewProxy, received message: PlaygroundValue)
```

## Parameters

- `remoteLiveViewProxy`: The local proxy for the remote always-on live view.
- `message`: A message sent to the playground page from the always-on live view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundsupport/playgroundremoteliveviewproxydelegate/3029572-remoteliveviewproxy)*