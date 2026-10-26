# setBusyTimeoutRegisterValue

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets the value to be written to the BUSY_TIMEOUT register.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
IOReturn (*setBusyTimeoutRegisterValue)(void *self, UInt32 timeout);
```

#### Discussion

1394-1995 defines a register known as the BUSY_TIMEOUT register. This register controls the busy retry behavior of your device. The initial value for this register is 0x00000000. Which means busied transactions will not be retried. Since most devices want their transactions retired on busy acks, the SBP2 service automatically updates the BUSY_TIMEOUT register with the value specified here whenever necessary. Most drivers should set this value to 0x0000000f.

## Parameters

- `self`: Pointer to IOFireWireSBP2LibLoginInterface object.
- `timeout`: desired value of the BUSY_TIMEOUT register.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2liblogininterface/1590478-setbusytimeoutregistervalue)*