# expectedValue

**Framework**: Xctest  
**Kind**: property

A value that the key path’s specified property must equal to fulfill the expectation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+

## Declaration

```swift
final var expectedValue: V? { get }
```

#### Discussion

If the expectation doesn’t initialize with an expected value, this property returns `nil`.

## See Also

- [let keyPath: KeyPath<T, V>](xctkeypathexpectation/keypath.md)
  The key path for the observed property, relative to the observed object.
- [let observedObject: T](xctkeypathexpectation/observedobject.md)
  The object the system observes the key path on.
- [let options: NSKeyValueObservingOptions](xctkeypathexpectation/options.md)
  A combination of values that specify what to include in observation notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctkeypathexpectation/expectedvalue)*