# init(predicate:object:)

**Framework**: Xctest  
**Kind**: init

Creates an expectation that’s fulfilled when an `NSPredicate` instance returns `true`, optionally for a provided object.

## Declaration

```swift
init(predicate: NSPredicate, object: Any?)
```

#### Discussion

When you use an instance of this class from Swift and await using [`fulfillment(of:timeout:enforceOrder:)`](xctestcase/fulfillment(of:timeout:enforceorder:).md) rather than [`wait(for:)`](xctestcase/wait(for:).md), XCTest evaluates `predicate` on the main actor.

## Parameters

- `predicate`: The predicate to evaluate.
- `object`: An optional object XCTest evaluates the predicate against.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctnspredicateexpectation/init(predicate:object:))*