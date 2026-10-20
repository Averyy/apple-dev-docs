# tabs

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An array of tabs that the tab bar displays.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var tabs: [UITab] { get set }
```

```objc
@property (nonatomic, copy) NSArray<__kindof UITab *> * tabs;
```

## Mentions

- [Elevating your iPad app with a tab bar and sidebar](../elevating-your-ipad-app-with-a-tab-bar-and-sidebar.md)

#### Discussion

To set the tab bar’s content, assign an array of [`UITab`](../uitab.md) objects to this property. For more information, see [Elevating your iPad app with a tab bar and sidebar](../elevating-your-ipad-app-with-a-tab-bar-and-sidebar.md).

## See Also

### Assigning tabs
- [func setTabs([UITab], animated: Bool)](./settabs%28_,animated%29.md)
  Sets the root tabs of the tab bar controller, with an option to animate the change.
- [func performBatchUpdates(() -> Void)](./performbatchupdates%28_%29.md)
  Animates multiple tab changes as a single update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/tabs)*