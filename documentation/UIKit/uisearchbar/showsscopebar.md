# showsScopeBar

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Specifies whether the scope bar is displayed.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var showsScopeBar: Bool { get set }
```

```objc
@property (nonatomic) BOOL showsScopeBar;
```

#### Discussion

If the search bar is owned by a [`UISearchController`](../uisearchcontroller.md), then setting this property implicitly sets the search controller’s [`automaticallyShowsScopeBar`](../uisearchcontroller/automaticallyshowsscopebar.md) property to [`false`](../../Swift/false.md).

## See Also

### Configuring scope bar buttons
- [var scopeButtonTitles: [String]?](./scopebuttontitles.md)
  An array of strings indicating the titles of the scope buttons.
- [var selectedScopeButtonIndex: Int](./selectedscopebuttonindex.md)
  The index of the selected scope button.
- [func setShowsScope(Bool, animated: Bool)](./setshowsscope%28_,animated%29.md)
  Specifies whether the scope bar is displayed, optionally using an animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/showsscopebar)*