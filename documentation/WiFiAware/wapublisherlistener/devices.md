# WAPublisherListener.Devices

**Framework**: Wi-Fi Aware  
**Kind**: struct

The structure that determines the devices to connect to.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
struct Devices
```

#### Overview

This structure determines the devices the `NetworkListener` acts on or allows connections from when publishing and includes only the devices that are relevant for a given `NetworkListener` operation and use case. It allows your app to include only the devices that are relevant for a given `NetworkListener` operation and use case.

`Devices` is the “`from:`” component of the `.wifiAware()` instruction to a `NetworkListener`.

The code below is an example of configuring a `NetworkListener` with specific devices to allow connections from:

```swift
NetworkListener(for: .wifiAware( .connecting(to:service,  from:.selected(devices)) ) )
```

> ❗ **Important**: Only include the devices your app intends to use with the use case. Including unnecessary devices may impose additional power and performance costs on both the local and remote devices, and may reduce privacy.

## Topics

### Selecting specific devices
- [static func selected(WAPairedDevice.Devices) -> WAPublisherListener.Devices](wapublisherlistener/devices/selected(_:)-56vig.md)
  Includes only the preselected paired devices in the provided dictionary.
- [static func selected(some Sequence<WAPairedDevice>) -> WAPublisherListener.Devices](wapublisherlistener/devices/selected(_:)-1e2.md)
  Includes only the preselected paired devices in the provided list.
- [static let userSpecifiedDevices: WAPublisherListener.Devices](wapublisherlistener/devices/userspecifieddevices.md)
  Includes only new devices the user pairs via DeviceDiscoveryUI’s `DevicePairingView()`.
### Using a live matching filter
- [static func matching(Predicate<WAPairedDevice>) -> WAPublisherListener.Devices](wapublisherlistener/devices/matching(_:).md)
  Includes only paired devices matching the provided live filter predicate.
### Allowing your paired devices to connect
- [static let allPairedDevices: WAPublisherListener.Devices](wapublisherlistener/devices/allpaireddevices.md)
  The property that includes all paired devices that your app has access to.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct WAPublisherListener](wapublisherlistener.md)
  Configures a network listener to publish a service over Wi-Fi Aware and accept incoming connections from paired devices.
- [WAPublisherListener.Action](wapublisherlistener/action.md)
  The structure that configures the Wi-Fi Aware publisher operation that the network listener performs.
- [WAPublisherListener.DatapathParameters](wapublisherlistener/datapathparameters.md)
  The parameter that sets the initial Wi-Fi Aware data path configuration for any devices that are connected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapublisherlistener/devices)*