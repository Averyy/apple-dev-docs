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

This method returns [`true`](https://developer.apple.com/documentation/Swift/true) if the receiver contains all of the trait values in the trait collection passed in the `trait` parameter, and returns [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

#### Discussion

Use this method to compare two standalone trait collections, or to compare the iOS interface environment’s trait collection to a standalone trait collection.

## Parameters

- `trait`: A trait collection that you want to compare to the current trait collection.

## See Also

- [func hasDifferentColorAppearance(comparedTo: UITraitCollection?) -> Bool](uitraitcollection/hasdifferentcolorappearance(comparedto:).md)
  Queries whether changing between the specified and current trait collections would affect color values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitcollection/containstraits(in:))*