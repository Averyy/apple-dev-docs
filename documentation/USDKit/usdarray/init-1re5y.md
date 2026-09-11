# init(_:)

**Framework**: USDKit  
**Kind**: init

Creates an array containing the elements of `s`.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(_ s: some Sequence<Element>)
```

#### Discussion

The backing C++ storage is reserved up front from the sequence’s `underestimatedCount`, so the common case allocates once rather than reallocating repeatedly while appending. `underestimatedCount` is exact and `O(1)` for collections such as `Array`; for sequences whose count isn’t known it is a lower bound (possibly zero) used purely as a reservation hint, which avoids a second traversal just to count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdarray/init(_:)-1re5y)*