# debugDescription

**Framework**: Xcuiautomation  
**Kind**: property

Provides debugging information about the element.

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
var debugDescription: String { get }
```

#### Discussion

The data in the string varies based on the time at which it’s captured, but it may include any of the following, as well as additional data:

- Values for the element’s attributes
- The entire tree of descendants rooted at the element
- The element’s query

Use this data for debugging only. Depending on any of the data as part of a test is unsupported.

## See Also

- [func waitForExistence(timeout: TimeInterval) -> Bool](xcuielement/waitforexistence(timeout:).md)
  Waits the specified amount of time for an element to exist.
- [func waitForNonExistence(timeout: TimeInterval) -> Bool](xcuielement/waitfornonexistence(timeout:).md)
  Waits the specified amount of time for an element to no longer exist.
- [func wait<V>(for: KeyPath<XCUIElement, V>, toEqual: V, timeout: TimeInterval) -> Bool](xcuielement/wait(for:toequal:timeout:).md)
  Waits a specified amount of time for a property value to equal a specified value.
- [var exists: Bool](xcuielement/exists.md)
  Determines if the element exists.
- [var isHittable: Bool](xcuielement/ishittable.md)
  Determines if the system can compute a hit point for the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/debugdescription)*