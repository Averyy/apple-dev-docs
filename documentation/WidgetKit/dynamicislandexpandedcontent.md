# DynamicIslandExpandedContent

**Framework**: WidgetKit  
**Kind**: struct

A view that describes the expanded presentation of a Live Activity that appears in the Dynamic Island.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
struct DynamicIslandExpandedContent<Content> where Content : View
```

#### Overview

This view holds the intermediate content for the [`DynamicIslandExpandedContentBuilder`](dynamicislandexpandedcontentbuilder.md).

## See Also

- [init(DynamicIslandExpandedRegionPosition, priority: Double, content: () -> Content)](dynamicislandexpandedregion/init(_:priority:content:).md)
  Creates the object that defines and positions the content of an expanded Live Activity in the Dynamic Island.
- [struct DynamicIslandExpandedRegionPosition](dynamicislandexpandedregionposition.md)
  View positions of an expanded Live Activity that appears in the Dynamic Island.
- [func dynamicIsland(verticalPlacement: DynamicIslandExpandedRegionVerticalPlacement) -> some View](../SwiftUI/View/dynamicIsland(verticalPlacement:).md)
  Specifies the vertical placement for a view of an expanded Live Activity that appears in the Dynamic Island.
- [struct DynamicIslandExpandedRegionVerticalPlacement](dynamicislandexpandedregionverticalplacement.md)
  Vertical view positions of an expanded Live Activity that appears in the Dynamic Island.
- [struct DynamicIslandExpandedContentBuilder](dynamicislandexpandedcontentbuilder.md)
  A result builder that constructs the content of an expanded Live Activity in the Dynamic Island.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/dynamicislandexpandedcontent)*