# setBackgroundImage(_:for:barMetrics:)

**Framework**: UIKit  
**Kind**: method

Sets the image to use for the background in a given position and with given metrics.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setBackgroundImage(_ backgroundImage: UIImage?, for barPosition: UIBarPosition, barMetrics: UIBarMetrics)
```

## Parameters

- `backgroundImage`: The image to use for the search bar background in the position specified by   and with the metrics specified by  .
- `barPosition`: A bar position constant.
- `barMetrics`: A bar metrics constant.

## See Also

- [var backgroundImage: UIImage?](uisearchbar/backgroundimage.md)
  The background image for the search bar.
- [func backgroundImage(for: UIBarPosition, barMetrics: UIBarMetrics) -> UIImage?](uisearchbar/backgroundimage(for:barmetrics:).md)
  Returns the image used for the background in a given position and with given metrics.
- [func image(for: UISearchBar.Icon, state: UIControl.State) -> UIImage?](uisearchbar/image(for:state:).md)
  Returns the image for a given search bar icon type and control state.
- [func setImage(UIImage?, for: UISearchBar.Icon, state: UIControl.State)](uisearchbar/setimage(_:for:state:).md)
  Sets the image for a given search bar icon type and control state.
- [func positionAdjustment(for: UISearchBar.Icon) -> UIOffset](uisearchbar/positionadjustment(for:).md)
  Returns the position adjustment for a given icon.
- [func setPositionAdjustment(UIOffset, for: UISearchBar.Icon)](uisearchbar/setpositionadjustment(_:for:).md)
  Returns the position adjustment for a given icon.
- [var inputAccessoryView: UIView?](uisearchbar/inputaccessoryview.md)
  A custom input accessory view for the keyboard of the search bar.
- [func searchFieldBackgroundImage(for: UIControl.State) -> UIImage?](uisearchbar/searchfieldbackgroundimage(for:).md)
  Returns the search text field image for a given state.
- [func setSearchFieldBackgroundImage(UIImage?, for: UIControl.State)](uisearchbar/setsearchfieldbackgroundimage(_:for:).md)
  Sets the search text field image for a given state.
- [var searchFieldBackgroundPositionAdjustment: UIOffset](uisearchbar/searchfieldbackgroundpositionadjustment.md)
  The offset of the search text field background in the search bar.
- [var searchTextPositionAdjustment: UIOffset](uisearchbar/searchtextpositionadjustment.md)
  The offset of the text within the search text field background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/setbackgroundimage(_:for:barmetrics:))*