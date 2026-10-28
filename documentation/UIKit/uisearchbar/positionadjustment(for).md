# positionAdjustment(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the position adjustment for a given icon.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func positionAdjustment(for icon: UISearchBar.Icon) -> UIOffset
```

```objc
- (UIOffset) positionAdjustmentForSearchBarIcon:(UISearchBarIcon) icon;
```

## Return Value

The position adjustment for the icon identified by `icon`.

## Discussion

The offset is used to adjust the position of an icon within the search text field.

## Parameters

- `icon`: An icon identifier constant.

## See Also

### Customizing the search bar appearance
- [var backgroundImage: UIImage?](./backgroundimage.md)
  The background image for the search bar.
- [func backgroundImage(for: UIBarPosition, barMetrics: UIBarMetrics) -> UIImage?](./backgroundimage%28for,barmetrics%29.md)
  Returns the image used for the background in a given position and with given metrics.
- [func setBackgroundImage(UIImage?, for: UIBarPosition, barMetrics: UIBarMetrics)](./setbackgroundimage%28_,for,barmetrics%29.md)
  Sets the image to use for the background in a given position and with given metrics.
- [func image(for: UISearchBar.Icon, state: UIControl.State) -> UIImage?](./image%28for,state%29.md)
  Returns the image for a given search bar icon type and control state.
- [func setImage(UIImage?, for: UISearchBar.Icon, state: UIControl.State)](./setimage%28_,for,state%29.md)
  Sets the image for a given search bar icon type and control state.
- [func setPositionAdjustment(UIOffset, for: UISearchBar.Icon)](./setpositionadjustment%28_,for%29.md)
  Returns the position adjustment for a given icon.
- [var inputAccessoryView: UIView?](./inputaccessoryview.md)
  A custom input accessory view for the keyboard of the search bar.
- [func searchFieldBackgroundImage(for: UIControl.State) -> UIImage?](./searchfieldbackgroundimage%28for%29.md)
  Returns the search text field image for a given state.
- [func setSearchFieldBackgroundImage(UIImage?, for: UIControl.State)](./setsearchfieldbackgroundimage%28_,for%29.md)
  Sets the search text field image for a given state.
- [var searchFieldBackgroundPositionAdjustment: UIOffset](./searchfieldbackgroundpositionadjustment.md)
  The offset of the search text field background in the search bar.
- [var searchTextPositionAdjustment: UIOffset](./searchtextpositionadjustment.md)
  The offset of the text within the search text field background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/positionadjustment(for:))*