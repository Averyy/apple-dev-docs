# WASharedSecret.Context

**Framework**: Wi-Fi Aware  
**Kind**: struct

A unique value that is specific to your App and the use case a given connection will perform, which diversifies the generated secret so that it is unique to your App and connection.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
struct Context
```

## Topics

### Initializers
- [init?(Data)](washaredsecret/context/init(_:)-74fai.md)
  Creates a new custom context that provides unique data.
- [init?(String)](washaredsecret/context/init(_:)-8fpqd.md)
  Creates a new custom context that provides a unique string.
### Type Properties
- [static let bundleID: WASharedSecret.Context](washaredsecret/context/bundleid.md)
  A string that provides a unique value specific to your app.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/washaredsecret/context)*