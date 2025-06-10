# descendants(matching:)

**Framework**: XCUIAutomation  
**Kind**: method

Returns a query for all descendants of the element matching the type you specify.

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
func descendants(matching type: XCUIElement.ElementType) -> XCUIElementQuery
```

#### Discussion

Because [`XCUIElement`](xcuielement.md) conforms to the [`XCUIElementTypeQueryProvider`](xcuielementtypequeryprovider.md) protocol, you can use the protocol’s properties as shorthand for calling [`descendants(matching:)`](xcuielement/descendants(matching:).md) for different element types. For example, rather than calling `table.descendants(matching: .cell)`, you can use the [`cells`](xcuielementtypequeryprovider/cells.md) property from the protocol to retrieve `table.cells`.

## See Also

- [func children(matching: XCUIElement.ElementType) -> XCUIElementQuery](xcuielement/children(matching:).md)
  Returns a query for all direct children of the element matching the type you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/descendants(matching:))*