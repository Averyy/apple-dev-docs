# init(keyPath:object:expectedValue:options:)

**Framework**: Xctest  
**Kind**: init

Creates an expectation with custom observation options that a KVO change fulfills when it causes the specified key path of the observed object to have an expected value.

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
init(keyPath: String, object: Any, expectedValue: Any?, options: NSKeyValueObservingOptions = [])
```

## Parameters

- `keyPath`: The key path to observe.
- `object`: The object to observe.
- `expectedValue`: The expected value for the observed key path.
- `options`: An array of   that determine the values to return as part of the observed key path’s change dictionary.

## See Also

- [convenience init(keyPath: String, object: Any)](xctkvoexpectation/init(keypath:object:).md)
  Creates an expectation that any KVO change to the specified key path of the observed object fulfills.
- [convenience init(keyPath: String, object: Any, expectedValue: Any?)](xctkvoexpectation/init(keypath:object:expectedvalue:).md)
  Creates an expectation a KVO change fulfills when it causes the specified key path of the observed object to have an expected value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctkvoexpectation/init(keypath:object:expectedvalue:options:))*