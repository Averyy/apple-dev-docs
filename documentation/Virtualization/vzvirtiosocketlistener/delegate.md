# delegate

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The custom object you use to respond to port-based connection attempts.

**Availability**:
- macOS 11.0+

## Declaration

```swift
weak var delegate: (any VZVirtioSocketListenerDelegate)? { get set }
```

```objc
@property (weak, nullable) id<VZVirtioSocketListenerDelegate> delegate;
```

## Discussion

Your delegate object must conform to the [`VZVirtioSocketListenerDelegate`](../vzvirtiosocketlistenerdelegate.md) protocol.

## See Also

### Responding to new connections
- [protocol VZVirtioSocketListenerDelegate](../vzvirtiosocketlistenerdelegate.md)
  An interface you use to manage connections between the guest operating system and host computer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosocketlistener/delegate)*