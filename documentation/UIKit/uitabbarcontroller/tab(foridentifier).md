# tab(forIdentifier:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the `tab` matching the specified `identifier` in the tab bar controller’s tabs. Returns nil if no tab is found matching the `identifier`.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func tab(forIdentifier identifier: String) -> UITab?
```

```objc
- (UITab *) tabForIdentifier:(NSString *) identifier;
```

## See Also

### Accessing the tab bar controller properties
- [var tabBar: UITabBar](./tabbar.md)
  The tab bar view associated with this controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/tab(foridentifier:))*