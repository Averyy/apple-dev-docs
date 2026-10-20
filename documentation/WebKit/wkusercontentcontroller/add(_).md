# add(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Adds the specified content rule list to the content controller object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
func add(_ contentRuleList: WKContentRuleList)
```

```objc
- (void) addContentRuleList:(WKContentRuleList *) contentRuleList;
```

#### Discussion

Call this method to apply a set of content filtering rules to your web view’s configuration.

## Parameters

- `contentRuleList`: The rule list to add. Create and retrieve rules lists using a `WKContentExtensionStore` object.

## See Also

### Adding and Removing Content Rules
- [func remove(WKContentRuleList)](./remove%28_%29.md)
  Removes the specified rule list from the content controller object.
- [func removeAllContentRuleLists()](./removeallcontentrulelists%28%29.md)
  Removes all rules lists from the content controller.
- [class WKContentRuleList](../wkcontentrulelist.md)
  A compiled list of rules to apply to web content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkusercontentcontroller/add(_:))*