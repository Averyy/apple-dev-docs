# Timer Option Masks

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Indicate optional actions when calling `MPArmTimer`. 

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [kMPPreserveTimerIDMask](./api-1585611-timer_option_masks/kmppreservetimeridmask.md)
- [kMPTimeIsDeltaMask](./api-1585611-timer_option_masks/kmptimeisdeltamask.md)
- [kMPTimeIsDurationMask](./api-1585611-timer_option_masks/kmptimeisdurationmask.md)
  Specifying this mask indicates that the specified expiration time is of type `Duration`. You can use this mask to avoid having to call time conversion routines when specifying an expiration time. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585611-timer_option_masks)*