# remove(_:)

**Framework**: WebKit  
**Kind**: method

Removes the specified rule list from the content controller object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func remove(_ contentRuleList: WKContentRuleList)
```

#### Discussion

This method removes the rule list only from the user content controller object. You can still access the rule list from the [`WKContentRuleListStore`](wkcontentruleliststore.md) object you used to create it.

## Parameters

- `contentRuleList`: The rule list to remove.

## See Also

- [func add(WKContentRuleList)](wkusercontentcontroller/add(_:).md)
  Adds the specified content rule list to the content controller object.
- [func removeAllContentRuleLists()](wkusercontentcontroller/removeallcontentrulelists.md)
  Removes all rules lists from the content controller.
- [class WKContentRuleList](wkcontentrulelist.md)
  A compiled list of rules to apply to web content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkusercontentcontroller/remove(_:))*