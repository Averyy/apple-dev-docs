# RegisterForNotification

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.9+

## Declaration

```c
IOReturn (*RegisterForNotification)(void *self, UInt64 notificationMask, IOAsyncCallback2 callback, void *refCon, UInt64 *pRegistrationToken);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface650/1559434-registerfornotification)*