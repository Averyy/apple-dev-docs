# WAPublisherListener.Action

**Framework**: Wi-Fi Aware  
**Kind**: struct  
**Role**: Structure

The structure that configures the Wi-Fi Aware publisher operation that the network listener performs.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct Action
```

## Overview

The configuration includes the service and devices it operates on.

The [`WAPublisherListener.Action`](./action.md) is the first component of the `.wifiAware()` instruction to a `NetworkListener`.

The code below is an example of creating a `NetworkListener`:

```swift
NetworkListener(for: .wifiAware( .connecting(to:service,  from:.selected(devices)) ) )
```

## Topics

### Creating a listener
- [static func connecting(to: WAPublishableService, from: WAPublisherListener.Devices, datapath: WAPublisherListener.DatapathParameters?) -> WAPublisherListener.Action](./action/connecting%28to,from,datapath%29.md)
  Publishes the provided service over Wi-Fi, enabling connections from the specified paired devices.
### Type Methods
- [static func addingConnections(from: WAPublisherListener.Devices) -> WAPublisherListener.Action](./action/addingconnections%28from%29.md)
  Makes additional network connections over a preexisting Wi-Fi Aware data path without publishing or advertising services over Wi-Fi Aware.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Publisher
- [struct WAPublisherListener](../wapublisherlistener.md)
  Configures a network listener to publish a service over Wi-Fi Aware and accept incoming connections from paired devices.
- [WAPublisherListener.Devices](./devices.md)
  The structure that determines the devices to connect to.
- [WAPublisherListener.DatapathParameters](./datapathparameters.md)
  The parameter that sets the initial Wi-Fi Aware data path configuration for any devices that are connected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapublisherlistener/action)*