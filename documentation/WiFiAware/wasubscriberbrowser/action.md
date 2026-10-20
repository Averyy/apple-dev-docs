# WASubscriberBrowser.Action

**Framework**: Wi-Fi Aware  
**Kind**: struct  
**Role**: Structure

The structure that configures the Wi-Fi Aware subscriber operation the network browser performs.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct Action
```

#### Overview

The configuration includes the service and devices it operates on.

The [`WASubscriberBrowser.Action`](./action.md) is the first component of the `.wifiAware()` instruction to a `NetworkBrowser`.

The code below is an example of creating a `NetworkBrowser`:

```swift
NetworkBrowser(for: .wifiAware( .connecting(to:.selected(devices),  from:service) ) )
```

## Topics

### Creating a browser
- [static func connecting(to: WASubscriberBrowser.Devices, from: WASubscribableService) -> WASubscriberBrowser.Action](./action/connecting%28to,from%29.md)
  Subscribes to the provided service over Wi-Fi, providing browse results for connecting to the specified paired devices if available.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Subscriber
- [struct WASubscriberBrowser](../wasubscriberbrowser.md)
  The structure that configures a network browser to subscribe to a Wi-Fi Aware service and make outgoing connections to paired devices.
- [WASubscriberBrowser.Devices](./devices.md)
  The structure that determines the devices to connect to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wasubscriberbrowser/action)*