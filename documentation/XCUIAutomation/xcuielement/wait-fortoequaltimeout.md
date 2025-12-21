# wait(for:toEqual:timeout:)

**Framework**: XCUIAutomation  
**Kind**: method

Waits a specified amount of time for a property value to equal a specified value.

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
@preconcurrency func wait<V>(for keyPath: KeyPath<XCUIElement, V>, toEqual expectedValue: V, timeout: TimeInterval) -> Bool where V : Equatable
```

#### Discussion

This method returns [`false`](https://developer.apple.com/documentation/Swift/false) if the timeout expires before the observed property equals the expected value.

## Parameters

- `keyPath`: The observed property on an  .
- `expectedValue`: The desired value, which must conform to  .
- `timeout`: The length of time in seconds to wait for the observed property to equal the expected value.

## See Also

- [func waitForExistence(timeout: TimeInterval) -> Bool](xcuielement/waitforexistence(timeout:).md)
  Waits the specified amount of time for an element to exist.
- [func waitForNonExistence(timeout: TimeInterval) -> Bool](xcuielement/waitfornonexistence(timeout:).md)
  Waits the specified amount of time for an element to no longer exist.
- [var exists: Bool](xcuielement/exists.md)
  Determines if the element exists.
- [var isHittable: Bool](xcuielement/ishittable.md)
  Determines if the system can compute a hit point for the element.
- [var debugDescription: String](xcuielement/debugdescription.md)
  Provides debugging information about the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/wait(for:toequal:timeout:))*