# XCTKVOExpectation.Handler

**Framework**: Xctest  
**Kind**: typealias

A custom handler to call when observing a KVO change for a specified key path.

## Declaration

```swift
typealias Handler = (Any, [AnyHashable : Any]) -> Bool
```

#### Return Value

Your custom handler returns [`true`](https://developer.apple.com/documentation/swift/true) if the system fulfills the expectation after the observed change; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `observedObject`: The observed object, which helps to avoid block-capture issues.
- `change`: The KVO change dictionary.

## See Also

- [var handler: XCTKVOExpectation.Handler?](xctkvoexpectation/handler-swift.property.md)
  An optional handler that performs custom evaluation of changes to the observed key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctkvoexpectation/handler-swift.typealias)*