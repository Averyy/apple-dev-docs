# element(matching:)

**Framework**: XCUIAutomation  
**Kind**: method  
**Role**: Instance Method

Matches the predicate.

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
func element(matching predicate: NSPredicate) -> XCUIElement
```

```objc
- (XCUIElement *) elementMatchingPredicate:(NSPredicate *) predicate;
```

#### Discussion

The predicate evaluates against objects that conform to the [`XCUIElementAttributes`](../xcuielementattributes.md) protocol.

> **Note**:  Where possible, use [`NSExpression`](../../Foundation/nsexpression.md)-based or format-string-based predicates with this method in preference to block-based predicates. This enables the framework to optimize the query’s performance.

## Parameters

- `predicate`: The predicate to match.

## See Also

### Accessing matched elements
- [var allElementsBoundByAccessibilityElement: [XCUIElement]](./allelementsboundbyaccessibilityelement.md)
  Immediately evaluates the query and returns an array of elements bound to the resulting accessibility elements.
- [var allElementsBoundByIndex: [XCUIElement]](./allelementsboundbyindex.md)
  Immediately evaluates the query and returns an array of elements bound by the index of each result.
- [var count: Int](./count.md)
  Evaluates the query and returns the number of elements that match.
- [var element: XCUIElement](./element.md)
  The query’s single matching element.
- [func element(boundBy: Int) -> XCUIElement](./element%28boundby%29.md)
  Uses an index into the query’s results to determine which underlying accessibility element to use.
- [func element(matching: XCUIElement.ElementType, identifier: String?) -> XCUIElement](./element%28matching,identifier%29.md)
  Matches the provided element type and identifier.
- [subscript(String) -> XCUIElement](./subscript%28_%29.md)
  Returns a descendant element that matches a provided identifier.
- [func element(at: Int) -> XCUIElement](./element%28at%29.md)
  Returns an element that resolves to the index into the query’s result set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielementquery/element(matching:))*