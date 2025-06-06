# PlaygroundLiveViewMessageHandler

**Framework**: Playground Support  
**Kind**: intf

A handler you use to send and receive messages between the always-on live view and its corresponding playground page.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
protocol PlaygroundLiveViewMessageHandler : AnyObject
```

## Topics

### Sending Messages
- [func send(PlaygroundValue)](playgroundliveviewmessagehandler/3029542-send.md)
  Allows the handler to send a message to a remote object.
### Receiving Messages
- [func receive(PlaygroundValue)](playgroundliveviewmessagehandler/3029540-receive.md)
  Allows the handler to receive a live view message from a remote object.
### Handling Connection Changes
- [func liveViewMessageConnectionOpened()](playgroundliveviewmessagehandler/3029538-liveviewmessageconnectionopened.md)
  Informs the handler that it has connected to a remote object.
- [func liveViewMessageConnectionClosed()](playgroundliveviewmessagehandler/3029536-liveviewmessageconnectionclosed.md)
  Informs the handler that the connection between the proxy and the remote object was closed.

## Relationships

### Conforming Types
- [PlaygroundRemoteLiveViewProxy](playgroundremoteliveviewproxy.md)

## See Also

- [Messaging Between a Playground Page and the Always-On Live View](messaging_between_a_playground_page_and_the_always-on_live_view.md)
  Display the results of running a playground page's code in a persistent live view.
- [class PlaygroundRemoteLiveViewProxy](playgroundremoteliveviewproxy.md)
  A proxy that facilitates message passing between the always-on live view and its corresponding playground page.
- [protocol PlaygroundRemoteLiveViewProxyDelegate](playgroundremoteliveviewproxydelegate.md)
  A delegate you use to receive messages from the always-on live view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundsupport/playgroundliveviewmessagehandler)*