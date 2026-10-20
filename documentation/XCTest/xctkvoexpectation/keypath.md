# keyPath

**Framework**: XCTest  
**Kind**: property  
**Role**: Instance Property

The key path the system observes for KVO changes.

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
var keyPath: String { get }
```

```objc
@property (copy, readonly) NSString * keyPath;
```

## See Also

### Expectation properties
- [var observedObject: Any](./observedobject.md)
  The object that the system observes for KVO changes.
- [var expectedValue: Any?](./expectedvalue.md)
  The value that the key path’s specified property must equal to fulfill the expectation.
- [var options: NSKeyValueObservingOptions](./options.md)
  The key-value observing options the expectation uses when registering for observation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctkvoexpectation/keypath)*