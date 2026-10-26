# Defines

**Framework**: IOKit  
**Role**: API Collection

## Topics

### Constants
- [kIOPMAssertionDetailsKey](../kiopmassertiondetailskey.md)
  The CFDictionary key for assertion name. Setting this key is required when you're creating an assertion.
- [kIOPMAssertionFrameworkIDKey](../kiopmassertionframeworkidkey.md)
  Specify if the assertion creator is a framework.
- [kIOPMAssertionHumanReadableReasonKey](../kiopmassertionhumanreadablereasonkey.md)
  Optional key that provides a localizable string for macOS to display PM Assertions in the GUI.
- [kIOPMAssertionLevelKey](../kiopmassertionlevelkey.md)
  The CFDictionary key for assertion level in an assertion info dictionary.
- [kIOPMAssertionLocalizationBundlePathKey](../kiopmassertionlocalizationbundlepathkey.md)
  Refers to a CFURL, as a CFString, identifying the path to the caller's bundle, which contains localization info.
- [kIOPMAssertionNameKey](../kiopmassertionnamekey.md)
  The CFDictionary key for assertion name. Setting this key is required when you're creating an assertion.
- [kIOPMAssertionPlugInIDKey](../kiopmassertionpluginidkey.md)
  Specify if the assertion creator is a plugin.
- [kIOPMAssertionRetainCountKey](../kiopmassertionretaincountkey.md)
  A potential value for [`kIOPMAssertionTimeoutActionKey`](../kiopmassertiontimeoutactionkey.md)
- [kIOPMAssertionTimeoutActionKey](../kiopmassertiontimeoutactionkey.md)
  Specifies the action to take upon timeout expiration.
- [kIOPMAssertionTimeoutActionLog](../kiopmassertiontimeoutactionlog.md)
  A potential value for [`kIOPMAssertionTimeoutActionKey`](../kiopmassertiontimeoutactionkey.md)
- [kIOPMAssertionTimeoutActionRelease](../kiopmassertiontimeoutactionrelease.md)
  A potential value for [`kIOPMAssertionTimeoutActionKey`](../kiopmassertiontimeoutactionkey.md)
- [kIOPMAssertionTimeoutActionTurnOff](../kiopmassertiontimeoutactionturnoff.md)
  A potential value for [`kIOPMAssertionTimeoutActionKey`](../kiopmassertiontimeoutactionkey.md)
- [kIOPMAssertionTimeoutKey](../kiopmassertiontimeoutkey.md)
  kIOPMAssertionTimeoutKey specifies an outer bound, in seconds, that this assertion should be asserted.
- [kIOPMAssertionTypeKey](../kiopmassertiontypekey.md)
  The CFDictionary key for assertion type in an assertion info dictionary.
- [kIOPMAssertionTypeNoDisplaySleep](../kiopmassertiontypenodisplaysleep.md)
  Use as AssertionType argument to [`IOPMAssertionCreate`](../api-1557118-iopmassertioncreate.md). The idle display will not sleep when enabled, and consequently the system will not idle sleep.
- [kIOPMAssertionTypeNoIdleSleep](../kiopmassertiontypenoidlesleep.md)
  Pass as the AssertionType argument to [`IOPMAssertionCreate`](../api-1557118-iopmassertioncreate.md). The system will not idle sleep when enabled (display may sleep). Note that the system may sleep for other reasons.
- [kIOPMAssertionTypePreventSystemSleep](../kiopmassertiontypepreventsystemsleep.md)
  Prevents the system from sleeping and allows the system to reside in Dark Wake for an arbitrary length of time.
- [kIOPMAssertionTypePreventUserIdleDisplaySleep](../kiopmassertiontypepreventuseridledisplaysleep.md)
  Prevents the display from dimming automatically.
- [kIOPMAssertionTypePreventUserIdleSystemSleep](../kiopmassertiontypepreventuseridlesystemsleep.md)
  Prevents the system from sleeping automatically due to a lack of user activity.
- [kIOPMCPUPowerNotificationKey](../kiopmcpupowernotificationkey.md)
  Key to register for BSD style notifications on CPU power or thermal change.
- [kIOPMThermalWarningNotificationKey](../kiopmthermalwarningnotificationkey.md)
  Key to register for BSD style notifications on system thermal warnings.
- [kIOSystemLoadAdvisoryBatteryLevelKey](../kiosystemloadadvisorybatterylevelkey.md)
  Key for dictionary returned by IOCopySystemLoadAdvisoryDetailed
- [kIOSystemLoadAdvisoryCombinedLevelKey](../kiosystemloadadvisorycombinedlevelkey.md)
  Key for dictionary returned by IOCopySystemLoadAdvisoryDetailed
- [kIOSystemLoadAdvisoryNotifyName](../kiosystemloadadvisorynotifyname.md)
  The notification by this name fires when system "SystemLoadAdvisory" status changes.
- [kIOSystemLoadAdvisoryThermalLevelKey](../kiosystemloadadvisorythermallevelkey.md)
  Key for dictionary returned by IOCopySystemLoadAdvisoryDetailed
- [kIOSystemLoadAdvisoryUserLevelKey](../kiosystemloadadvisoryuserlevelkey.md)
  Key for dictionary returned by IOCopySystemLoadAdvisoryDetailed

## See Also

### Related Documentation
- [IOPMAssertionDictionaryKeys](./iopmassertiondictionarykeys.md)
- [IOPMAssertionTypes](./iopmassertiontypes.md)
  Use as AssertionType argument to . The idle display will not sleep when enabled, and consequently the system will not idle sleep.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iopmlib_h/defines)*