# ==(_:_:)

**Framework**: Wi-Fi Aware  
**Kind**: op

Two endpoints are logically equivalent if they have the same service type (publish vs subscribe) with the same name, and refer to the same device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

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

- [func hash(into: inout Hasher)](waendpoint/hash(into:).md)
  Compute unique hash of this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waendpoint/==(_:_:))*