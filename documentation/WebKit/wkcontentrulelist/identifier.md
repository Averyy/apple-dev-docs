# identifier

**Framework**: WebKit  
**Kind**: property

The identifier for the rule list.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var identifier: String! { get }
```

#### Discussion

You specify the identifier for your rule lists at compile time in the [`compileContentRuleList(forIdentifier:encodedContentRuleList:completionHandler:)`](wkcontentruleliststore/compilecontentrulelist(foridentifier:encodedcontentrulelist:completionhandler:).md) method of [`WKContentRuleListStore`](wkcontentruleliststore.md). You also use this identifier to look up the rules list later.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkcontentrulelist/identifier)*