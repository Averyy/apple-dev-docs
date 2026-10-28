# systemTraitsAffectingVerticalBarEdge

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The system traits that affect the value of `verticalBarEdge`.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```objc
@property (class, nonatomic, readonly) NSArray<Class<UITraitDefinition>> * systemTraitsAffectingVerticalBarEdge;
```

## Discussion

Pass this array to `-registerForTraitChanges:withHandler:` to be notified when the vertical bar edge changes. Note that it is possible for the actual edge to be the same even if the traits affecting the vertical bar edge themselves may have changed.

## See Also

### Getting related traits
- [systemTraitsAffectingColorAppearance](./systemtraitsaffectingcolorappearance-18zhm.md)
- [systemTraitsAffectingImageLookup](./systemtraitsaffectingimagelookup-640w8.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitcollection/systemtraitsaffectingverticalbaredge-8k87m)*