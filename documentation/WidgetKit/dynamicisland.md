# DynamicIsland

**Framework**: Widgetkit  
**Kind**: struct

The layout and configuration for a Live Activity that appears in the Dynamic Island.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+

## Declaration

```swift
struct DynamicIsland
```

## Topics

### Creating the view for the Dynamic Island
- [init<Expanded, CompactLeading, CompactTrailing, Minimal>(expanded: () -> DynamicIslandExpandedContent<Expanded>, compactLeading: () -> CompactLeading, compactTrailing: () -> CompactTrailing, minimal: () -> Minimal)](dynamicisland/init(expanded:compactleading:compacttrailing:minimal:).md)
  Creates a configuration object with views that appear in the Dynamic Island.
- [struct DynamicIslandExpandedRegion](dynamicislandexpandedregion.md)
  A structure that defines and positions the content of an expanded Live Activity in the Dynamic Island.
### Deep linking
- [func widgetURL(URL?) -> DynamicIsland](dynamicisland/widgeturl(_:).md)
  Sets the URL that opens the corresponding app of a Live Activity when a user taps on the Live Activity.
### Setting a tint color
- [func keylineTint(Color?) -> DynamicIsland](dynamicisland/keylinetint(_:).md)
  Applies a subtle tint color to the surrounding border of a Live Activity that appears in the Dynamic Island.
### Specifying content margins
- [func contentMargins(Edge.Set, Double, for: DynamicIslandMode) -> DynamicIsland](dynamicisland/contentmargins(_:_:for:).md)
  Overrides default content margins for the provided content modes in the Dynamic Island.
- [struct DynamicIslandMode](dynamicislandmode.md)
  A structure that offers values that describe the content mode for a Live Activity.

## See Also

- [struct ActivityConfiguration](activityconfiguration.md)
  An object that describes the content of a Live Activity.
- [let NSUserActivityTypeLiveActivity: String](nsuseractivitytypeliveactivity.md)
  A string that the system passes to the app on launch from a Live Activity that doesn’t provide a URL.
- [enum ActivityPreviewViewKind](activitypreviewviewkind.md)
  Values that represent Live Activity presentations for use in Xcode previews.
- [enum ActivityFamily](activityfamily.md)
  A family that defines the Live Activity’s size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/dynamicisland)*