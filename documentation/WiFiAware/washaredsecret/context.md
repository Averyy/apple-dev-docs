# WASharedSecret.Context

**Framework**: Wi-Fi Aware  
**Kind**: struct  
**Role**: Structure

A unique value that is specific to your App and the use case a given connection will perform, which diversifies the generated secret so that it is unique to your App and connection.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
struct Context
```

## Topics

### Initializers
- [init?(Data)](./context/init%28_%29-74fai.md)
  Creates a new custom context that provides unique data.
- [init?(String)](./context/init%28_%29-8fpqd.md)
  Creates a new custom context that provides a unique string.
### Type Properties
- [static let bundleID: WASharedSecret.Context](./context/bundleid.md)
  A string that provides a unique value specific to your app.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/washaredsecret/context)*