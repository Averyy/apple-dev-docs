# IOHIDDeviceConformsTo

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Convenience function that scans the Application Collection elements to see if it conforms to the provided usagePage and usage.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```c
Boolean IOHIDDeviceConformsTo(IOHIDDeviceRef device, uint32_t usagePage, uint32_t usage);
```

#### Return Value

Returns TRUE if device conforms to provided usage.

#### Discussion

Examples of Application Collection usages pairs are:

usagePage = kHIDPage_GenericDesktop

usage = kHIDUsage_GD_Mouse

**or**

usagePage = kHIDPage_GenericDesktop

usage = kHIDUsage_GD_Keyboard

## Parameters

- `device`: Reference to an IOHIDDevice.
- `usagePage`: Device usage page
- `usage`: Device usage

## See Also

### Miscellaneous
- [IOHIDDeviceClose](./api-1588668-iohiddeviceclose.md)
  Closes communication with a HID device.
- [IOHIDDeviceCopyMatchingElements](./api-1588671-iohiddevicecopymatchingelements.md)
  Obtains HID elements that match the criteria contained in the matching dictionary.
- [IOHIDDeviceCopyValueMultiple](./api-1588652-iohiddevicecopyvaluemultiple.md)
  Copies a values for multiple elements.
- [IOHIDDeviceCopyValueMultipleWithCallback](./api-1588655-iohiddevicecopyvaluemultiplewith.md)
  Copies a values for multiple elements and returns status via a completion callback.
- [IOHIDDeviceCreate](./api-1588663-iohiddevicecreate.md)
  Creates an element from an io_service_t.
- [IOHIDDeviceGetProperty](./api-1588648-iohiddevicegetproperty.md)
  Obtains a property from an IOHIDDevice.
- [IOHIDDeviceGetReport](./api-1588659-iohiddevicegetreport.md)
  Obtains a report from the device.
- [IOHIDDeviceGetReportWithCallback](./api-1588662-iohiddevicegetreportwithcallback.md)
  Obtains a report from the device.
- [IOHIDDeviceGetService](./api-1588646-iohiddevicegetservice.md)
  Returns the io_service_t for an IOHIDDevice, if it has one.
- [IOHIDDeviceGetTypeID](./api-1588664-iohiddevicegettypeid.md)
  Returns the type identifier of all IOHIDDevice instances.
- [IOHIDDeviceGetValue](./api-1588657-iohiddevicegetvalue.md)
  Gets a value for an element.
- [IOHIDDeviceGetValueWithCallback](./api-1588647-iohiddevicegetvaluewithcallback.md)
  Gets a value for an element and returns status via a completion callback.
- [IOHIDDeviceOpen](./api-1588670-iohiddeviceopen.md)
  Opens a HID device for communication.
- [IOHIDDeviceRegisterInputReportCallback](./api-1588666-iohiddeviceregisterinputreportca.md)
  Registers a callback to be used when an input report is issued by the device.
- [IOHIDDeviceRegisterInputValueCallback](./api-1588672-iohiddeviceregisterinputvaluecal.md)
  Registers a callback to be used when an input value is issued by the device.
- [IOHIDDeviceRegisterRemovalCallback](./api-1588673-iohiddeviceregisterremovalcallba.md)
  Registers a callback to be used when a IOHIDDevice is removed.
- [IOHIDDeviceScheduleWithRunLoop](./api-1588660-iohiddeviceschedulewithrunloop.md)
  Schedules HID device with run loop.
- [IOHIDDeviceSetInputValueMatching](./api-1588654-iohiddevicesetinputvaluematching.md)
  Sets matching criteria for input values received via IOHIDDeviceRegisterInputValueCallback.
- [IOHIDDeviceSetInputValueMatchingMultiple](./api-1588645-iohiddevicesetinputvaluematching.md)
  Sets multiple matching criteria for input values received via IOHIDDeviceRegisterInputValueCallback.
- [IOHIDDeviceSetProperty](./api-1588653-iohiddevicesetproperty.md)
  Sets a property for an IOHIDDevice.
- [IOHIDDeviceSetReport](./api-1588656-iohiddevicesetreport.md)
  Sends a report to the device.
- [IOHIDDeviceSetReportWithCallback](./api-1588661-iohiddevicesetreportwithcallback.md)
  Sends a report to the device.
- [IOHIDDeviceSetValue](./api-1588651-iohiddevicesetvalue.md)
  Sets a value for an element.
- [IOHIDDeviceSetValueMultiple](./api-1588669-iohiddevicesetvaluemultiple.md)
  Sets multiple values for multiple elements.
- [IOHIDDeviceSetValueMultipleWithCallback](./api-1588658-iohiddevicesetvaluemultiplewithc.md)
  Sets multiple values for multiple elements and returns status via a completion callback.
- [IOHIDDeviceSetValueWithCallback](./api-1588667-iohiddevicesetvaluewithcallback.md)
  Sets a value for an element and returns status via a completion callback.
- [IOHIDDeviceUnscheduleFromRunLoop](./api-1588650-iohiddeviceunschedulefromrunloop.md)
  Unschedules HID device with run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1588665-iohiddeviceconformsto)*