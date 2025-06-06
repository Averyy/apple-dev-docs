# observedObject

**Framework**: Xctest  
**Kind**: property

The object that the system observes for KVO changes.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var observedObject: Any { get }
```

## See Also

- [var keyPath: String](xctkvoexpectation/keypath.md)
  The key path the system observes for KVO changes.
- [var expectedValue: Any?](xctkvoexpectation/expectedvalue.md)
  The value that the key path’s specified property must equal to fulfill the expectation.
- [var options: NSKeyValueObservingOptions](xctkvoexpectation/options.md)
  The key-value observing options the expectation uses when registering for observation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctkvoexpectation/observedobject)*