# children(matching:)

**Framework**: XCUIAutomation  
**Kind**: method  
**Role**: Instance Method

Returns a query for all direct children of the element matching the type you specify.

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
func children(matching type: XCUIElement.ElementType) -> XCUIElementQuery
```

```objc
- (XCUIElementQuery *) childrenMatchingType:(XCUIElementType) type;
```

## See Also

### Querying descendant elements
- [func descendants(matching: XCUIElement.ElementType) -> XCUIElementQuery](./descendants%28matching%29.md)
  Returns a query for all descendants of the element matching the type you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/children(matching:))*