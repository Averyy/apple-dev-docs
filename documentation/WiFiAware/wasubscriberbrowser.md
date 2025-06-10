# WASubscriberBrowser

**Framework**: Wi-Fi Aware  
**Kind**: struct

The structure that configures a network browser to subscribe to a Wi-Fi Aware service and make outgoing connections to paired devices.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
struct WASubscriberBrowser
```

#### Overview

Devices can subscribe to services provided by other Wi-Fi Aware devices by creating a `NetworkBrowser` object from the [`Network`](https://developer.apple.comhttps://developer.apple.com/documentation/Network) framework, and passing in a `.wifiAware()` instruction indicating the `WASubscribableService` to look for, and the set of `WAPairedDevice` to find it on.

The code below configures the `NetworkBrowser` as a Wi-Fi Aware subscriber by passing in a `.wifiAware()` instruction:

```swift
NetworkBrowser(for: .wifiAware( .connecting(to:.selected(devices),  from:service) ) )
```

## Topics

### Configuring a browser
- [WASubscriberBrowser.Action](wasubscriberbrowser/action.md)
  The structure that configures the Wi-Fi Aware subscriber operation the network browser performs.
- [WASubscriberBrowser.Devices](wasubscriberbrowser/devices.md)
  The structure that determines the devices to connect to.
### Processing Wi-Fi Aware subscribe results
- [WASubscriberBrowser.Endpoint](wasubscriberbrowser/endpoint.md)
  A result for each discovered Wi-Fi Aware device.
### Creating browser implementation details
- [func makeDescriptor() -> NWBrowser.Descriptor](wasubscriberbrowser/makedescriptor.md)
  Makes a descriptor that can create a network browser for a Wi-Fi Aware subscribe operation.
- [func configureParameters(NWParameters?) -> NWParameters](wasubscriberbrowser/configureparameters(_:).md)
  Returns the parameters to use to configure the Wi-Fi Aware subscriber and the subsequent connection.
- [func makeEndpoint(from: NWBrowser.Result) throws -> WASubscriberBrowser.Endpoint?](wasubscriberbrowser/makeendpoint(from:).md)
  Creates a connectable Wi-Fi Aware endpoint from a browse result.
### Default Implementations
- [BrowserProvider Implementations](wasubscriberbrowser/browserprovider-implementations.md)

## Relationships

### Conforms To
- [BrowserProvider](../Network/BrowserProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [WASubscriberBrowser.Action](wasubscriberbrowser/action.md)
  The structure that configures the Wi-Fi Aware subscriber operation the network browser performs.
- [WASubscriberBrowser.Devices](wasubscriberbrowser/devices.md)
  The structure that determines the devices to connect to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wasubscriberbrowser)*