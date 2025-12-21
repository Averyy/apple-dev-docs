# connecting(to:from:datapath:)

**Framework**: Wi-Fi Aware  
**Kind**: method

Publishes the provided service over Wi-Fi, enabling connections from the specified paired devices.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
static func connecting(to myPublishingService: WAPublishableService, from pairedDevices: WAPublisherListener.Devices, datapath wifiAware: WAPublisherListener.DatapathParameters? = nil) -> WAPublisherListener.Action
```

#### Return Value

A new `Action` configuring this operation.

#### Discussion

When publishing, the `NetworkListener` provides a `NetworkConnection` object for each paired device that connects.

You can set the data path parameters, including the [`WAPerformanceMode`](waperformancemode.md), in the optional “`datapath:`” parameter, or by using [`WAParameters`](waparameters.md) that are written into the [`NWParameters`](https://developer.apple.com/documentation/Network/NWParameters) for the `NetworkListener`.

> ❗ **Important**: Each service must have the same [`WAPerformanceMode`](waperformancemode.md) on both the `NetworkBrowser` (subscriber) and `NetworkListener` (publisher) sides of the connection, or the resulting performance behavior is undefined. If not specified, the performance mode defaults to [`WAPerformanceMode.bulk`](waperformancemode/bulk.md) on both sides.

## Parameters

- `myPublishingService`: The service the publisher hosts, and accept connections to.
- `pairedDevices`: The remote devices to accept connections from. The   isn’t activated if the system doesn’t specify any devices.
- `wifiAware`: The parameters specifying the initial Wi-Fi Aware data path configuration for any resulting connections, or   to apply default parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapublisherlistener/action/connecting(to:from:datapath:))*