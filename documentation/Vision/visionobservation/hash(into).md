# hash(into:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Hashes the essential components of this value by feeding them into the given hasher.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+

## Declaration

```swift
override func hash(into hasher: inout Hasher)
```

## Discussion

Implement this method to conform to the `Hashable` protocol. The components used for hashing must be the same as the components compared in your type’s `==` operator implementation. Call `hasher.combine(_:)` with each of these components.

> ❗ **Important**: In your implementation of `hash(into:)`, don’t call `finalize()` on the `hasher` instance provided, or replace it with a different instance. Doing so may become a compile-time error in the future.

## Parameters

- `hasher`: The hasher to use when combining the components of this instance.

## Default Implementations

### VisionObservation Implementations
- [func hash(into: inout Hasher)](./hash%28into%29-8aqw6.md)
  Hashes the essential components of this value by feeding them into the given hasher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/visionobservation/hash(into:))*