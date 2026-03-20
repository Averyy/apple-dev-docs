# addingConnections(from:)

**Framework**: Wi-Fi Aware  
**Kind**: method

Makes additional network connections over a preexisting Wi-Fi Aware data path without publishing or advertising services over Wi-Fi Aware.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
static func addingConnections(from pairedDevices: WAPublisherListener.Devices) -> WAPublisherListener.Action
```

#### Return Value

A new `WAPublisherListener.Action` that configures the listener to accept network connections from specified paired devices.

#### Discussion

Set up your app’s first connection to a device using Wi-Fi Aware service discovery. Apps can do so by defining a single “control” service used for initial discovery and connection, and creating a `NetworkListener` for that service via [`connecting(to:from:datapath:)`](WAPublisherListener/Action/connecting(to:from:datapath:).md). Subsequent connections may then use a `.addingConnections` `NetworkListener` to quickly connect without going through the service discovery process again.

The framework limits the listener to accepting connections from the paired devices specified.

> ❗ **Important**: Your app must have at least one pre-existing [`NetworkConnection`](https://developer.apple.com/documentation/Network/NetworkConnection) to a remote device before it can make additional connections to an `.addingConnections NetworkListener` on that device.

```swift
// Create a listener to add new connections.
let listener = try NetworkListener(for:
            .wifiAware(.addingConnections(from: .matching(devices))),
        using: .parameters({
             TCP()
}))

// Get the port number once the listener is in the ready state.
guard let port = listener.port { return }

// Send the port number to the client device or devices over the control connection.
```

## Parameters

- `pairedDevices`: The remote devices from which to accept connections. The `NetworkListener` isn’t activated if the system doesn’t specify any devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapublisherlistener/action/addingconnections(from:))*