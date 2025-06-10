# options

**Framework**: XCTest  
**Kind**: property

A combination of values that specify what to include in observation notifications.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+

## Declaration

```swift
final let options: NSKeyValueObservingOptions
```

#### Discussion

For possible values, see [`NSKeyValueObservingOptions`](https://developer.apple.com/documentation/Foundation/NSKeyValueObservingOptions).

## See Also

- [let keyPath: KeyPath<T, V>](xctkeypathexpectation/keypath.md)
  The key path for the observed property, relative to the observed object.
- [let observedObject: T](xctkeypathexpectation/observedobject.md)
  The object the system observes the key path on.
- [var expectedValue: V?](xctkeypathexpectation/expectedvalue.md)
  A value that the key path’s specified property must equal to fulfill the expectation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctkeypathexpectation/options)*