# init(traitsFrom:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a trait collection that consists of traits merged from a specified array of trait collections.

**Availability**:
- iOS 8.0+ - Deprecated in 17.0
- iPadOS 8.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- tvOS - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`init(mutations:)`](./init%28mutations%29.md) or [`modifyingTraits(_:)`](./modifyingtraits%28_%29.md) instead.

## Declaration

```swift
init(traitsFrom traitCollections: [UITraitCollection])
```

```objc
+ (UITraitCollection *) traitCollectionWithTraitsFromCollections:(NSArray<UITraitCollection *> *) traitCollections;
```

## Return Value

A new trait collection consisting of traits merged from a specified `traitCollections` array.

## Discussion

This method takes an array of one or more trait collections and merges them to create a new trait collection. If the array contains more than one element, the highest-indexed element that contains a given trait is used for that trait. For example, the following code snippet creates a trait collection with a *compact* horizontal size class, because the second element in the array overrides the first for that trait:

```objc
UITraitCollection *newHorizontalSizeClass1 = [UITraitCollection traitCollectionWithHorizontalSizeClass: UIUserInterfaceSizeClassRegular];
UITraitCollection *newHorizontalSizeClass2 = [UITraitCollection traitCollectionWithHorizontalSizeClass: UIUserInterfaceSizeClassCompact];
NSArray *traitArray = [NSArray arrayWithObjects: newHorizontalSizeClass1, newHorizontalSizeClass2, nil];
UITraitCollection *combinedTraits = [UITraitCollection traitCollectionWithTraitsFromCollections: traitArray];
```

## Parameters

- `traitCollections`: An array of [`UITraitCollection`](../uitraitcollection.md) objects.

## See Also

### Deprecated
- [func containsTraits(in: UITraitCollection?) -> Bool](./containstraits%28in%29.md)
  Queries whether a trait collection contains all of another trait collection’s values.
- [init(traitsFromCollections: [UITraitCollection])](./init%28traitsfromcollections%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitcollection/init(traitsfrom:))*