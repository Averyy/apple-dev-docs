# isHittable

**Framework**: Xcuiautomation  
**Kind**: property

Determines if the system can compute a hit point for the element.

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
var isHittable: Bool { get }
```

#### Discussion

[`isHittable`](xcuielement/ishittable.md) returns [`true`](https://developer.apple.com/documentation/swift/true) if the element exists and can be clicked, tapped, or pressed at its current location. It returns [`false`](https://developer.apple.com/documentation/swift/false) if the element doesn’t exist, is offscreen, or is covered by another element.

> **Note**:  [`isHittable`](xcuielement/ishittable.md) only returns [`true`](https://developer.apple.com/documentation/swift/true) if the element is already visible and hittable onscreen. It returns [`false`](https://developer.apple.com/documentation/swift/false) for an offscreen element in a scrollable view, even if the element can be scrolled into a hittable position by calling [`click()`](xcuielement/click().md), [`tap()`](xcuielement/tap().md), or another hit-point-related interaction method.

 [`isHittable`](xcuielement/ishittable.md) only returns [`true`](https://developer.apple.com/documentation/swift/true) if the element is already visible and hittable onscreen. It returns [`false`](https://developer.apple.com/documentation/swift/false) for an offscreen element in a scrollable view, even if the element can be scrolled into a hittable position by calling [`click()`](xcuielement/click().md), [`tap()`](xcuielement/tap().md), or another hit-point-related interaction method.

## See Also

- [func waitForExistence(timeout: TimeInterval) -> Bool](xcuielement/waitforexistence(timeout:).md)
  Waits the specified amount of time for an element to exist.
- [func waitForNonExistence(timeout: TimeInterval) -> Bool](xcuielement/waitfornonexistence(timeout:).md)
  Waits the specified amount of time for an element to no longer exist.
- [func wait<V>(for: KeyPath<XCUIElement, V>, toEqual: V, timeout: TimeInterval) -> Bool](xcuielement/wait(for:toequal:timeout:).md)
  Waits a specified amount of time for a property value to equal a specified value.
- [var exists: Bool](xcuielement/exists.md)
  Determines if the element exists.
- [var debugDescription: String](xcuielement/debugdescription.md)
  Provides debugging information about the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/ishittable)*