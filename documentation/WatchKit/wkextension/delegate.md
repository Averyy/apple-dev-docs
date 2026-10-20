# delegate

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The delegate of the WatchKit extension object.

**Availability**:
- watchOS 2.0+ - Deprecated in 9.2 (renamed: WKApplication)

## Declaration

```swift
weak var delegate: (any WKExtensionDelegate)? { get }
```

```objc
@property (nonatomic, weak, readonly, nullable) id<WKExtensionDelegate> delegate;
```

#### Discussion

The delegate object is an object that conforms to the [`WKExtensionDelegate`](../wkextensiondelegate.md) protocol. You provide the delegate object and use it to manage lifecycle events in your extension. Providing a delegate object is required if your extension supports actionable notifications or Handoff behaviors.

For more information about the methods of the delegate object, see [`WKExtensionDelegate`](../wkextensiondelegate.md).

## See Also

### Accessing the extension delegate
- [protocol WKExtensionDelegate](../wkextensiondelegate.md)
  A collection of methods that manages the app-level behavior of a WatchKit extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/delegate)*