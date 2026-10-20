# delegate

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The delegate of the WatchKit app object.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
weak var delegate: (any WKApplicationDelegate)? { get }
```

```objc
@property (nonatomic, weak, readonly, nullable) id<WKApplicationDelegate> delegate;
```

#### Discussion

The delegate object is an object that conforms to the [`WKApplicationDelegate`](../wkapplicationdelegate.md) protocol. You provide the delegate object and use it to manage lifecycle events in your extension. Providing a delegate object is required if your extension supports actionable notifications or Handoff behaviors.

For more information about the methods of the delegate object, see [`WKApplicationDelegate`](../wkapplicationdelegate.md).

## See Also

### Accessing the app delegate
- [protocol WKApplicationDelegate](../wkapplicationdelegate.md)
  A collection of methods that manages the app-level behavior for a single-target watchOS app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplication/delegate)*