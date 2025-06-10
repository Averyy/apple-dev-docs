# DynamicIslandExpandedContentBuilder

**Framework**: WidgetKit  
**Kind**: struct

A result builder that constructs the content of an expanded Live Activity in the Dynamic Island.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
@resultBuilder
struct DynamicIslandExpandedContentBuilder
```

## Topics

### Type Methods
- [static func buildPartialBlock<C0, C1>(accumulated: DynamicIslandExpandedContent<C0>, next: DynamicIslandExpandedContent<C1>) -> DynamicIslandExpandedContent<some View>
](dynamicislandexpandedcontentbuilder/buildpartialblock(accumulated:next:)-39sr0.md)
- [static func buildPartialBlock<C0, C1>(accumulated: DynamicIslandExpandedContent<C0>, next: DynamicIslandExpandedRegion<C1>) -> DynamicIslandExpandedContent<some View>
](dynamicislandexpandedcontentbuilder/buildpartialblock(accumulated:next:)-3jswv.md)
- [static func buildPartialBlock<C>(first: DynamicIslandExpandedRegion<C>) -> DynamicIslandExpandedContent<some View>
](dynamicislandexpandedcontentbuilder/buildpartialblock(first:)-5j108.md)
- [static func buildPartialBlock<C>(first: DynamicIslandExpandedContent<C>) -> DynamicIslandExpandedContent<some View>
](dynamicislandexpandedcontentbuilder/buildpartialblock(first:)-74hpw.md)

## See Also

- [init(DynamicIslandExpandedRegionPosition, priority: Double, content: () -> Content)](dynamicislandexpandedregion/init(_:priority:content:).md)
  Creates the object that defines and positions the content of an expanded Live Activity in the Dynamic Island.
- [struct DynamicIslandExpandedRegionPosition](dynamicislandexpandedregionposition.md)
  View positions of an expanded Live Activity that appears in the Dynamic Island.
- [@MainActor @preconcurrency func dynamicIsland(verticalPlacement: DynamicIslandExpandedRegionVerticalPlacement) -> some View
](../SwiftUI/View/dynamicIsland(verticalPlacement:).md)
  Specifies the vertical placement for a view of an expanded Live Activity that appears in the Dynamic Island.
- [struct DynamicIslandExpandedRegionVerticalPlacement](dynamicislandexpandedregionverticalplacement.md)
  Vertical view positions of an expanded Live Activity that appears in the Dynamic Island.
- [struct DynamicIslandExpandedContent](dynamicislandexpandedcontent.md)
  A view that describes the expanded presentation of a Live Activity that appears in the Dynamic Island.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/dynamicislandexpandedcontentbuilder)*