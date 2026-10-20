# containsTraits(in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Queries whether a trait collection contains all of another trait collection’s values.

**Availability**:
- iOS 8.0+ - Deprecated in 17.0
- iPadOS 8.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- tvOS - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Compare values for specific traits in the trait collections instead.

## Declaration

```swift
func containsTraits(in trait: UITraitCollection?) -> Bool
```

```objc
- (BOOL) containsTraitsInCollection:(UITraitCollection *) trait;
```

#### Return Value

This method returns [`true`](../../Swift/true.md) if the receiver contains all of the trait values in the trait collection passed in the `trait` parameter, and returns [`false`](../../Swift/false.md) otherwise.

#### Discussion

Use this method to compare two standalone trait collections, or to compare the iOS interface environment’s trait collection to a standalone trait collection.

## Parameters

- `trait`: A trait collection that you want to compare to the current trait collection.

## See Also

### Deprecated
- [init(traitsFrom: [UITraitCollection])](./init%28traitsfrom%29.md)
  Creates a trait collection that consists of traits merged from a specified array of trait collections.
- [init(traitsFromCollections: [UITraitCollection])](./init%28traitsfromcollections%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitcollection/containstraits(in:))*