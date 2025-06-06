# delegate

**Framework**: Virtualization  
**Kind**: property

The custom object you use to respond to port-based connection attempts.

**Availability**:
- macOS 11.0+

## Declaration

```swift
weak var delegate: (any VZVirtioSocketListenerDelegate)? { get set }
```

#### Discussion

Your delegate object must conform to the [`VZVirtioSocketListenerDelegate`](vzvirtiosocketlistenerdelegate.md) protocol.

## See Also

- [protocol VZVirtioSocketListenerDelegate](vzvirtiosocketlistenerdelegate.md)
  An interface you use to manage connections between the guest operating system and host computer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosocketlistener/delegate)*