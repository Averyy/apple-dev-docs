# WASubscriberBrowser.Devices

**Framework**: Wi-Fi Aware  
**Kind**: struct

The structure that determines the devices to connect to.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
struct Devices
```

#### Overview

This structure determines the devices the `NetworkBrowser` acts on when subscribing, such as which devices to try to connect to. It allows your app to include only the devices that are relevant for a given `NetworkBrowser` operation and use case.

`Devices` is the `to:` component of the `.wifiAware()` instruction to a `NetworkBrowser`.

The code below is an example of configuring a `NetworkBrowser` with specific devices to connect to:

```swift
NetworkBrowser(for: .wifiAware( .connecting(to:.selected(devices),  from:service) ) )
```

> ❗ **Important**:  Only include the devices your app intends to use with the use case. Including unnecessary devices may impose additional power and performance costs on both the local and remote devices, and may reduce privacy.

## Topics

### Selecting devices to connect to
- [static func selected(WAPairedDevice.Devices) -> WASubscriberBrowser.Devices](wasubscriberbrowser/devices/selected(_:)-8myz8.md)
  Includes only the preselected paired devices in the provided dictionary.
- [static func selected(some Sequence<WAPairedDevice>) -> WASubscriberBrowser.Devices](wasubscriberbrowser/devices/selected(_:)-5arv0.md)
  Includes only the preselected paired devices in the provided list.
### Using a live matching filter
- [static func matching(Predicate<WAPairedDevice>) -> WASubscriberBrowser.Devices](wasubscriberbrowser/devices/matching(_:).md)
  Includes only paired devices matching the provided live filter predicate.
### Connecting to all paired devices
- [static let allPairedDevices: WASubscriberBrowser.Devices](wasubscriberbrowser/devices/allpaireddevices.md)
  The property that includes all paired devices that your app has access to.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct WASubscriberBrowser](wasubscriberbrowser.md)
  The structure that configures a network browser to subscribe to a Wi-Fi Aware service and make outgoing connections to paired devices.
- [WASubscriberBrowser.Action](wasubscriberbrowser/action.md)
  The structure that configures the Wi-Fi Aware subscriber operation the network browser performs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wasubscriberbrowser/devices)*