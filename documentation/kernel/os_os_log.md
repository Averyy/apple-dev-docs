# OS_os_log

**Framework**: Kernel  
**Kind**: intf  
**Role**: Protocol

**Availability**:
- macOS 10.12+

## Declaration

```objc
@protocol OS_os_log
```

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Logging
- [IOLog](./api-1575337-iolog.md)
  Log a message to console in text mode, and /var/log/system.log.
- [IOLogv](./api-1575323-iologv.md)
  Log a message to console in text mode, and /var/log/system.log.
- [os_log_create](./api-1643798-os_log_create.md)
  Creates a custom log object, to be passed to logging functions for sending messages to the logging system.
- [os_log_debug_enabled](./api-1643808-os_log_debug_enabled.md)
  Returns a Boolean value indicating whether debug-level logging is enabled for a specified log object.
- [os_log_info_enabled](./api-1643817-os_log_info_enabled.md)
  Returns a Boolean value indicating whether info-level logging is enabled for a specified log object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/os_os_log)*