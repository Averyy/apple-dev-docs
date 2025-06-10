# removeAllContentRuleLists()

**Framework**: WebKit  
**Kind**: method

Removes all rules lists from the content controller.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func removeAllContentRuleLists()
```

#### Discussion

This method removes the rule lists only from the user content controller object. You can still access rule lists from the [`WKContentRuleListStore`](wkcontentruleliststore.md) objects you used to create them.

## See Also

- [func add(WKContentRuleList)](wkusercontentcontroller/add(_:).md)
  Adds the specified content rule list to the content controller object.
- [func remove(WKContentRuleList)](wkusercontentcontroller/remove(_:).md)
  Removes the specified rule list from the content controller object.
- [class WKContentRuleList](wkcontentrulelist.md)
  A compiled list of rules to apply to web content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkusercontentcontroller/removeallcontentrulelists())*