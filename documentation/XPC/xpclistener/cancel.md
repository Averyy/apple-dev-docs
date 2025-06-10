# cancel()

**Framework**: XPC  
**Kind**: method

Cancels a listener.

**Availability**:
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
func cancel()
```

#### Discussion

Typically you don’t need to explicitly cancel a listener. When the server process exits, the system automatically cancels the listener. In rare circumstances, such as part of a testing infrastructure, you may want to cancel a listener to ensure it doesn’t receive any new messages. Be aware that canceling a listener causes peers attempting to connect to the service to hang.

## See Also

- [func activate() throws](xpclistener/activate.md)
  Activates an inactive listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpclistener/cancel())*