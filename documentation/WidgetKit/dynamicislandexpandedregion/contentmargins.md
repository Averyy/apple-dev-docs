# contentMargins(_:_:)

**Framework**: Widgetkit  
**Kind**: method

Overrides default content margins for the provided edges in the Dynamic Island.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+

## Declaration

```swift
func contentMargins(_ edges: Edge.Set = .all, _ length: Double) -> DynamicIslandExpandedRegion<Content>
```

#### Return Value

The view for the Dynamic Island expanded region with the updated content margins.

#### Discussion

If you repeatedly use the `contentMargins(_:_:)` modifier, the system uses the innermost specified values. The following example results in a margin of 8 points for the trailing, top, and bottom edges, and uses the default margin for the leading edge:

```swift
DynamicIslandContentRegion(.trailing) {
    ContainerRelativeShape()
    .aspectRatio(1, contentMode:.fit)
}.contentMargins([.trailing, .top, .bottom], 8)
```

Note that the system applies the provided custom content margins to content that’s adjacent to the modified content margin edges.

## Parameters

- `edges`: The edges that use the custom content margins.
- `length`: The length of the custom margin for the given  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/dynamicislandexpandedregion/contentmargins(_:_:))*