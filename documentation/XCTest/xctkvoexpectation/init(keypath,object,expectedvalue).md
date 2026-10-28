# init(keyPath:object:expectedValue:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Creates an expectation a KVO change fulfills when it causes the specified key path of the observed object to have an expected value.

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
convenience init(keyPath: String, object: Any, expectedValue: Any?)
```

```objc
- (instancetype) initWithKeyPath:(NSString *) keyPath object:(id) object expectedValue:(id) expectedValue;
```

## Discussion

This initializer sets up KVO observation for `keyPath` with the following [`NSKeyValueObservingOptions`](../../Foundation/nskeyvalueobservingoptions.md):

- [`initial`](../../Foundation/nskeyvalueobservingoptions/initial.md)
- [`new`](../../Foundation/nskeyvalueobservingoptions/new.md)
- [`old`](../../Foundation/nskeyvalueobservingoptions/old.md)

The inclusion of the [`initial`](../../Foundation/nskeyvalueobservingoptions/initial.md) option means that the system checks the observed key path immediately after initialization. The inclusion of the [`new`](../../Foundation/nskeyvalueobservingoptions/new.md) and [`old`](../../Foundation/nskeyvalueobservingoptions/old.md) options means that any custom KVO handler you provide in the expectation’s [`handler`](./handler-swift.property.md) property receives a change info dictionary that contains the [`newKey`](../../Foundation/nskeyvaluechangekey/newkey.md) and [`oldKey`](../../Foundation/nskeyvaluechangekey/oldkey.md) keys.

## Parameters

- `keyPath`: The key path to observe.
- `object`: The object to observe.
- `expectedValue`: The expected value for the observed key path.

## See Also

### Creating KVO expectations
- [convenience init(keyPath: String, object: Any)](./init%28keypath,object%29.md)
  Creates an expectation that any KVO change to the specified key path of the observed object fulfills.
- [init(keyPath: String, object: Any, expectedValue: Any?, options: NSKeyValueObservingOptions)](./init%28keypath,object,expectedvalue,options%29.md)
  Creates an expectation with custom observation options that a KVO change fulfills when it causes the specified key path of the observed object to have an expected value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctkvoexpectation/init(keypath:object:expectedvalue:))*