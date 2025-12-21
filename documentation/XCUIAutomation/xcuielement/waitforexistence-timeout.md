# waitForExistence(timeout:)

**Framework**: XCUIAutomation  
**Kind**: method

Waits the specified amount of time for an element to exist.

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
func waitForExistence(timeout: TimeInterval) -> Bool
```

#### Discussion

Returns [`false`](https://developer.apple.com/documentation/Swift/false) if the timeout expires while the element’s [`exists`](xcuielement/exists.md) property equals [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func waitForNonExistence(timeout: TimeInterval) -> Bool](xcuielement/waitfornonexistence(timeout:).md)
  Waits the specified amount of time for an element to no longer exist.
- [func wait<V>(for: KeyPath<XCUIElement, V>, toEqual: V, timeout: TimeInterval) -> Bool](xcuielement/wait(for:toequal:timeout:).md)
  Waits a specified amount of time for a property value to equal a specified value.
- [var exists: Bool](xcuielement/exists.md)
  Determines if the element exists.
- [var isHittable: Bool](xcuielement/ishittable.md)
  Determines if the system can compute a hit point for the element.
- [var debugDescription: String](xcuielement/debugdescription.md)
  Provides debugging information about the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/waitforexistence(timeout:))*