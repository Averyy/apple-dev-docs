# firstMatch

**Framework**: XCUIAutomation  
**Kind**: property  
**Required**: Yes

The first element that matches the query.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Xcode 16.3+

## Declaration

```swift
@MainActor
var firstMatch: XCUIElement { get }
```

#### Discussion

Use the [`firstMatch`](xcuielementtypequeryprovider/firstmatch.md) property when you know that there can only be one possible match for an element query. When you call [`firstMatch`](xcuielementtypequeryprovider/firstmatch.md), the framework stops traversing your app’s accessibility hierarchy as soon as it finds a matching element, speeding up element query resolution.

> **Note**:  Only use [`firstMatch`](xcuielementtypequeryprovider/firstmatch.md) in cases where you know categorically that a single element matches a query. Accessing the [`firstMatch`](xcuielementtypequeryprovider/firstmatch.md) property doesn’t check for multiple conflicting matches in ambiguous cases. Use [`XCUIElementQuery`](xcuielementquery.md)‘s [`element`](xcuielementquery/element.md) property instead if you want to check for multiple matches before using the element, and to fail the test if there isn’t a single unique match.

## See Also

- [var element: XCUIElement](xcuielementquery/element.md)
  The query’s single matching element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielementtypequeryprovider/firstmatch)*