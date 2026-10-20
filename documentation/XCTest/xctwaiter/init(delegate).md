# init(delegate:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Creates a new waiter with the specified delegate.

## Declaration

```swift
init(delegate: (any XCTWaiterDelegate)?)
```

```objc
- (instancetype) initWithDelegate:(id<XCTWaiterDelegate>) delegate;
```

## Parameters

- `delegate`: The [`XCTWaiterDelegate`](../xctwaiterdelegate.md) that wait events should be sent to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctwaiter/init(delegate:))*