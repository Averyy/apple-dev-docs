# Messaging Between a Playground Page and the Always-On Live View

**Framework**: Playground Support

Display the results of running a playground page's code in a persistent live view.

#### Overview

The always-on live view in Swift Playgrounds runs continuously as learners write and debug the code in the accompanying playground page. Because the code in the playground page may change continuously, the code you write for the always-on live view runs in a separate process so it isn't continuously restarting.

Instances in a playground page can't communicate directly with instances in the always-on live view. Instead, you communicate asynchronously between the two parts of a playground by adopting a message-handling protocol and setting a delegate for a proxy object that mediates between the two processes.

##### 3034527

You create the always-on live view by assigning a view or view controller to the global [`liveView`](playgroundpage/1964506-liveview.md) for the current page.

> ❗ **Important**: You invoke the always-on live view from a file named `LiveView.swift`, which must be located in the directory for each playground page. If you assign the current [`liveView`](playgroundpage/1964506-liveview.md) from any other code, the resulting live view will be a traditional live view that doesn't persist across multiple runs of the page.

Configure your always-on live view to adopt the [`PlaygroundLiveViewMessageHandler`](playgroundliveviewmessagehandler.md) protocol for sending and receiving messages from the corresponding playground page. The example below uses a [`UIButton`](https://developer.apple.com/documentation/uikit/uibutton) as the root view and changes the background color of the button when it receives a message. 

```swift
extension UIButton: PlaygroundLiveViewMessageHandler {
    public func receive(_ message: PlaygroundValue) {
        // Change the appearance of the view when a message is received.
        self.backgroundColor = .yellow
    }
}

var button = UIButton()
button.backgroundColor = .purple
button.setTitle("Always-on live view", for: .normal)

PlaygroundPage.current.liveView = button
```

##### 3034523

The always-on live view that you configure in `LiveView.swift` is visible to learner-facing code—code invoked from `main.swift`—as an instance of [`PlaygroundRemoteLiveViewProxy`](playgroundremoteliveviewproxy.md). To receive messages from the always-on live view, you define a class to be that proxy's delegate.

The example below defines a delegate for the always-on live view proxy and configures it to print any messages it receives.

```swift
class MessageHandler: PlaygroundRemoteLiveViewProxyDelegate {
    func remoteLiveViewProxy(
        _ remoteLiveViewProxy: PlaygroundRemoteLiveViewProxy,
        received message: PlaygroundValue
    ) {
        print("Received a message from the always-on live view", message)
    }

    func remoteLiveViewProxyConnectionClosed(_ remoteLiveViewProxy: PlaygroundRemoteLiveViewProxy) {}
}

guard let remoteView = PlaygroundPage.current.liveView as? PlaygroundRemoteLiveViewProxy else {
    fatalError("Always-on live view not configured in this page's LiveView.swift.")
}

remoteView.delegate = MessageHandler()
```

##### 3034522

You send messages to the always-on live view by calling the [`send(_:)`](playgroundremoteliveviewproxy/3029570-send.md) method on its proxy.

```swift
remoteView.send(.string("Hey"))
```

You send messages back to the playground page from the always-on live view by calling the [`send(_:)`](playgroundliveviewmessagehandler/3029542-send.md) method on the view itself.

The example below builds on the example in [`Configure the Always-On Live View`](messaging_between_a_playground_page_and_the_always-on_live_view#3034527.md) by sending a message back to the playground page in response to any messages the always-on live view receives.

```swift
extension UIButton: PlaygroundLiveViewMessageHandler {
    public func receive(_ message: PlaygroundValue) {
        // Change the appearance of the view when a message is received.
        self.backgroundColor = .yellow

        // Send a message in response.
        self.send(.string("Greetings from the always-on live view."))
    }
}
```

## See Also

- [class PlaygroundRemoteLiveViewProxy](playgroundremoteliveviewproxy.md)
  A proxy that facilitates message passing between the always-on live view and its corresponding playground page.
- [protocol PlaygroundRemoteLiveViewProxyDelegate](playgroundremoteliveviewproxydelegate.md)
  A delegate you use to receive messages from the always-on live view.
- [protocol PlaygroundLiveViewMessageHandler](playgroundliveviewmessagehandler.md)
  A handler you use to send and receive messages between the always-on live view and its corresponding playground page.
- [class PlaygroundPage](playgroundpage.md)
  An object you use to configure the state of a playground page and its live view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundsupport/messaging_between_a_playground_page_and_the_always-on_live_view)*