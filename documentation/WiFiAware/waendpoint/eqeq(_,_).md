# ==(_:_:)

**Framework**: Wi-Fi Aware  
**Kind**: op  
**Role**: Operator

Two endpoints are logically equivalent if they have the same service type (publish vs subscribe) with the same name, and refer to the same device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
static func == (lhs: WAEndpoint, rhs: WAEndpoint) -> Bool
```

#### Return Value

`true` if both sides are logically equivalent, `false` otherwise

## Parameters

- `lhs`: The left-hand side object.
- `rhs`: The other object to compare.

## See Also

### Hashing and comparing
- [func hash(into: inout Hasher)](./hash%28into%29.md)
  Compute unique hash of this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waendpoint/==(_:_:))*