# init(keyPath:object:)

**Framework**: XCTest  
**Kind**: init

Creates an expectation that any KVO change to the specified key path of the observed object fulfills.

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
convenience init(keyPath: String, object: Any)
```

#### Discussion

This initializer sets up KVO observation for `keyPath` with the following [`NSKeyValueObservingOptions`](https://developer.apple.com/documentation/Foundation/NSKeyValueObservingOptions):

- [`new`](https://developer.apple.com/documentation/Foundation/NSKeyValueObservingOptions/new)
- [`old`](https://developer.apple.com/documentation/Foundation/NSKeyValueObservingOptions/old)

The inclusion of the [`new`](https://developer.apple.com/documentation/Foundation/NSKeyValueObservingOptions/new) and [`old`](https://developer.apple.com/documentation/Foundation/NSKeyValueObservingOptions/old) options means that any custom KVO handler you provide in the expectation’s [`handler`](xctkvoexpectation/handler-swift.property.md) property receives a change info dictionary that contains the [`newKey`](https://developer.apple.com/documentation/Foundation/NSKeyValueChangeKey/newKey) and [`oldKey`](https://developer.apple.com/documentation/Foundation/NSKeyValueChangeKey/oldKey) keys.

## Parameters

- `keyPath`: The key path to observe.
- `object`: The object to observe.

## See Also

- [convenience init(keyPath: String, object: Any, expectedValue: Any?)](xctkvoexpectation/init(keypath:object:expectedvalue:).md)
  Creates an expectation a KVO change fulfills when it causes the specified key path of the observed object to have an expected value.
- [init(keyPath: String, object: Any, expectedValue: Any?, options: NSKeyValueObservingOptions)](xctkvoexpectation/init(keypath:object:expectedvalue:options:).md)
  Creates an expectation with custom observation options that a KVO change fulfills when it causes the specified key path of the observed object to have an expected value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctkvoexpectation/init(keypath:object:))*