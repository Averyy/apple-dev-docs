# scopeButtonTitles

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An array of strings indicating the titles of the scope buttons.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var scopeButtonTitles: [String]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<NSString *> * scopeButtonTitles;
```

## Discussion

The order of the strings in the array indicates the order that the corresponding buttons will be displayed, from left to right. The index in the array corresponds to the index used in [`selectedScopeButtonIndex`](./selectedscopebuttonindex.md).

## See Also

### Configuring scope bar buttons
- [var selectedScopeButtonIndex: Int](./selectedscopebuttonindex.md)
  The index of the selected scope button.
- [var showsScopeBar: Bool](./showsscopebar.md)
  Specifies whether the scope bar is displayed.
- [func setShowsScope(Bool, animated: Bool)](./setshowsscope%28_,animated%29.md)
  Specifies whether the scope bar is displayed, optionally using an animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/scopebuttontitles)*