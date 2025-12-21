# WAPublisherListener.Action

**Framework**: Wi-Fi Aware  
**Kind**: struct

The structure that configures the Wi-Fi Aware publisher operation that the network listener performs.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
struct Action
```

#### Overview

The configuration includes the service and devices it operates on.

The [`WAPublisherListener.Action`](wapublisherlistener/action.md) is the first component of the `.wifiAware()` instruction to a `NetworkListener`.

The code below is an example of creating a `NetworkListener`:

```swift
NetworkListener(for: .wifiAware( .connecting(to:service,  from:.selected(devices)) ) )
```

## Topics

### Creating a listener
- [static func connecting(to: WAPublishableService, from: WAPublisherListener.Devices, datapath: WAPublisherListener.DatapathParameters?) -> WAPublisherListener.Action](wapublisherlistener/action/connecting(to:from:datapath:).md)
  Publishes the provided service over Wi-Fi, enabling connections from the specified paired devices.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct WAPublisherListener](wapublisherlistener.md)
  Configures a network listener to publish a service over Wi-Fi Aware and accept incoming connections from paired devices.
- [WAPublisherListener.Devices](wapublisherlistener/devices.md)
  The structure that determines the devices to connect to.
- [WAPublisherListener.DatapathParameters](wapublisherlistener/datapathparameters.md)
  The parameter that sets the initial Wi-Fi Aware data path configuration for any devices that are connected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapublisherlistener/action)*