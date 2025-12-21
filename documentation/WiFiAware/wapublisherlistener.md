# WAPublisherListener

**Framework**: Wi-Fi Aware  
**Kind**: struct

Configures a network listener to publish a service over Wi-Fi Aware and accept incoming connections from paired devices.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
struct WAPublisherListener
```

#### Overview

Devices can publish services for other Wi-Fi Aware devices to use by creating a `NetworkListener` object from the [`Network`](https://developer.apple.comhttps://developer.apple.com/documentation/Network) framework, and passing in a `.wifiAware()` instruction indicating the `WAPublishableService` to provide, and the set of `WAPairedDevice` that can connect to the service. The code below configures the `NetworkListener` as a Wi-Fi Aware publisher by passing in a `.wifiAware()` instruction:

```swift
NetworkListener(for: .wifiAware( .connecting(to:service,  from:.selected(devices)) ) )
```

## Topics

### Configuring a listener
- [WAPublisherListener.Action](wapublisherlistener/action.md)
  The structure that configures the Wi-Fi Aware publisher operation that the network listener performs.
- [WAPublisherListener.Devices](wapublisherlistener/devices.md)
  The structure that determines the devices to connect to.
- [WAPublisherListener.DatapathParameters](wapublisherlistener/datapathparameters.md)
  The parameter that sets the initial Wi-Fi Aware data path configuration for any devices that are connected.
### Creating publisher implementation details
- [func configureParameters(NWParameters)](wapublisherlistener/configureparameters(_:).md)
  Configures the provided parameters for a Wi-Fi Aware publish operation and connection.
- [var service: NWListener.Service](wapublisherlistener/service.md)
  The service data for the Wi-Fi Aware publish operation.
- [var isApplicationService: Bool](wapublisherlistener/isapplicationservice.md)
  A Boolean value that determines whether the devices are listening for an application service.

## Relationships

### Conforms To
- [ListenerProvider](../Network/ListenerProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [WAPublisherListener.Action](wapublisherlistener/action.md)
  The structure that configures the Wi-Fi Aware publisher operation that the network listener performs.
- [WAPublisherListener.Devices](wapublisherlistener/devices.md)
  The structure that determines the devices to connect to.
- [WAPublisherListener.DatapathParameters](wapublisherlistener/datapathparameters.md)
  The parameter that sets the initial Wi-Fi Aware data path configuration for any devices that are connected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapublisherlistener)*