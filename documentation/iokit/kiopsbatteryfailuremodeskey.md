# kIOPSBatteryFailureModesKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

Enumerates a battery's failures and error conditions.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.6+

## Declaration

```c
#define kIOPSBatteryFailureModesKey
```

## Discussion

Various battery failures will be listed here. A battery may suffer from more than one type of failure simultaneously, so this key has a CFArray value.

If BatteryFailureModesKey is not defined (or is set to an empty dictionary), then the battery has no detectable failures.

Each entry in the array should be a short descriptive string describing the error.

- Apple-defined power sources will publish this key if any battery errors exist.
- For power source creators: Providing this key is RECOMMENDED.
- Type CFArrayRef


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopsbatteryfailuremodeskey)*