# debugDescription

**Framework**: XCUIAutomation  
**Kind**: property  
**Role**: Instance Property

Provides debugging information about the element.

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
var debugDescription: String { get }
```

```objc
@property (copy, readonly) NSString * debugDescription;
```

#### Discussion

The data in the string varies based on the time at which it’s captured, but it may include any of the following, as well as additional data:

- Values for the element’s attributes
- The entire tree of descendants rooted at the element
- The element’s query

Use this data for debugging only. Depending on any of the data as part of a test is unsupported.

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
- [var isHittable: Bool](./ishittable.md)
  Determines if the system can compute a hit point for the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/debugdescription)*