# doInstallNotification

**Framework**: Kernel  
**Kind**: clm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
static OSPtr<IONotifier> doInstallNotification(const OSSymbol *type, OSDictionary *matching, IOServiceMatchingNotificationHandler handler, void *target, void *ref, SInt32 priority, OSIterator **existing);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioservice/1532603-doinstallnotification)*