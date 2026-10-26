# Timeout Constants

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify a timeout value.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
enum : int {
    ...
};
```

## Topics

### Constants
- [kAEDefaultTimeout](./api-1542814-timeout_constants/kaedefaulttimeout.md)
  The timeout value is determined by the Apple Event Manager. The default timeout value is about one minute.
- [kNoTimeOut](./api-1542814-timeout_constants/knotimeout.md)
  Your application is willing to wait indefinitely. Most commonly, you instead provide a timeout value (in ticks) that will provide a reasonable amount of time for the current operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1542814-timeout_constants)*