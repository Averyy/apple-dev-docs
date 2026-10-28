# UITrait

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

A type representing a trait in a trait collection.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS

## Declaration

```swift
typealias UITrait = any UITraitDefinition.Type
```

## Discussion

The type of a trait serves as a key to uniquely identify a trait in a trait collection. The [`subscript(_:)`](./uitraitcollection/subscript%28_%29-96v58.md) method of [`UITraitCollection`](./uitraitcollection.md) and [`registerForTraitChanges(_:handler:)`](./uitraitchangeobservable-67e94/registerfortraitchanges%28_,handler%29.md) are two examples that take trait types to identify traits in the collection.

## See Also

### Custom traits
- [Providing data to the view hierarchy with custom traits](./providing-data-to-the-view-hierarchy-with-custom-traits.md)
  Share data that needs to flow hierarchically across multiple levels of your view hierarchy.
- [protocol UIMutableTraits](./uimutabletraits-13ja5.md)
  A mutable container of traits.
- [protocol UITraitDefinition](./uitraitdefinition-64c15.md)
  A type representing a trait in a trait collection.
- [protocol UITraitBridgedEnvironmentKey](./uitraitbridgedenvironmentkey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitrait-9423)*