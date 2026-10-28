# kMPTimeIsDeltaMask

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
kMPTimeIsDeltaMask = 1L << 1
```

## Discussion

Specifying this mask indicates that the specified time should be added to the previous expiration time to form the new expiration time. You can use this mask to compensate for timing drift caused by the finite amount of time required to arm the timer, receive the notification, and so on. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585611-timer_option_masks/kmptimeisdeltamask)*