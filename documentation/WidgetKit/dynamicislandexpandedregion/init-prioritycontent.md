# init(_:priority:content:)

**Framework**: WidgetKit  
**Kind**: init

Creates the object that defines and positions the content of an expanded Live Activity in the Dynamic Island.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
init(_ position: DynamicIslandExpandedRegionPosition, priority: Double = 0, @ViewBuilder content: () -> Content)
```

## Parameters

- `position`: The position for Live Activity content.
- `priority`: The priority that tells the system which content to prioritize when it sizes   the content of an expanded Live Activity in the Dynamic Island.
- `content`: The content of an expanded Live Activity.

## See Also

- [struct DynamicIslandExpandedRegionPosition](dynamicislandexpandedregionposition.md)
  View positions of an expanded Live Activity that appears in the Dynamic Island.
- [func dynamicIsland(verticalPlacement: DynamicIslandExpandedRegionVerticalPlacement) -> some View](../SwiftUI/View/dynamicIsland(verticalPlacement:).md)
  Specifies the vertical placement for a view of an expanded Live Activity that appears in the Dynamic Island.
- [struct DynamicIslandExpandedRegionVerticalPlacement](dynamicislandexpandedregionverticalplacement.md)
  Vertical view positions of an expanded Live Activity that appears in the Dynamic Island.
- [struct DynamicIslandExpandedContent](dynamicislandexpandedcontent.md)
  A view that describes the expanded presentation of a Live Activity that appears in the Dynamic Island.
- [struct DynamicIslandExpandedContentBuilder](dynamicislandexpandedcontentbuilder.md)
  A result builder that constructs the content of an expanded Live Activity in the Dynamic Island.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/dynamicislandexpandedregion/init(_:priority:content:))*