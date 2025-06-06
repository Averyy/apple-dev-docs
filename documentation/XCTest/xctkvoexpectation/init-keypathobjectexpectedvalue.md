# init(keyPath:object:expectedValue:)

**Framework**: Xctest  
**Kind**: init

Creates an expectation a KVO change fulfills when it causes the specified key path of the observed object to have an expected value.

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
convenience init(keyPath: String, object: Any, expectedValue: Any?)
```

#### Discussion

This initializer sets up KVO observation for `keyPath` with the following [`NSKeyValueObservingOptions`](https://developer.apple.com/documentation/Foundation/NSKeyValueObservingOptions):

- [`initial`](https://developer.apple.com/documentation/foundation/nskeyvalueobservingoptions/1413959-initial)
- [`new`](https://developer.apple.com/documentation/foundation/nskeyvalueobservingoptions/1417881-new)
- [`old`](https://developer.apple.com/documentation/foundation/nskeyvalueobservingoptions/1414041-old)

The inclusion of the [`initial`](https://developer.apple.com/documentation/foundation/nskeyvalueobservingoptions/1413959-initial) option means that the system checks the observed key path immediately after initialization. The inclusion of the [`new`](https://developer.apple.com/documentation/foundation/nskeyvalueobservingoptions/1417881-new) and [`old`](https://developer.apple.com/documentation/foundation/nskeyvalueobservingoptions/1414041-old) options means that any custom KVO handler you provide in the expectation’s [`handler`](xctkvoexpectation/handler-swift.property.md) property receives a change info dictionary that contains the [`newKey`](https://developer.apple.com/documentation/foundation/nskeyvaluechangekey/1416259-newkey) and [`oldKey`](https://developer.apple.com/documentation/foundation/nskeyvaluechangekey/1415014-oldkey) keys.

## Parameters

- `keyPath`: The key path to observe.
- `object`: The object to observe.
- `expectedValue`: The expected value for the observed key path.

## See Also

- [convenience init(keyPath: String, object: Any)](xctkvoexpectation/init(keypath:object:).md)
  Creates an expectation that any KVO change to the specified key path of the observed object fulfills.
- [init(keyPath: String, object: Any, expectedValue: Any?, options: NSKeyValueObservingOptions)](xctkvoexpectation/init(keypath:object:expectedvalue:options:).md)
  Creates an expectation with custom observation options that a KVO change fulfills when it causes the specified key path of the observed object to have an expected value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctkvoexpectation/init(keypath:object:expectedvalue:))*