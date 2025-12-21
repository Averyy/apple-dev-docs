# WAParameters

**Framework**: Wi-Fi Aware  
**Kind**: struct

Parameters configuring a Wi-Fi Aware data path connection.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
struct WAParameters
```

#### Overview

You can customize Wi-Fi Aware configuration with the parameters passed in the `.wifiAware()` instruction to the `NetworkBrowser` and `NetworkListener`, or via the `.wifiAware:WAParameters?` property on `NWParameters`.

For more information about creating a `NetworkListener`, refer to [`WAPublisherListener.DatapathParameters`](wapublisherlistener/datapathparameters.md)

> ❗ **Important**: Each service must have the same [`WAPerformanceMode`](waperformancemode.md) on both the `NetworkBrowser` (subscriber) and `NetworkListener` (publisher) sides of the connection, or the resulting performance behavior is undefined. If not specified, the performance mode defaults to [`WAPerformanceMode.bulk`](waperformancemode/bulk.md) on both sides.

## Topics

### Setting common configurations
- [static let defaults: WAParameters](waparameters/defaults.md)
  The property that configures default parameters that prioritize bulk throughput, power consumption, and other concurrent Wi-Fi use cases.
- [static let realtime: WAParameters](waparameters/realtime.md)
  The property that configures parameters that prioritize latency at the expense of throughput, power consumption, and other concurrent Wi-Fi use cases.
### Checking the configured performance mode
- [var performanceMode: WAPerformanceMode](waparameters/performancemode.md)
  The initial performance configuration of the data path when connected.
- [init(performanceMode: WAPerformanceMode)](waparameters/init(performancemode:).md)
  Initializes the parameters with defaults.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NWParameters](../Network/NWParameters.md)
  An object that stores the protocols to use for connections, options for sending data, and network path constraints.
- [struct NWParametersBuilder](../Network/NWParametersBuilder.md)
  An opaque class that is responsible for creating and configuring NWParameters based on the parameterized protocol stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waparameters)*