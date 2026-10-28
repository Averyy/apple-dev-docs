# waitForExistence(timeout:)

**Framework**: XCUIAutomation  
**Kind**: method  
**Role**: Instance Method

Waits the specified amount of time for an element to exist.

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
func waitForExistence(timeout: TimeInterval) -> Bool
```

```objc
- (BOOL) waitForExistenceWithTimeout:(NSTimeInterval) timeout;
```

## Discussion

Returns [`false`](../../Swift/false.md) if the timeout expires while the element’s [`exists`](./exists.md) property equals [`false`](../../Swift/false.md).

## See Also

### Querying element state
- [func waitForNonExistence(timeout: TimeInterval) -> Bool](./waitfornonexistence%28timeout%29.md)
  Waits the specified amount of time for an element to no longer exist.
- [func wait<V>(for: KeyPath<XCUIElement, V>, toEqual: V, timeout: TimeInterval) -> Bool](./wait%28for,toequal,timeout%29.md)
  Waits a specified amount of time for a property value to equal a specified value.
- [var exists: Bool](./exists.md)
  Determines if the element exists.
- [var isHittable: Bool](./ishittable.md)
  Determines if the system can compute a hit point for the element.
- [var debugDescription: String](./debugdescription.md)
  Provides debugging information about the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/waitforexistence(timeout:))*