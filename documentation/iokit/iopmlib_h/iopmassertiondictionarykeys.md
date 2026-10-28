# IOPMAssertionDictionaryKeys

**Framework**: IOKit  
**Kind**: macro

## Declaration

```c
/*!
   */
#define kIOPMAssertionTimeoutKey CFSTR("TimeoutSeconds")
/*!
   */
#define kIOPMAssertionTimeoutActionKey CFSTR("TimeoutAction")
/*!
   */
#define kIOPMAssertionTimeoutActionLog CFSTR("TimeoutActionLog")
/*!
   */
#define kIOPMAssertionTimeoutActionTurnOff CFSTR("TimeoutActionTurnOff")
/*!
   */
#define kIOPMAssertionTimeoutActionRelease CFSTR("TimeoutActionRelease")
/*!
   */
#define kIOPMAssertionRetainCountKey CFSTR("RetainCount")
/*!
   */
#define kIOPMAssertionNameKey CFSTR("AssertName")
/*!
   */
#define kIOPMAssertionDetailsKey CFSTR("Details")
/*!
   */
#define kIOPMAssertionHumanReadableReasonKey CFSTR("HumanReadableReason")
/*!
   */
#define kIOPMAssertionLocalizationBundlePathKey CFSTR("BundlePath")
/*!
   */
#define kIOPMAssertionFrameworkIDKey CFSTR("FrameworkBundleID")
/*!
   */
#define kIOPMAssertionPlugInIDKey CFSTR("PlugInBundleID")
/*!
   */
#define kIOPMAssertionTypeKey CFSTR("AssertType")
/*!
   */
#define kIOPMAssertionLevelKey CFSTR("AssertLevel")
```

## Overview

Keys into dictionaries describing assertions.

## See Also

### Miscellaneous
- [IOPMAssertionTypes](./iopmassertiontypes.md)
  Use as AssertionType argument to [`IOPMAssertionCreate`](../api-1557118-iopmassertioncreate.md). The idle display will not sleep when enabled, and consequently the system will not idle sleep.
- [IOPMCopyBatteryInfo](../api-1557138-iopmcopybatteryinfo.md)
  Request raw battery data from the system.
- [IOPMFindPowerManagement](../api-1557133-iopmfindpowermanagement.md)
  Finds the Root Power Domain IOService.
- [IOPMGetAggressiveness](../api-1557117-iopmgetaggressiveness.md)
  Retrieves the current value of one of the aggressiveness factors in IOKit Power Management.
- [IOPMSetAggressiveness](../api-1557098-iopmsetaggressiveness.md)
  Sets one of the aggressiveness factors in IOKit Power Management.
- [IOPMSleepEnabled](../api-1557074-iopmsleepenabled.md)
  Tells whether the system supports full sleep, or just doze
- [IOPMSleepSystem](../api-1557121-iopmsleepsystem.md)
  Request that the system initiate sleep.
### Related Documentation
- [kIOPMAssertionFrameworkIDKey](../kiopmassertionframeworkidkey.md)
  Specify if the assertion creator is a framework.
- [kIOPMAssertionRetainCountKey](../kiopmassertionretaincountkey.md)
  A potential value for 
- [kIOPMAssertionDetailsKey](../kiopmassertiondetailskey.md)
  The CFDictionary key for assertion name. Setting this key is required when you're creating an assertion.
- [kIOPMAssertionTypeKey](../kiopmassertiontypekey.md)
  The CFDictionary key for assertion type in an assertion info dictionary.
- [kIOPMAssertionTimeoutKey](../kiopmassertiontimeoutkey.md)
  kIOPMAssertionTimeoutKey specifies an outer bound, in seconds, that this assertion should be asserted.
- [kIOPMAssertionPlugInIDKey](../kiopmassertionpluginidkey.md)
  Specify if the assertion creator is a plugin.
- [kIOPMAssertionLevelKey](../kiopmassertionlevelkey.md)
  The CFDictionary key for assertion level in an assertion info dictionary.
- [kIOPMAssertionLocalizationBundlePathKey](../kiopmassertionlocalizationbundlepathkey.md)
  Refers to a CFURL, as a CFString, identifying the path to the caller's bundle, which contains localization info.
- [kIOPMAssertionNameKey](../kiopmassertionnamekey.md)
  The CFDictionary key for assertion name. Setting this key is required when you're creating an assertion.
- [kIOPMAssertionTimeoutActionKey](../kiopmassertiontimeoutactionkey.md)
  Specifies the action to take upon timeout expiration.
- [kIOPMAssertionTimeoutActionTurnOff](../kiopmassertiontimeoutactionturnoff.md)
  A potential value for 
- [kIOPMAssertionHumanReadableReasonKey](../kiopmassertionhumanreadablereasonkey.md)
  Optional key that provides a localizable string for macOS to display PM Assertions in the GUI.
- [kIOPMAssertionTimeoutActionRelease](../kiopmassertiontimeoutactionrelease.md)
  A potential value for 
- [kIOPMAssertionTimeoutActionLog](../kiopmassertiontimeoutactionlog.md)
  A potential value for 


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iopmlib_h/iopmassertiondictionarykeys)*