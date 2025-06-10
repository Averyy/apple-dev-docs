# connecting(to:from:)

**Framework**: Wi-Fi Aware  
**Kind**: method

Subscribes to the provided service over Wi-Fi, providing browse results for connecting to the specified paired devices if available.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
static func connecting(to pairedDevices: WASubscriberBrowser.Devices, from mySubscribingService: WASubscribableService) -> WASubscriberBrowser.Action
```

#### Return Value

A new `Action` configuring this operation.

#### Discussion

When subscribing, the `NetworkBrowser` provides a [`WAEndpoint`](waendpoint.md) for each discovered paired device, and the app can then create a `NetworkConnection` object to connect to each. Data path parameters including the [`WAPerformanceMode`](waperformancemode.md) are set when creating the connection, using [`WAParameters`](waparameters.md) written into the `Network/NWParameters` for the `NetworkConnection`.

## Parameters

- `pairedDevices`: The devices to connect to. The browser isn’t activated if no devices are specified.
- `mySubscribingService`: The service to discover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wasubscriberbrowser/action/connecting(to:from:))*