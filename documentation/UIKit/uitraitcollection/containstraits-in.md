# containsTraits(in:)

**Framework**: UIKit  
**Kind**: method

Queries whether a trait collection contains all of another trait collection’s values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func containsTraits(in trait: UITraitCollection?) -> Bool
```

#### Return Value

This method returns [`true`](https://developer.apple.com/documentation/swift/true) if the receiver contains all of the trait values in the trait collection passed in the `trait` parameter, and returns [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

Use this method to compare two standalone trait collections, or to compare the iOS interface environment’s trait collection to a standalone trait collection.

## Parameters

- `trait`: A trait collection that you want to compare to the current trait collection.

## See Also

- [init(traitsFrom: [UITraitCollection])](uitraitcollection/init(traitsfrom:).md)
  Creates a trait collection that consists of traits merged from a specified array of trait collections.
- [init(traitsFromCollections: [UITraitCollection])](uitraitcollection/init(traitsfromcollections:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitcollection/containstraits(in:))*