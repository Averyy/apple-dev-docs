# kIOPSHardwareSerialNumberKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

A unique serial number that identifies the power source.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.6+

## Declaration

```c
#define kIOPSHardwareSerialNumberKey
```

## Discussion

For Apple-manufactured batteries, this is an alphanumeric string generated during the battery manufacturing process.

- Apple-defined power sources will publish this key if the hardware provides the serial number.
- For power source creators: Providing this key is RECOMMENDED.
- Type CFStringRef


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopshardwareserialnumberkey)*