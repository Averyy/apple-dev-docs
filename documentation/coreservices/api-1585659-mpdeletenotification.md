# MPDeleteNotification

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Removes a kernel notification. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPDeleteNotification(MPNotificationID notificationID);
```

## Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965).

## Discussion

Also see the function  [`MPCreateNotification`](./api-1585723-mpcreatenotification.md). 

## Parameters

- `notificationID`: The ID of the notification you want to remove. 

## See Also

### Handling Kernel Notifications
- [MPCauseNotification](./api-1585754-mpcausenotification.md)
  Signals a kernel notification. 
- [MPCreateNotification](./api-1585723-mpcreatenotification.md)
  Creates a kernel notification
- [MPModifyNotification](./api-1585780-mpmodifynotification.md)
  Adds a simple notification to a kernel notification.
- [MPModifyNotificationParameters](./api-1585668-mpmodifynotificationparameters.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585659-mpdeletenotification)*