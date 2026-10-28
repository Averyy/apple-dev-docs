# init(predicate:object:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Creates an expectation that’s fulfilled when an `NSPredicate` instance returns `true`, optionally for a provided object.

## Declaration

```swift
init(predicate: NSPredicate, object: Any?)
```

```objc
- (instancetype) initWithPredicate:(NSPredicate *) predicate object:(id) object;
```

## Discussion

When you use an instance of this class from Swift and await using [`fulfillment(of:timeout:enforceOrder:)`](../xctestcase/fulfillment%28of,timeout,enforceorder%29.md) rather than [`wait(for:)`](../xctestcase/wait%28for%29.md), XCTest evaluates `predicate` on the main actor.

## Parameters

- `predicate`: The predicate to evaluate.
- `object`: An optional object XCTest evaluates the predicate against.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctnspredicateexpectation/init(predicate:object:))*