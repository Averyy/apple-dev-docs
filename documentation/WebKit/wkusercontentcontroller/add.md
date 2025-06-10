# add(_:)

**Framework**: WebKit  
**Kind**: method

Adds the specified content rule list to the content controller object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func add(_ contentRuleList: WKContentRuleList)
```

#### Discussion

Call this method to apply a set of content filtering rules to your web view’s configuration.

## Parameters

- `contentRuleList`: The rule list to add. Create and retrieve rules lists using a   object.

## See Also

- [func remove(WKContentRuleList)](wkusercontentcontroller/remove(_:).md)
  Removes the specified rule list from the content controller object.
- [func removeAllContentRuleLists()](wkusercontentcontroller/removeallcontentrulelists.md)
  Removes all rules lists from the content controller.
- [class WKContentRuleList](wkcontentrulelist.md)
  A compiled list of rules to apply to web content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkusercontentcontroller/add(_:))*