# init(service:targetQueue:options:incomingSessionHandler:)

**Framework**: Xpc  
**Kind**: init

Creates the server side of an XPC service using the specified service name.

**Availability**:
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
init(service: String, targetQueue: DispatchQueue? = nil, options: XPCListener.InitializationOptions = .none, incomingSessionHandler: @escaping (XPCListener.IncomingSessionRequest) -> XPCListener.IncomingSessionRequest.Decision) throws
```

#### Discussion

Listener creation fails if the XPC service isn’t found or is unavailable.

When a client connects to your service, the system invokes the `incomingSessionHandler` with a request that you must either accept or reject. To accept the incoming request, choose one of the following two approaches:

- For simple protocols, use [`accept(incomingMessageHandler:cancellationHandler:)`](xpclistener/incomingsessionrequest/accept(incomingmessagehandler:cancellationhandler:)-8rodk.md) or [`accept(incomingMessageHandler:cancellationHandler:)`](xpclistener/incomingsessionrequest/accept(incomingmessagehandler:cancellationhandler:)-48c3k.md) to provide a closure that receives the incoming message directly.
- For more complex protocols that delegate message handling to a different object, use `accept(_:)` to provide a closure that returns a [`XPCPeerHandler`](xpcpeerhandler.md). The peer handler object receives incoming messages from the client directly.

When the `incomingSessionHandler` returns, the system automatically activates the peer session unless you explicitly reject it or pass the [`inactive`](xpclistener/initializationoptions/inactive.md) initialzation option.

## Parameters

- `service`: The Mach service or XPC service name that clients use to connect to the service.
- `targetQueue`: The dispatch queue that events arrive on. This may be a concurrent queue. If  , the listeners uses  .
- `options`: Configuration options for the listener, such as creating it in an inactive state.
- `incomingSessionHandler`: A handler that the system calls when a client connects to the XPC service.

## See Also

- [XPCListener.InitializationOptions](xpclistener/initializationoptions.md)
  Options that control the listener’s configuration, such as if it’s inactive at creation.
- [XPCListener.IncomingSessionRequest](xpclistener/incomingsessionrequest.md)
  A session request from a client that you accept or reject.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpclistener/init(service:targetqueue:options:incomingsessionhandler:))*