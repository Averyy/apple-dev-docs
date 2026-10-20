# WAEndpoint

**Framework**: Wi-Fi Aware  
**Kind**: struct  
**Role**: Structure

The endpoint of a Wi-Fi Aware connection.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct WAEndpoint
```

## Topics

### Getting the service
- [var publishedService: WAPublishableService?](./waendpoint/publishedservice.md)
  The publishable service that is, or can be, connected.
- [var subscribedService: WASubscribableService?](./waendpoint/subscribedservice.md)
  The subscribable service that is, or can be, connected.
### Getting the device anchoring the endpoint
- [let device: WAPairedDevice](./waendpoint/device.md)
  The remote device that is, or can be, connected.
### Getting a string description
- [var description: String](./waendpoint/description.md)
  The description of the object.
### Hashing and comparing
- [static func == (WAEndpoint, WAEndpoint) -> Bool](./waendpoint/eqeq%28_,_%29.md)
  Two endpoints are logically equivalent if they have the same service type (publish vs subscribe) with the same name, and refer to the same device.
- [func hash(into: inout Hasher)](./waendpoint/hash%28into%29.md)
  Compute unique hash of this object.
### Instance Properties
- [let performanceForecast: [WAPerformanceMode : WAPerformanceForecast]](./waendpoint/performanceforecast.md)
  The forecasted performance for connections setup to the remote device, per WAPerformanceMode.

## Relationships

### Conforms To
- [Connectable](../Network/connectable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Connections
- [class WAConnection](./waconnection.md)
  Provides access to the Wi-Fi Aware-specific configuration and information that underlies a given `Network/NetworkConnection`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waendpoint)*