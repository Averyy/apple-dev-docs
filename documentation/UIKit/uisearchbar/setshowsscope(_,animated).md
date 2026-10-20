# setShowsScope(_:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Specifies whether the scope bar is displayed, optionally using an animation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func setShowsScope(_ show: Bool, animated animate: Bool)
```

```objc
- (void) setShowsScopeBar:(BOOL) show animated:(BOOL) animate;
```

#### Discussion

If the search bar is owned by a [`UISearchController`](../uisearchcontroller.md), then calling this method implicitly sets the search controller’s [`automaticallyShowsScopeBar`](../uisearchcontroller/automaticallyshowsscopebar.md) property to [`false`](../../Swift/false.md).

## Parameters

- `show`: A Boolean value that indicates whether the scope bar is shown.
- `animate`: A Boolean value that indicates whether the scope bar animates when it appears and disappears.

## See Also

### Configuring scope bar buttons
- [var scopeButtonTitles: [String]?](./scopebuttontitles.md)
  An array of strings indicating the titles of the scope buttons.
- [var selectedScopeButtonIndex: Int](./selectedscopebuttonindex.md)
  The index of the selected scope button.
- [var showsScopeBar: Bool](./showsscopebar.md)
  Specifies whether the scope bar is displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/setshowsscope(_:animated:))*