# options

**Framework**: XCTest  
**Kind**: property  
**Role**: Instance Property

The key-value observing options the expectation uses when registering for observation.

**Availability**:
- iOS - Deprecated in 17.0
- iPadOS - Deprecated in 17.0
- Mac Catalyst - Deprecated in 17.0
- macOS - Deprecated in 27.0
- tvOS - Deprecated in 17.0
- visionOS - Deprecated in 1.0
- watchOS - Deprecated in 26.0

> **Deprecated**: Replaced by 'XCTKeyPathExpectation'

## Declaration

```swift
var options: NSKeyValueObservingOptions { get }
```

```objc
@property (readonly) NSKeyValueObservingOptions options;
```

## See Also

### Expectation properties
- [var keyPath: String](./keypath.md)
  The key path the system observes for KVO changes.
- [var observedObject: Any](./observedobject.md)
  The object that the system observes for KVO changes.
- [var expectedValue: Any?](./expectedvalue.md)
  The value that the key path’s specified property must equal to fulfill the expectation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctkvoexpectation/options)*