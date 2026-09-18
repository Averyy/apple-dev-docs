# systemTraitsAffectingVerticalBarEdge

**Framework**: UIKit  
**Kind**: property

The system traits that affect the value of `verticalBarEdge`.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
static var systemTraitsAffectingVerticalBarEdge: [UITrait] { get }
```

#### Discussion

Pass this array to `registerForTraitChanges(_:handler:)` to be notified when the vertical bar edge changes. Note that it is possible for the actual edge to be the same even if the traits affecting the vertical bar edge themselves may have changed.

## See Also

- [static var systemTraitsAffectingColorAppearance: [UITrait]](uitraitcollection/systemtraitsaffectingcolorappearance-64z7q.md)
- [static var systemTraitsAffectingImageLookup: [UITrait]](uitraitcollection/systemtraitsaffectingimagelookup-4jv5.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitcollection/systemtraitsaffectingverticalbaredge-475st)*