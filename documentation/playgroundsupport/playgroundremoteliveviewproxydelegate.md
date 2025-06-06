# PlaygroundRemoteLiveViewProxyDelegate

**Framework**: Playground Support  
**Kind**: intf

A delegate you use to receive messages from the always-on live view.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
protocol PlaygroundRemoteLiveViewProxyDelegate : AnyObject
```

## Topics

### Receiving Messages
- [func remoteLiveViewProxy(PlaygroundRemoteLiveViewProxy, received: PlaygroundValue)](playgroundremoteliveviewproxydelegate/3029572-remoteliveviewproxy.md)
  Tells the delegate that a message was received from the always-on live view.
### Handling Connection Changes
- [func remoteLiveViewProxyConnectionClosed(PlaygroundRemoteLiveViewProxy)](playgroundremoteliveviewproxydelegate/3029573-remoteliveviewproxyconnectionclo.md)
  Tells the delegate that it has disconnected from the always-on live view.

## See Also

- [Messaging Between a Playground Page and the Always-On Live View](messaging_between_a_playground_page_and_the_always-on_live_view.md)
  Display the results of running a playground page's code in a persistent live view.
- [class PlaygroundRemoteLiveViewProxy](playgroundremoteliveviewproxy.md)
  A proxy that facilitates message passing between the always-on live view and its corresponding playground page.
- [protocol PlaygroundLiveViewMessageHandler](playgroundliveviewmessagehandler.md)
  A handler you use to send and receive messages between the always-on live view and its corresponding playground page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundsupport/playgroundremoteliveviewproxydelegate)*