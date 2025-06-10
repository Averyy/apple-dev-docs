# containing(_:identifier:)

**Framework**: XCUIAutomation  
**Kind**: method

Returns a new query that matches elements that contain a descendant of the requested type and an identifying property that matches a provided identifier.

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
func containing(_ elementType: XCUIElement.ElementType, identifier: String?) -> XCUIElementQuery
```

#### Return Value

A new query that defines a search that extends the search criteria of the receiver. The new search finds elements that match the original search and contain elements of the requested type that have an identifying property that matches a provided identifier. For the list of the types, see [`XCUIElement.ElementType`](xcuielement/elementtype.md).

## Parameters

- `elementType`: The contained element type to match.
- `identifier`: An optional string to match against the contained element’s identifying properties:  ,  ,  ,  , or  .

## See Also

- [func children(matching: XCUIElement.ElementType) -> XCUIElementQuery](xcuielementquery/children(matching:).md)
  Returns a new query that matches all direct children of the requested type.
- [func descendants(matching: XCUIElement.ElementType) -> XCUIElementQuery](xcuielementquery/descendants(matching:).md)
  Returns a new query that matches all descendants of the requested type.
- [func containing(NSPredicate) -> XCUIElementQuery](xcuielementquery/containing(_:).md)
  Returns a new query that matches elements containing a descendant that meets the logical conditions of the provided predicate.
- [func matching(identifier: String) -> XCUIElementQuery](xcuielementquery/matching(identifier:).md)
  Returns a new query that matches elements that have an identifying property that matches a provided identifier.
- [func matching(NSPredicate) -> XCUIElementQuery](xcuielementquery/matching(_:).md)
  Returns a new query that matches elements that meet the logical conditions of the provided predicate.
- [func matching(XCUIElement.ElementType, identifier: String?) -> XCUIElementQuery](xcuielementquery/matching(_:identifier:).md)
  Returns a new query that matches elements of the requested type and have an identifying property that matches a provided identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielementquery/containing(_:identifier:))*