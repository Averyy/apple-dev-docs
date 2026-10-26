# Defines

**Framework**: IOKit  
**Role**: API Collection

## Topics

### Constants
- [kIOPMAutoPowerOn](../kiopmautopoweron.md)
  Value for scheduled power on from off state.
- [kIOPMAutoRestart](../kiopmautorestart.md)
  Value for scheduled restart.
- [kIOPMAutoShutdown](../kiopmautoshutdown.md)
  Value for scheduled shutdown.
- [kIOPMAutoSleep](../kiopmautosleep.md)
  Value for scheduled sleep.
- [kIOPMAutoWake](../kiopmautowake.md)
  Value for scheduled wake from sleep.
- [kIOPMAutoWakeOrPowerOn](../kiopmautowakeorpoweron.md)
  Value for scheduled wake from sleep, or power on. The system will either wake OR power on, whichever is necessary.
- [kIOPMPowerEventAppNameKey](../kiopmpowereventappnamekey.md)
  Key for the CFBundleIdentifier of the app that scheduled the power event. Value is a CFStringRef.
- [kIOPMPowerEventTimeKey](../kiopmpowereventtimekey.md)
  Key for the time of the scheduled power event. Value is a CFDateRef.
- [kIOPMPowerEventTypeKey](../kiopmpowereventtypekey.md)
  Key for the type of power event. Value is a CFStringRef, with the c-string value of one of the "kIOPMAuto" strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iopmkeys_h/defines)*