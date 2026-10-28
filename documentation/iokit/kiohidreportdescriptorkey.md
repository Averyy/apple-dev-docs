# kIOHIDReportDescriptorKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

Keys that represent properties of a paticular device.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.6+

## Declaration

```c
#define kIOHIDReportDescriptorKey
```

## Discussion

Keys that represent properties of a paticular device. Can be added to your matching dictionary when refining searches for HID devices.

**Please note:**

kIOHIDPrimaryUsageKey and kIOHIDPrimaryUsagePageKey are no longer rich enough to describe a device's capabilities. Take, for example, a device that describes both a keyboard and a mouse in the same descriptor. The previous behavior was to only describe the keyboard behavior with the primary usage and usage page. Needless to say, this would sometimes cause a program interested in mice to skip this device when matching.

Thus we have added 3 additional keys:

- kIOHIDDeviceUsageKey
- kIOHIDDeviceUsagePageKey
- kIOHIDDeviceUsagePairsKey

kIOHIDDeviceUsagePairsKey is used to represent an array of dictionaries containing key/value pairs referenced by kIOHIDDeviceUsageKey and kIOHIDDeviceUsagePageKey. These usage pairs describe all application type collections (behaviors) defined by the device.

An application intersted in only matching on one criteria would only add the kIOHIDDeviceUsageKey and kIOHIDDeviceUsagePageKey keys to the matching dictionary. If it is interested in a device that has multiple behaviors, the application would instead add an array or dictionaries referenced by kIOHIDDeviceUsagePairsKey to his matching dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiohidreportdescriptorkey)*