# waitForNonExistence(timeout:)

**Framework**: XCUIAutomation  
**Kind**: method  
**Role**: Instance Method

Waits the specified amount of time for an element to no longer exist.

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
func waitForNonExistence(timeout: TimeInterval) -> Bool
```

```objc
- (BOOL) waitForNonExistenceWithTimeout:(NSTimeInterval) timeout;
```

## Discussion

## Parameters

- `timeout`: The time, in seconds, the test allows for the element to become unavailable. The default timeout allows the test to run until it reaches its execution time allowance.

## See Also

### Querying element state
- [func waitForExistence(timeout: TimeInterval) -> Bool](./waitforexistence%28timeout%29.md)
  Waits the specified amount of time for an element to exist.
- [func wait<V>(for: KeyPath<XCUIElement, V>, toEqual: V, timeout: TimeInterval) -> Bool](./wait%28for,toequal,timeout%29.md)
  Waits a specified amount of time for a property value to equal a specified value.
- [var exists: Bool](./exists.md)
  Determines if the element exists.
- [var isHittable: Bool](./ishittable.md)
  Determines if the system can compute a hit point for the element.
- [var debugDescription: String](./debugdescription.md)
  Provides debugging information about the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/waitfornonexistence(timeout:))*