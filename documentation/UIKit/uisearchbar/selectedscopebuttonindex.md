# selectedScopeButtonIndex

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The index of the selected scope button.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var selectedScopeButtonIndex: Int { get set }
```

```objc
@property (nonatomic) NSInteger selectedScopeButtonIndex;
```

## Discussion

The indexes of the scope buttons are determined by the indexes of the strings in [`scopeButtonTitles`](./scopebuttontitles.md).

## See Also

### Configuring scope bar buttons
- [var scopeButtonTitles: [String]?](./scopebuttontitles.md)
  An array of strings indicating the titles of the scope buttons.
- [var showsScopeBar: Bool](./showsscopebar.md)
  Specifies whether the scope bar is displayed.
- [func setShowsScope(Bool, animated: Bool)](./setshowsscope%28_,animated%29.md)
  Specifies whether the scope bar is displayed, optionally using an animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/selectedscopebuttonindex)*