# init(keyPath:object:expectedValue:options:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Creates an expectation with custom observation options that a KVO change fulfills when it causes the specified key path of the observed object to have an expected value.

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
init(keyPath: String, object: Any, expectedValue: Any?, options: NSKeyValueObservingOptions = [])
```

```objc
- (instancetype) initWithKeyPath:(NSString *) keyPath object:(id) object expectedValue:(id) expectedValue options:(NSKeyValueObservingOptions) options;
```

## Parameters

- `keyPath`: The key path to observe.
- `object`: The object to observe.
- `expectedValue`: The expected value for the observed key path.
- `options`: An array of [`NSKeyValueObservingOptions`](../../Foundation/nskeyvalueobservingoptions.md) that determine the values to return as part of the observed key path’s change dictionary.

## See Also

### Creating KVO expectations
- [convenience init(keyPath: String, object: Any)](./init%28keypath,object%29.md)
  Creates an expectation that any KVO change to the specified key path of the observed object fulfills.
- [convenience init(keyPath: String, object: Any, expectedValue: Any?)](./init%28keypath,object,expectedvalue%29.md)
  Creates an expectation a KVO change fulfills when it causes the specified key path of the observed object to have an expected value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctkvoexpectation/init(keypath:object:expectedvalue:options:))*