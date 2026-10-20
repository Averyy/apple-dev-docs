# WKPreferences.InactiveSchedulingPolicy.none

**Framework**: WebKit  
**Kind**: case  
**Role**: Case

A policy where a web view that’s not in a window runs tasks normally.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
case none
```

```c
WKInactiveSchedulingPolicyNone
```

## See Also

### Scheduling policies
- [WKPreferences.InactiveSchedulingPolicy.suspend](./suspend.md)
  A policy where a web view that’s not in a window fully suspends tasks.
- [WKPreferences.InactiveSchedulingPolicy.throttle](./throttle.md)
  A policy where a web view that’s not in a window limits processing, but does not fully suspend tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkpreferences/inactiveschedulingpolicy-swift.enum/none)*