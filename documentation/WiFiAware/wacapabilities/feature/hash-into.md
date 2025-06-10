# hash(into:)

**Framework**: Wi-Fi Aware  
**Kind**: method

Hashes the essential components of this value by feeding them into the given hasher.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
func hash(into hasher: inout Hasher)
```

#### Discussion

Implement this method to conform to the `Hashable` protocol. The components used for hashing must be the same as the components compared in your type’s `==` operator implementation. Call `hasher.combine(_:)` with each of these components.

> ❗ **Important**: In your implementation of `hash(into:)`, don’t call `finalize()` on the `hasher` instance provided, or replace it with a different instance. Doing so may become a compile-time error in the future.

## Parameters

- `hasher`: The hasher to use when combining the components   of this instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wacapabilities/feature/hash(into:))*