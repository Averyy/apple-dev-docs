# backgroundImage(for:barMetrics:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the image used for the background in a given position and with given metrics.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func backgroundImage(for barPosition: UIBarPosition, barMetrics: UIBarMetrics) -> UIImage?
```

```objc
- (UIImage *) backgroundImageForBarPosition:(UIBarPosition) barPosition barMetrics:(UIBarMetrics) barMetrics;
```

## Return Value

The image used for the search bar background in the position specified by `barPosition` and with the metrics specified by `barMetrics`.

## Discussion

The default value is `nil`.

## Parameters

- `barPosition`: A bar position constant.
- `barMetrics`: A bar metrics constant.

## See Also

### Customizing the search bar appearance
- [var backgroundImage: UIImage?](./backgroundimage.md)
  The background image for the search bar.
- [func setBackgroundImage(UIImage?, for: UIBarPosition, barMetrics: UIBarMetrics)](./setbackgroundimage%28_,for,barmetrics%29.md)
  Sets the image to use for the background in a given position and with given metrics.
- [func image(for: UISearchBar.Icon, state: UIControl.State) -> UIImage?](./image%28for,state%29.md)
  Returns the image for a given search bar icon type and control state.
- [func setImage(UIImage?, for: UISearchBar.Icon, state: UIControl.State)](./setimage%28_,for,state%29.md)
  Sets the image for a given search bar icon type and control state.
- [func positionAdjustment(for: UISearchBar.Icon) -> UIOffset](./positionadjustment%28for%29.md)
  Returns the position adjustment for a given icon.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/backgroundimage(for:barmetrics:))*