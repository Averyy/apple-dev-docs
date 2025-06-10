# children(matching:)

**Framework**: XCUIAutomation  
**Kind**: method

Returns a new query that matches all direct children of the requested type.

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
func children(matching type: XCUIElement.ElementType) -> XCUIElementQuery
```

#### Return Value

A new query that defines a search that extends the search criteria of the receiver. The new search finds all direct children of elements that match the original search and are of the requested type. For a list of the types, see [`XCUIElement.ElementType`](xcuielement/elementtype.md).

#### Discussion

If you need to match all descendants including elements that aren’t direct child elements, use the [`descendants(matching:)`](xcuielementquery/descendants(matching:).md) method.

## Parameters

- `type`: The element type to match.

## See Also

- [func descendants(matching: XCUIElement.ElementType) -> XCUIElementQuery](xcuielementquery/descendants(matching:).md)
  Returns a new query that matches all descendants of the requested type.
- [func containing(NSPredicate) -> XCUIElementQuery](xcuielementquery/containing(_:).md)
  Returns a new query that matches elements containing a descendant that meets the logical conditions of the provided predicate.
- [func containing(XCUIElement.ElementType, identifier: String?) -> XCUIElementQuery](xcuielementquery/containing(_:identifier:).md)
  Returns a new query that matches elements that contain a descendant of the requested type and an identifying property that matches a provided identifier.
- [func matching(identifier: String) -> XCUIElementQuery](xcuielementquery/matching(identifier:).md)
  Returns a new query that matches elements that have an identifying property that matches a provided identifier.
- [func matching(NSPredicate) -> XCUIElementQuery](xcuielementquery/matching(_:).md)
  Returns a new query that matches elements that meet the logical conditions of the provided predicate.
- [func matching(XCUIElement.ElementType, identifier: String?) -> XCUIElementQuery](xcuielementquery/matching(_:identifier:).md)
  Returns a new query that matches elements of the requested type and have an identifying property that matches a provided identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielementquery/children(matching:))*