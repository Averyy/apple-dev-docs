# addNotification

**Framework**: Kernel  
**Kind**: clm

**Availability**:
- macOS 10.11.4+ - Deprecated in 10.11.4

## Declaration

```swift
static OSPtr<IONotifier> addNotification(const OSSymbol *type, OSDictionary *matching, IOServiceNotificationHandler handler, void *target, void *ref, SInt32 priority);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioservice/1532881-addnotification)*