# WACapabilities

**Framework**: Wi-Fi Aware  
**Kind**: struct

A structure that checks the host device’s supported features and capabilities.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
struct WACapabilities
```

## Topics

### Checking features supported by host device
- [WACapabilities.Feature](wacapabilities/feature.md)
  Features that your app’s current host device can support.
- [static var supportedFeatures: Set<WACapabilities.Feature>](wacapabilities/supportedfeatures.md)
  A property that returns a set of supported features, or an empty set if the current platform doesn’t support Wi-Fi Aware.
### Checking for the maximum devices and services
- [static var maximumConnectableDevices: Int](wacapabilities/maximumconnectabledevices.md)
  The maximum number of unique devices your app can connect to simultaneously.
- [static var maximumPublishableServices: Int](wacapabilities/maximumpublishableservices.md)
  The maximum number of unique services your app can publish simultaneously.
- [static var maximumSubscribableServices: Int](wacapabilities/maximumsubscribableservices.md)
  The maximum number of unique services your app can simultaneously subscribe to.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [WACapabilities.Feature](wacapabilities/feature.md)
  Features that your app’s current host device can support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wacapabilities)*