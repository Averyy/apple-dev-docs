# titleTextAttributes

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

String attributes to apply to the text of the tab bar item’s title.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var titleTextAttributes: [NSAttributedString.Key : Any] { get set }
```

```objc
@property (nonatomic, copy, readwrite) NSDictionary<NSString *,id> * titleTextAttributes;
```

## Discussion

If you don’t specify font or color attributes for the text, UIKit supplies appropriate default values. For a list of possible keys, see [`NSAttributedString.Key`](../../Foundation/nsattributedstring/key.md).

## See Also

### Configuring the item’s title
- [var titlePositionAdjustment: UIOffset](./titlepositionadjustment.md)
  The additional amount by which to offset the title horizontally and vertically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbaritemstateappearance/titletextattributes)*