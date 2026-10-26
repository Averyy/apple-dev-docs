# IOGetSystemLoadAdvisory

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Returns a hint about whether now would be a good time to perform time-insensitive work.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.6+

## Declaration

```c
IOSystemLoadAdvisoryLevel IOGetSystemLoadAdvisory(void);
```

#### Return Value

IOSystemLoadAdvisoryLevel - one of: kIOSystemLoadAdvisoryLevelGreat - A Good time to perform time-insensitive work. kIOSystemLoadAdvisoryLevelOK - An OK time to perform time-insensitive work. kIOSystemLoadAdvisoryLevelBad - A Bad time to perform time-insensitive work.

#### Discussion

Based on user and system load, IOGetSystemLoadAdvisory determines "better" and "worse" times to run optional or time-insensitive CPU or disk work.

Applications may use this result to avoid degrading the user experience. If it is a "Bad" or "OK" time to perform work, applications should slow down and perform work less aggressively.

There is no guarantee that the system will ever be in "Great" condition to perform work - all essential work must still be performed even in "Bad", or "OK" times. Completely optional work, such as updating caches, may be postponed indefinitely.

Note: You may more efficiently read the SystemLoadAdvisory level using notify_get_state() instead of IOGetSystemLoadAdvisory. The results are identical. notify_get_state() requires that you pass the token argument received by registering for SystemLoadAdvisory notifications.

## See Also

### IOSystemLoadAdvisory
- [IOCopySystemLoadAdvisoryDetailed](./api-1557099-iocopysystemloadadvisorydetailed.md)
  Indicates how user activity, battery level, and thermal level each contribute to the overall "SystemLoadAdvisory" level. In the future, this combined level may represent new levels as well.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1557110-iogetsystemloadadvisory)*