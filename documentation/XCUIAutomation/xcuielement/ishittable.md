# isHittable

**Framework**: XCUIAutomation  
**Kind**: property  
**Role**: Instance Property

Determines if the system can compute a hit point for the element.

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
var isHittable: Bool { get }
```

```objc
@property (readonly, getter=isHittable) BOOL hittable;
```

#### Discussion

[`isHittable`](./ishittable.md) returns [`true`](../../Swift/true.md) if the element exists and can be clicked, tapped, or pressed at its current location. It returns [`false`](../../Swift/false.md) if the element doesn’t exist, is offscreen, or is covered by another element.

> **Note**:  [`isHittable`](./ishittable.md) only returns [`true`](../../Swift/true.md) if the element is already visible and hittable onscreen. It returns [`false`](../../Swift/false.md) for an offscreen element in a scrollable view, even if the element can be scrolled into a hittable position by calling [`click()`](./click%28%29.md), [`tap()`](./tap%28%29.md), or another hit-point-related interaction method.

## See Also

### Querying element state
- [func waitForExistence(timeout: TimeInterval) -> Bool](./waitforexistence%28timeout%29.md)
  Waits the specified amount of time for an element to exist.
- [func waitForNonExistence(timeout: TimeInterval) -> Bool](./waitfornonexistence%28timeout%29.md)
  Waits the specified amount of time for an element to no longer exist.
- [func wait<V>(for: KeyPath<XCUIElement, V>, toEqual: V, timeout: TimeInterval) -> Bool](./wait%28for,toequal,timeout%29.md)
  Waits a specified amount of time for a property value to equal a specified value.
- [var exists: Bool](./exists.md)
  Determines if the element exists.
- [var debugDescription: String](./debugdescription.md)
  Provides debugging information about the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/ishittable)*