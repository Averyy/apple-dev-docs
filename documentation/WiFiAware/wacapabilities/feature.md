# WACapabilities.Feature

**Framework**: Wi-Fi Aware  
**Kind**: enum  
**Role**: Enumeration

Features that your app’s current host device can support.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
enum Feature
```

#### Overview

Supported features are typically created by the system on behalf of the client, so they usually don’t need to be instantiated directly.

## Topics

### Checking for Wi-Fi Aware support
- [WACapabilities.Feature.wifiAware](./feature/wifiaware.md)
  Indicates that the host supports Wi-Fi Aware.

## Relationships

### Conforms To
- [CaseIterable](../../Swift/caseiterable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Host capabilities
- [struct WACapabilities](../wacapabilities.md)
  A structure that checks the host device’s supported features and capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wacapabilities/feature)*