# WKContentRuleList

**Framework**: Webkit  
**Kind**: class

A compiled list of rules to apply to web content.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class WKContentRuleList
```

#### Overview

A [`WKContentRuleList`](wkcontentrulelist.md) object represents a compiled set of rules for modifying how a webpage loads content. You don’t create a [`WKContentRuleList`](wkcontentrulelist.md) directly. Instead, you specify your rules in JSON format and compile them using the [`compileContentRuleList(forIdentifier:encodedContentRuleList:completionHandler:)`](wkcontentruleliststore/compilecontentrulelist(foridentifier:encodedcontentrulelist:completionhandler:).md) method of [`WKContentRuleListStore`](wkcontentruleliststore.md). That method compiles your rules into an efficient byte format and returns them in an instance of this class.

Content rule lists use the same syntax as content blocker extensions in Safari. For more information on how to specify the JSON for your rule lists, see [`Creating a content blocker`](https://developer.apple.com/documentation/SafariServices/creating-a-content-blocker).

## Topics

### Getting the Rules List Identifier
- [var identifier: String!](wkcontentrulelist/identifier.md)
  The identifier for the rule list.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func add(WKContentRuleList)](wkusercontentcontroller/add(_:).md)
  Adds the specified content rule list to the content controller object.
- [func remove(WKContentRuleList)](wkusercontentcontroller/remove(_:).md)
  Removes the specified rule list from the content controller object.
- [func removeAllContentRuleLists()](wkusercontentcontroller/removeallcontentrulelists.md)
  Removes all rules lists from the content controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkcontentrulelist)*