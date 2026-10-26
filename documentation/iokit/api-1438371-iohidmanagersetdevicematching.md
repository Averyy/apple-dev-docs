# IOHIDManagerSetDeviceMatching

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Sets matching criteria for device enumeration.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```c
void IOHIDManagerSetDeviceMatching(IOHIDManagerRef manager, CFDictionaryRef matching);
```

#### Discussion

Matching keys are prefixed by kIOHIDDevice and declared in <IOKit/hid/IOHIDKeys.h>. Passing a NULL dictionary will result in all devices being enumerated. Any subsequent calls will cause the hid manager to release previously enumerated devices and restart the enuerate process using the revised criteria. If interested in multiple, specific device classes, please defer to using IOHIDManagerSetDeviceMatchingMultiple.

## Parameters

- `manager`: Reference to an IOHIDManager.
- `matching`: CFDictionaryRef containg device matching criteria.

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
- [IOHIDManagerSetDeviceMatchingMultiple](./api-1438387-iohidmanagersetdevicematchingmul.md)
  Sets multiple matching criteria for device enumeration.
- [IOHIDManagerSetInputValueMatching](./api-1438389-iohidmanagersetinputvaluematchin.md)
  Sets matching criteria for input values received via IOHIDManagerRegisterInputValueCallback.
- [IOHIDManagerSetInputValueMatchingMultiple](./api-1438379-iohidmanagersetinputvaluematchin.md)
  Sets multiple matching criteria for input values received via IOHIDManagerRegisterInputValueCallback.
- [IOHIDManagerSetProperty](./api-1438401-iohidmanagersetproperty.md)
  Sets a property for an IOHIDManager.
- [IOHIDManagerUnscheduleFromRunLoop](./api-1438378-iohidmanagerunschedulefromrunloo.md)
  Unschedules HID manager with run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1438371-iohidmanagersetdevicematching)*