# exists

**Framework**: XCUIAutomation  
**Kind**: property  
**Role**: Instance Property

Determines if the element exists.

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
var exists: Bool { get }
```

```objc
@property (readonly) BOOL exists;
```

## Discussion

This property determines if the element exists within the app’s current UI hierarchy.

> **Note**:  The fact that an element exists doesn’t imply that it’s hittable. Elements can exist offscreen, or exist onscreen but be hidden by another element, causing their [`isHittable`](./ishittable.md) property to return false.

## See Also

### Querying element state
- [func waitForExistence(timeout: TimeInterval) -> Bool](./waitforexistence%28timeout%29.md)
  Waits the specified amount of time for an element to exist.
- [func waitForNonExistence(timeout: TimeInterval) -> Bool](./waitfornonexistence%28timeout%29.md)
  Waits the specified amount of time for an element to no longer exist.
- [func wait<V>(for: KeyPath<XCUIElement, V>, toEqual: V, timeout: TimeInterval) -> Bool](./wait%28for,toequal,timeout%29.md)
  Waits a specified amount of time for a property value to equal a specified value.
- [var isHittable: Bool](./ishittable.md)
  Determines if the system can compute a hit point for the element.
- [var debugDescription: String](./debugdescription.md)
  Provides debugging information about the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/exists)*