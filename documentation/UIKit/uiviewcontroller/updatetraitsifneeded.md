# updateTraitsIfNeeded()

**Framework**: UIKit  
**Kind**: method

Updates traits immediately for this view controller and its view, including any view controllers and views in this subtree.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func updateTraitsIfNeeded()
```

#### Discussion

The system sends trait change callbacks synchronously.

## See Also

- [var traitOverrides: UITraitOverrides](uiviewcontroller/traitoverrides-1z1cc.md)
  A mutable container of traits you use to set trait changes for this view controller and its views.
- [struct UITraitOverrides](uitraitoverrides-swift.struct.md)
  A mutable container of traits you use to set trait changes for an object and its descendants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/updatetraitsifneeded())*