# XCTKVOExpectation.Handler

**Framework**: XCTest  
**Kind**: typealias  
**Role**: Type Alias

A custom handler to call when observing a KVO change for a specified key path.

## Declaration

```swift
typealias Handler = @Sendable (Any, [AnyHashable : Any]) -> Bool
```

```c
typedef _Bool (^)(id, NSDictionary *) XCKeyValueObservingExpectationHandler;
```

## Return Value

Your custom handler returns [`true`](../../Swift/true.md) if the system fulfills the expectation after the observed change; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `observedObject`: The observed object, which helps to avoid block-capture issues.
- `change`: The KVO change dictionary.

## See Also

### Custom KVO evaluation
- [var handler: XCTKVOExpectation.Handler?](./handler-swift.property.md)
  An optional handler that performs custom evaluation of changes to the observed key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctkvoexpectation/handler-swift.typealias)*