# wait(for:toEqual:timeout:)

**Framework**: XCUIAutomation  
**Kind**: method  
**Role**: Instance Method

Waits a specified amount of time for a property value to equal a specified value.

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
@MainActor
@preconcurrency func wait<V>(for keyPath: KeyPath<XCUIElement, V>, toEqual expectedValue: V, timeout: TimeInterval) -> Bool where V : Equatable
```

## Discussion

This method returns [`false`](../../Swift/false.md) if the timeout expires before the observed property equals the expected value.

## Parameters

- `keyPath`: The observed property on an [`XCUIElement`](../xcuielement.md).
- `expectedValue`: The desired value, which must conform to `Equatable`.
- `timeout`: The length of time in seconds to wait for the observed property to equal the expected value.

## See Also

### Querying element state
- [func waitForExistence(timeout: TimeInterval) -> Bool](./waitforexistence%28timeout%29.md)
  Waits the specified amount of time for an element to exist.
- [func waitForNonExistence(timeout: TimeInterval) -> Bool](./waitfornonexistence%28timeout%29.md)
  Waits the specified amount of time for an element to no longer exist.
- [var exists: Bool](./exists.md)
  Determines if the element exists.
- [var isHittable: Bool](./ishittable.md)
  Determines if the system can compute a hit point for the element.
- [var debugDescription: String](./debugdescription.md)
  Provides debugging information about the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/wait(for:toequal:timeout:))*