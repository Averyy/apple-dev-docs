# tIOUSB30LinkStateTimeout

**Framework**: USBDriverKit  
**Kind**: enum

Constants for the link state timeout values on USB 3.0 devices.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
enum tIOUSB30LinkStateTimeout : unsigned int;
```

#### Discussion

For information about these constants, see Table 7-12 of the USB 3.0 specification, and sections 7.5.4, 7.5.9, and 7.5.10 of the USB 3.0 specification at [`http://www.usb.org`](https://developer.apple.comhttp://www.usb.org).

## Topics

### Getting the Link State Timeouts
- [kIOUSB30LinkStateSSInactiveQuietTimeout](tiousb30linkstatetimeout/kiousb30linkstatessinactivequiettimeout.md)
- [kIOUSB30LinkStateRxDetectQuietTimeout](tiousb30linkstatetimeout/kiousb30linkstaterxdetectquiettimeout.md)
- [kIOUSB30LinkStatePollingLFPSTimeout](tiousb30linkstatetimeout/kiousb30linkstatepollinglfpstimeout.md)
- [kIOUSB30LinkStatePollingActiveTimeout](tiousb30linkstatetimeout/kiousb30linkstatepollingactivetimeout.md)
- [kIOUSB30LinkStatePollingConfigurationTimeout](tiousb30linkstatetimeout/kiousb30linkstatepollingconfigurationtimeout.md)
- [kIOUSB30LinkStatePollingIdleTimeout](tiousb30linkstatetimeout/kiousb30linkstatepollingidletimeout.md)
- [kIOUSB30LinkStateU0LTimeout](tiousb30linkstatetimeout/kiousb30linkstateu0ltimeout.md)
- [kIOUSB30LinkStateU0RecoveryTimeout](tiousb30linkstatetimeout/kiousb30linkstateu0recoverytimeout.md)
- [kIOUSB30LinkStateU1NoLFPSResponseTimeout](tiousb30linkstatetimeout/kiousb30linkstateu1nolfpsresponsetimeout.md)
- [kIOUSB30LinkStateU1PingTimeout](tiousb30linkstatetimeout/kiousb30linkstateu1pingtimeout.md)
- [kIOUSB30LinkStateU2NoLFPSResponseTimeout](tiousb30linkstatetimeout/kiousb30linkstateu2nolfpsresponsetimeout.md)
- [kIOUSB30LinkStateU3NoLFPSResponseTimeout](tiousb30linkstatetimeout/kiousb30linkstateu3nolfpsresponsetimeout.md)
- [kIOUSB30LinkStateU3RxDetectDelay](tiousb30linkstatetimeout/kiousb30linkstateu3rxdetectdelay.md)
- [kIOUSB30LinkStateU3WakeupRetryDelay](tiousb30linkstatetimeout/kiousb30linkstateu3wakeupretrydelay.md)
- [kIOUSB30LinKStateU2RxDetectDelay](tiousb30linkstatetimeout/kiousb30linkstateu2rxdetectdelay.md)
- [kIOUSB30LinkStateRecoveryActiveTimeout](tiousb30linkstatetimeout/kiousb30linkstaterecoveryactivetimeout.md)
- [kIOUSB30LinkStateRecoveryConfigurationTimeout](tiousb30linkstatetimeout/kiousb30linkstaterecoveryconfigurationtimeout.md)
- [kIOUSB30LinkStateRecoveryIdleTimeout](tiousb30linkstatetimeout/kiousb30linkstaterecoveryidletimeout.md)
- [kIOUSB30LinkStateLoopbackExitTimeout](tiousb30linkstatetimeout/kiousb30linkstateloopbackexittimeout.md)
- [kIOUSB30LinkStateHotResetActiveTimeout](tiousb30linkstatetimeout/kiousb30linkstatehotresetactivetimeout.md)
- [kIOUSB30LinkStatePollingDeadline](tiousb30linkstatetimeout/kiousb30linkstatepollingdeadline.md)
- [kIOUSB30LinkStateSSResumeDeadline](tiousb30linkstatetimeout/kiousb30linkstatessresumedeadline.md)
### Enumeration Cases
- [kIOUSB30LinkStateHotResetDeadline](tiousb30linkstatetimeout/kiousb30linkstatehotresetdeadline.md)
- [kIOUSB30LinkStateHotResetExitTimeout](tiousb30linkstatetimeout/kiousb30linkstatehotresetexittimeout.md)
- [kIOUSB30LinkStateRecoveryDeadline](tiousb30linkstatetimeout/kiousb30linkstaterecoverydeadline.md)

## See Also

- [tIOUSB30ResetTimeout](tiousb30resettimeout.md)
  Constants for the reset timeout values on USB 3.0 devices.
- [tIOUSB30TimingParameters](tiousb30timingparameters.md)
  Constants for USB 3.0 timing parameters.
- [Timing Parameters](timing_parameters-enum.md)
  Constants for ping response times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/tiousb30linkstatetimeout)*