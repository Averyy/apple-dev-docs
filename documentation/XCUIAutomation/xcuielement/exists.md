# exists

**Framework**: Xcuiautomation  
**Kind**: property

Determines if the element exists.

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
var exists: Bool { get }
```

#### Discussion

This property determines if the element exists within the app’s current UI hierarchy.

> **Note**:  The fact that an element exists doesn’t imply that it’s hittable. Elements can exist offscreen, or exist onscreen but be hidden by another element, causing their [`isHittable`](xcuielement/ishittable.md) property to return false.

## See Also

- [func waitForExistence(timeout: TimeInterval) -> Bool](xcuielement/waitforexistence(timeout:).md)
  Waits the specified amount of time for an element to exist.
- [func waitForNonExistence(timeout: TimeInterval) -> Bool](xcuielement/waitfornonexistence(timeout:).md)
  Waits the specified amount of time for an element to no longer exist.
- [func wait<V>(for: KeyPath<XCUIElement, V>, toEqual: V, timeout: TimeInterval) -> Bool](xcuielement/wait(for:toequal:timeout:).md)
  Waits a specified amount of time for a property value to equal a specified value.
- [var isHittable: Bool](xcuielement/ishittable.md)
  Determines if the system can compute a hit point for the element.
- [var debugDescription: String](xcuielement/debugdescription.md)
  Provides debugging information about the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/exists)*