# keyPath

**Framework**: XCTest  
**Kind**: property  
**Role**: Instance Property

The key path for the observed property, relative to the observed object.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+

## Declaration

```swift
final let keyPath: KeyPath<T, V>
```

## See Also

### Expectation properties
- [let observedObject: T](./observedobject.md)
  The object the system observes the key path on.
- [let options: NSKeyValueObservingOptions](./options.md)
  A combination of values that specify what to include in observation notifications.
- [var expectedValue: V?](./expectedvalue.md)
  A value that the key path’s specified property must equal to fulfill the expectation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctkeypathexpectation/keypath)*