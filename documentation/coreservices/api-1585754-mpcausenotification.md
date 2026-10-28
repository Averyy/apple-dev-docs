# MPCauseNotification

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Signals a kernel notification. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPCauseNotification(MPNotificationID notificationID);
```

## Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965).

## Discussion

You call this function to signal a kernel notification much as you would signal any simple notification (for example,  [`MPNotifyQueue`](./api-1585699-mpnotifyqueue.md) ). 

## Parameters

- `notificationID`: The ID of the kernel notification you want to signal. 

## See Also

### Handling Kernel Notifications
- [MPCreateNotification](./api-1585723-mpcreatenotification.md)
  Creates a kernel notification
- [MPDeleteNotification](./api-1585659-mpdeletenotification.md)
  Removes a kernel notification. 
- [MPModifyNotification](./api-1585780-mpmodifynotification.md)
  Adds a simple notification to a kernel notification.
- [MPModifyNotificationParameters](./api-1585668-mpmodifynotificationparameters.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585754-mpcausenotification)*