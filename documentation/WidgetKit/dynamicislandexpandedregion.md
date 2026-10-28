# DynamicIslandExpandedRegion

**Framework**: WidgetKit  
**Kind**: struct  
**Role**: Structure

A structure that defines and positions the content of an expanded Live Activity in the Dynamic Island.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
struct DynamicIslandExpandedRegion<Content> where Content : View
```

## Overview

The expanded presentation of a Live Activity in the Dynamic Island consists of four regions:

- [`center`](./dynamicislandexpandedregionposition/center.md) places content right below the TrueDepth camera.
- [`leading`](./dynamicislandexpandedregionposition/leading.md) places content along the leading edge of the expanded Live Activity next to the TrueDepth camera and wraps additional content below it.
- [`trailing`](./dynamicislandexpandedregionposition/trailing.md) places content along the trailing edge of the expanded Live Activity next to the TrueDepth camera and wraps additional content below it.
- [`bottom`](./dynamicislandexpandedregionposition/bottom.md) places content below leading, trailing, and center content.

## Topics

### Creating the expanded presentation
- [init(DynamicIslandExpandedRegionPosition, priority: Double, content: () -> Content)](./dynamicislandexpandedregion/init%28_,priority,content%29.md)
  Creates the object that defines and positions the content of an expanded Live Activity in the Dynamic Island.
- [struct DynamicIslandExpandedRegionPosition](./dynamicislandexpandedregionposition.md)
  View positions of an expanded Live Activity that appears in the Dynamic Island.
- [func dynamicIsland(verticalPlacement: DynamicIslandExpandedRegionVerticalPlacement) -> some View
](../SwiftUI/view/dynamicisland%28verticalplacement%29.md)
  Specifies the vertical placement for a view of an expanded Live Activity that appears in the Dynamic Island.
- [struct DynamicIslandExpandedRegionVerticalPlacement](./dynamicislandexpandedregionverticalplacement.md)
  Vertical view positions of an expanded Live Activity that appears in the Dynamic Island.
- [struct DynamicIslandExpandedContent](./dynamicislandexpandedcontent.md)
  A view that describes the expanded presentation of a Live Activity that appears in the Dynamic Island.
- [struct DynamicIslandExpandedContentBuilder](./dynamicislandexpandedcontentbuilder.md)
  A result builder that constructs the content of an expanded Live Activity in the Dynamic Island.
### Specifying custom content margins
- [func contentMargins(Edge.Set, Double) -> DynamicIslandExpandedRegion<Content>](./dynamicislandexpandedregion/contentmargins%28_,_%29.md)
  Overrides default content margins for the provided edges in the Dynamic Island.

## See Also

### Creating the view for the Dynamic Island
- [init<Expanded, CompactLeading, CompactTrailing, Minimal>(expanded: () -> DynamicIslandExpandedContent<Expanded>, compactLeading: () -> CompactLeading, compactTrailing: () -> CompactTrailing, minimal: () -> Minimal)](./dynamicisland/init%28expanded,compactleading,compacttrailing,minimal%29.md)
  Creates a configuration object with views that appear in the Dynamic Island.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/dynamicislandexpandedregion)*