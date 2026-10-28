# IOHIDManagerSetInputValueMatchingMultiple

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Sets multiple matching criteria for input values received via IOHIDManagerRegisterInputValueCallback.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```c
void IOHIDManagerSetInputValueMatchingMultiple(IOHIDManagerRef manager, CFArrayRef multiple);
```

## Discussion

Matching keys are prefixed by kIOHIDElement and declared in <IOKit/hid/IOHIDKeys.h>. This method is useful if interested in multiple, specific elements .

## Parameters

- `manager`: Reference to an IOHIDManager.
- `multiple`: CFArrayRef containing multiple CFDictionaryRef objects containing input element matching criteria.

## See Also

### Miscellaneous
- [IOHIDManagerClose](./api-1438405-iohidmanagerclose.md)
  Closes the IOHIDManager.
- [IOHIDManagerCopyDevices](./api-1438391-iohidmanagercopydevices.md)
  Obtains currently enumerated devices.
- [IOHIDManagerCreate](./api-1438383-iohidmanagercreate.md)
  Creates an IOHIDManager object.
- [IOHIDManagerGetProperty](./api-1438403-iohidmanagergetproperty.md)
  Obtains a property of an IOHIDManager.
- [IOHIDManagerGetTypeID](./api-1438375-iohidmanagergettypeid.md)
  Returns the type identifier of all IOHIDManager instances.
- [IOHIDManagerOpen](./api-1438369-iohidmanageropen.md)
  Opens the IOHIDManager.
- [IOHIDManagerRegisterDeviceMatchingCallback](./api-1438399-iohidmanagerregisterdevicematchi.md)
  Registers a callback to be used a device is enumerated.
- [IOHIDManagerRegisterDeviceRemovalCallback](./api-1438376-iohidmanagerregisterdeviceremova.md)
  Registers a callback to be used when any enumerated device is removed.
- [IOHIDManagerRegisterInputReportCallback](./api-1438397-iohidmanagerregisterinputreportc.md)
  Registers a callback to be used when an input report is issued by any enumerated device.
- [IOHIDManagerRegisterInputValueCallback](./api-1438367-iohidmanagerregisterinputvalueca.md)
  Registers a callback to be used when an input value is issued by any enumerated device.
- [IOHIDManagerSaveToPropertyDomain](./api-1438395-iohidmanagersavetopropertydomain.md)
  Used to write out the current properties to a specific domain.
- [IOHIDManagerScheduleWithRunLoop](./api-1438409-iohidmanagerschedulewithrunloop.md)
  Schedules HID manager with run loop.
- [IOHIDManagerSetDeviceMatching](./api-1438371-iohidmanagersetdevicematching.md)
  Sets matching criteria for device enumeration.
- [IOHIDManagerSetDeviceMatchingMultiple](./api-1438387-iohidmanagersetdevicematchingmul.md)
  Sets multiple matching criteria for device enumeration.
- [IOHIDManagerSetInputValueMatching](./api-1438389-iohidmanagersetinputvaluematchin.md)
  Sets matching criteria for input values received via IOHIDManagerRegisterInputValueCallback.
- [IOHIDManagerSetProperty](./api-1438401-iohidmanagersetproperty.md)
  Sets a property for an IOHIDManager.
- [IOHIDManagerUnscheduleFromRunLoop](./api-1438378-iohidmanagerunschedulefromrunloo.md)
  Unschedules HID manager with run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1438379-iohidmanagersetinputvaluematchin)*