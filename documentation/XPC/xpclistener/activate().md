# activate()

**Framework**: XPC  
**Kind**: method  
**Role**: Instance Method

Activates an inactive listener.

**Availability**:
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
func activate() throws
```

## Discussion

If you create an inactive listener using the [`inactive`](./initializationoptions/inactive.md) flag, be sure to activate it before releasing the last reference to the listener. Releasing the last reference to an inactive listener crashes.

If activation fails, the system automatically cancels the listener.

## See Also

### Managing the life cycle
- [func cancel()](./cancel%28%29.md)
  Cancels a listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpclistener/activate())*