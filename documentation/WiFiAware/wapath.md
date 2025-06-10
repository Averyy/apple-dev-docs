# WAPath

**Framework**: Wi-Fi Aware  
**Kind**: struct

A representation of the current Wi-Fi Aware path.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
struct WAPath
```

## Topics

### Getting a connection endpoint
- [let endpoint: WAEndpoint](wapath/endpoint.md)
  The Wi-Fi Aware endpoint that’s connected.
### Getting a current performance
- [let performance: WAPerformanceReport](wapath/performance.md)
  The current performance metrics for the Wi-Fi Aware data path.
### Getting path metrics
- [let durationActive: Duration](wapath/durationactive.md)
  A property that indicates a cumulative duration data path is connected on this Wi-Fi Aware path.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct NWPath](../Network/NWPath.md)
  An object that contains information about the properties of the network that a connection uses, or that are available to your app.
- [enum WAPerformanceMode](waperformancemode.md)
  The performance mode that indicates what performance criterion to prioritize.
- [enum WAAccessCategory](waaccesscategory.md)
  The underling quality-of-service (QoS) the Wi-Fi layer uses to transmit data packets from a connection over the air.
- [struct WAPerformanceReport](waperformancereport.md)
  The current performance state of the data path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapath)*