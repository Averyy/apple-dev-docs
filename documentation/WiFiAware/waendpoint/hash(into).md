# hash(into:)

**Framework**: Wi-Fi Aware  
**Kind**: method  
**Role**: Instance Method

Compute unique hash of this object.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func hash(into hasher: inout Hasher)
```

## Parameters

- `hasher`: The hasher to combine the properties into.

## See Also

### Hashing and comparing
- [static func == (WAEndpoint, WAEndpoint) -> Bool](./eqeq%28_,_%29.md)
  Two endpoints are logically equivalent if they have the same service type (publish vs subscribe) with the same name, and refer to the same device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waendpoint/hash(into:))*