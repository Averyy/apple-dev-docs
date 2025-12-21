# DynamicIslandExpandedRegionVerticalPlacement

**Framework**: WidgetKit  
**Kind**: struct

Vertical view positions of an expanded Live Activity that appears in the Dynamic Island.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
struct DynamicIslandExpandedRegionVerticalPlacement
```

## Topics

### Configuring vertical content placement
- [static let `default`: DynamicIslandExpandedRegionVerticalPlacement](dynamicislandexpandedregionverticalplacement/default.md)
  The system’s default vertical placement.
- [static let belowIfTooWide: DynamicIslandExpandedRegionVerticalPlacement](dynamicislandexpandedregionverticalplacement/belowiftoowide.md)
  Vertical placement below the default vertical position for content that’s too wide to fit next to the TrueDepth camera.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [init(DynamicIslandExpandedRegionPosition, priority: Double, content: () -> Content)](dynamicislandexpandedregion/init(_:priority:content:).md)
  Creates the object that defines and positions the content of an expanded Live Activity in the Dynamic Island.
- [struct DynamicIslandExpandedRegionPosition](dynamicislandexpandedregionposition.md)
  View positions of an expanded Live Activity that appears in the Dynamic Island.
- [func dynamicIsland(verticalPlacement: DynamicIslandExpandedRegionVerticalPlacement) -> some View](../SwiftUI/View/dynamicIsland(verticalPlacement:).md)
  Specifies the vertical placement for a view of an expanded Live Activity that appears in the Dynamic Island.
- [struct DynamicIslandExpandedContent](dynamicislandexpandedcontent.md)
  A view that describes the expanded presentation of a Live Activity that appears in the Dynamic Island.
- [struct DynamicIslandExpandedContentBuilder](dynamicislandexpandedcontentbuilder.md)
  A result builder that constructs the content of an expanded Live Activity in the Dynamic Island.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/dynamicislandexpandedregionverticalplacement)*