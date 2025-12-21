# WAPublisherListener.DatapathParameters

**Framework**: Wi-Fi Aware  
**Kind**: struct

The parameter that sets the initial Wi-Fi Aware data path configuration for any devices that are connected.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
struct DatapathParameters
```

#### Overview

The `DatapathParameters` is an optional “`datapath:`” component of the `.wifiAware()` instruction to a `NetworkListener`. If you don’t set a specific parameter, then the system applies the default parameters with bulk performance mode.

The code below is an example of how to set a data path configuration:

```swift
NetworkListener(for: .wifiAware( .connecting(to:service,  from:.selected(devices)) datapath: .defaults) )
```

> ❗ **Important**: Each service must have the same [`WAPerformanceMode`](waperformancemode.md) on both the `NetworkBrowser` (subscriber) and `NetworkListener` (publisher) sides of the connection, or the resulting performance behavior is undefined. If not specified, the performance mode defaults to [`WAPerformanceMode.bulk`](waperformancemode/bulk.md) on both sides.

## Topics

### Setting performance modes
- [static let defaults: WAPublisherListener.DatapathParameters](wapublisherlistener/datapathparameters/defaults.md)
  The property that configures default parameters that prioritize bulk throughput, power consumption, and other concurrent Wi-Fi use cases.
- [static let realtime: WAPublisherListener.DatapathParameters](wapublisherlistener/datapathparameters/realtime.md)
  Parameters that prioritize latency at the expense of throughput, power consumption, and other concurrent Wi-Fi use cases and devices.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct WAPublisherListener](wapublisherlistener.md)
  Configures a network listener to publish a service over Wi-Fi Aware and accept incoming connections from paired devices.
- [WAPublisherListener.Action](wapublisherlistener/action.md)
  The structure that configures the Wi-Fi Aware publisher operation that the network listener performs.
- [WAPublisherListener.Devices](wapublisherlistener/devices.md)
  The structure that determines the devices to connect to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapublisherlistener/datapathparameters)*