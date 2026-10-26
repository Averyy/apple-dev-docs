# kIOPSBatteryHealthConditionKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

kIOPSBatteryHealthConditionKey broadly describes the battery's health.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.6+

## Declaration

```c
#define kIOPSBatteryHealthConditionKey
```

#### Discussion

- Apple-defined power sources will publish this key.
- Value is one of the "Battery Health Condition Values" strings described in this file.
- For power source creators: Providing this key is OPTIONAL - these keys have values only used by Apple power sources.
- Type CFStringRef


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopsbatteryhealthconditionkey)*