# containing(_:)

**Framework**: XCUIAutomation  
**Kind**: method  
**Role**: Instance Method

Returns a new query that matches elements containing a descendant that meets the logical conditions of the provided predicate.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS
- Xcode 16.3+

## Declaration

```swift
func containing(_ predicate: NSPredicate) -> XCUIElementQuery
```

```objc
- (XCUIElementQuery *) containingPredicate:(NSPredicate *) predicate;
```

## Return Value

A new query that defines a search that extends the search criteria of the receiver. The new search finds elements that match the original search and contain elements that meet the logical conditions of the provided predicate.

## Discussion

The predicate evaluates against objects that conform to the [`XCUIElementAttributes`](../xcuielementattributes.md) protocol.

> **Note**:  Where possible, use [`NSExpression`](../../Foundation/nsexpression.md)-based or format-string-based predicates with this method in preference to block-based predicates. This enables the framework to optimize the query’s performance.

## Parameters

- `predicate`: The predicate used to evaluate each descendant element.

## See Also

### Creating new queries
- [func children(matching: XCUIElement.ElementType) -> XCUIElementQuery](./children%28matching%29.md)
  Returns a new query that matches all direct children of the requested type.
- [func descendants(matching: XCUIElement.ElementType) -> XCUIElementQuery](./descendants%28matching%29.md)
  Returns a new query that matches all descendants of the requested type.
- [func containing(XCUIElement.ElementType, identifier: String?) -> XCUIElementQuery](./containing%28_,identifier%29.md)
  Returns a new query that matches elements that contain a descendant of the requested type and an identifying property that matches a provided identifier.
- [func matching(identifier: String) -> XCUIElementQuery](./matching%28identifier%29.md)
  Returns a new query that matches elements that have an identifying property that matches a provided identifier.
- [func matching(NSPredicate) -> XCUIElementQuery](./matching%28_%29.md)
  Returns a new query that matches elements that meet the logical conditions of the provided predicate.
- [func matching(XCUIElement.ElementType, identifier: String?) -> XCUIElementQuery](./matching%28_,identifier%29.md)
  Returns a new query that matches elements of the requested type and have an identifying property that matches a provided identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielementquery/containing(_:))*