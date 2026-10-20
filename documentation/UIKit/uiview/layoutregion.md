# UIView.LayoutRegion

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct LayoutRegion
```

## Topics

### Type Methods
- [static func bar(onEdge: UIRectEdge) -> UIView.LayoutRegion](./layoutregion/bar%28onedge%29-4937k.md)
- [static func bar(onEdge: NSDirectionalRectEdge) -> UIView.LayoutRegion](./layoutregion/bar%28onedge%29-52kes.md)
- [static func bar(onEdge: NSDirectionalRectEdge, extent: CGFloat) -> UIView.LayoutRegion](./layoutregion/bar%28onedge,extent%29-2tj1g.md)
- [static func bar(onEdge: UIRectEdge, extent: CGFloat) -> UIView.LayoutRegion](./layoutregion/bar%28onedge,extent%29-8rmhq.md)
- [static func margins(cornerAdaptation: UIView.LayoutRegion.AdaptivityAxis?) -> UIView.LayoutRegion](./layoutregion/margins%28corneradaptation%29.md)
- [static func readableContent(cornerAdaptation: UIView.LayoutRegion.AdaptivityAxis?) -> UIView.LayoutRegion](./layoutregion/readablecontent%28corneradaptation%29.md)
- [static func safeArea(cornerAdaptation: UIView.LayoutRegion.AdaptivityAxis?) -> UIView.LayoutRegion](./layoutregion/safearea%28corneradaptation%29.md)
### Enumerations
- [UIView.LayoutRegion.AdaptivityAxis](./layoutregion/adaptivityaxis.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Accessing insets and layout guides
- [static func bar(onEdge: NSDirectionalRectEdge, extent: CGFloat) -> UIView.LayoutRegion](./layoutregion/bar%28onedge,extent%29-2tj1g.md)
- [static func bar(onEdge: UIRectEdge, extent: CGFloat) -> UIView.LayoutRegion](./layoutregion/bar%28onedge,extent%29-8rmhq.md)
- [func directionalEdgeInsets(for: UIView.LayoutRegion) -> NSDirectionalEdgeInsets](./directionaledgeinsets%28for%29.md)
- [func edgeInsets(for: UIView.LayoutRegion) -> UIEdgeInsets](./edgeinsets%28for%29.md)
- [func layoutGuide(for: UIView.LayoutRegion) -> UILayoutGuide](./layoutguide%28for%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/layoutregion)*