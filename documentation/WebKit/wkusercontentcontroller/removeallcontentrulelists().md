# removeAllContentRuleLists()

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Removes all rules lists from the content controller.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
func removeAllContentRuleLists()
```

```objc
- (void) removeAllContentRuleLists;
```

#### Discussion

This method removes the rule lists only from the user content controller object. You can still access rule lists from the [`WKContentRuleListStore`](../wkcontentruleliststore.md) objects you used to create them.

## See Also

### Adding and Removing Content Rules
- [func add(WKContentRuleList)](./add%28_%29.md)
  Adds the specified content rule list to the content controller object.
- [func remove(WKContentRuleList)](./remove%28_%29.md)
  Removes the specified rule list from the content controller object.
- [class WKContentRuleList](../wkcontentrulelist.md)
  A compiled list of rules to apply to web content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkusercontentcontroller/removeallcontentrulelists())*