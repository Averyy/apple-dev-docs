# addMatchingNotification

**Framework**: Kernel  
**Kind**: clm  
**Role**: Type Method

**Availability**:
- macOS 10.11.4+

## Declaration

```c
static IONotifier * addMatchingNotification(const OSSymbol *type, OSDictionary *matching, IOServiceMatchingNotificationHandler handler, void *target, void *ref, SInt32 priority);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioservice/1532878-addmatchingnotification)*