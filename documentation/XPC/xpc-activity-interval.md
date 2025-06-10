# XPC_ACTIVITY_INTERVAL

**Framework**: XPC  
**Kind**: var

An integer property that indicates the desired time interval of the activity in seconds.

**Availability**:
- macOS 10.9+

## Declaration

```swift
let XPC_ACTIVITY_INTERVAL: UnsafePointer<CChar>
```

#### Discussion

The activity doesn’t run more than once per time interval. Due to the nature of XPC Activity finding an opportune time to run the activity, any two occurrences may be more or less than [`XPC_ACTIVITY_INTERVAL`](xpc_activity_interval.md) seconds apart, but on average are [`XPC_ACTIVITY_INTERVAL`](xpc_activity_interval.md) seconds apart. The presence of this key implies the following, unless you override these values:

- [`XPC_ACTIVITY_REPEATING`](xpc_activity_repeating.md) with a value of `true`
- [`XPC_ACTIVITY_DELAY`](xpc_activity_delay.md) with a value of half the interval. The delay enforces a minimum distance between any two occurrences.
- [`XPC_ACTIVITY_GRACE_PERIOD`](xpc_activity_grace_period.md) with a value of half the interval. The grace period is the amount of time that passes after the end of the interval before more aggressive scheduling occurs. The grace period doesn’t increase the size of the interval.

## See Also

- [let XPC_ACTIVITY_INTERVAL_1_MIN: Int64](xpc_activity_interval_1_min.md)
  A constant that represents a 1-minute time interval.
- [let XPC_ACTIVITY_INTERVAL_5_MIN: Int64](xpc_activity_interval_5_min.md)
  A constant that represents a 5-minute time interval.
- [let XPC_ACTIVITY_INTERVAL_15_MIN: Int64](xpc_activity_interval_15_min.md)
  A constant that represents a 15-minute time interval.
- [let XPC_ACTIVITY_INTERVAL_30_MIN: Int64](xpc_activity_interval_30_min.md)
  A constant that represents a 30-minute time interval.
- [let XPC_ACTIVITY_INTERVAL_1_HOUR: Int64](xpc_activity_interval_1_hour.md)
  A constant that represents a 1-hour time interval.
- [let XPC_ACTIVITY_INTERVAL_4_HOURS: Int64](xpc_activity_interval_4_hours.md)
  A constant that represents a 4-hour time interval.
- [let XPC_ACTIVITY_INTERVAL_8_HOURS: Int64](xpc_activity_interval_8_hours.md)
  A constant that represents an 8-hour time interval.
- [let XPC_ACTIVITY_INTERVAL_1_DAY: Int64](xpc_activity_interval_1_day.md)
  A constant that represents a one-day time interval.
- [let XPC_ACTIVITY_INTERVAL_7_DAYS: Int64](xpc_activity_interval_7_days.md)
  A constant that represents a seven-day time interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_activity_interval)*