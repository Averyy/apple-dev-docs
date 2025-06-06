# mach_absolute_time

**Framework**: Kernel  
**Kind**: func

Returns current value of a clock that increments monotonically in tick units (starting at an arbitrary point), this clock does not increment while the system is asleep.

**Availability**:
- macOS 10.0+

## Declaration

```swift
uint64_t mach_absolute_time(void);
```

#### Return_value

		Value of mach absolute time clock.

#### Discussion

Prefer to use the equivalent clock_gettime_nsec_np(CLOCK_UPTIME_RAW) in nanoseconds.

> ❗ **Important**: This API has the potential of being misused to access device signals to try to identify the device or user, also known as fingerprinting. Regardless of whether a user gives your app permission to track, fingerprinting is not allowed. When you use this API in your app or third-party SDK (an SDK not provided by Apple), declare your usage and the reason for using the API in your app or third-party SDK’s `PrivacyInfo.xcprivacy` file. For more information, including the list of valid reasons for using the API, see [`Describing use of required reason API`](https://developer.apple.com/documentation/bundleresources/describing-use-of-required-reason-api).

This API has the potential of being misused to access device signals to try to identify the device or user, also known as fingerprinting. Regardless of whether a user gives your app permission to track, fingerprinting is not allowed. When you use this API in your app or third-party SDK (an SDK not provided by Apple), declare your usage and the reason for using the API in your app or third-party SDK’s `PrivacyInfo.xcprivacy` file. For more information, including the list of valid reasons for using the API, see [`Describing use of required reason API`](https://developer.apple.com/documentation/bundleresources/describing-use-of-required-reason-api).

## See Also

- [mach_approximate_time](1462443-mach_approximate_time.md)
- [mach_continuous_time](1646199-mach_continuous_time.md)
  Returns current value of a clock that increments monotonically in tick units (starting at an arbitrary point), including while the system is asleep.
- [mach_continuous_approximate_time](1646198-mach_continuous_approximate_time.md)
- [mach_bridge_remote_time](2870302-mach_bridge_remote_time.md)
- [mach_bridge_compute_timestamp](2935668-mach_bridge_compute_timestamp.md)
- [mach_bridge_register_regwrite_timestamp_callback](2869537-mach_bridge_register_regwrite_ti.md)
- [mach_timebase_info_t](mach_timebase_info_t.md)
- [mach_zone_info_array_t](mach_zone_info_array_t.md)
- [mach_zone_name_array_t](mach_zone_name_array_t.md)
- [mach_timebase_info_data_t](mach_timebase_info_data_t.md)
   Raw Mach Time API In general prefer to use the <time.h> API clock_gettime_nsec_np(3), which deals in the same clocks (and more) in ns units. Conversion of ns to (resp. from) tick units as returned by the mach time APIs is performed by division (resp. multiplication) with the fraction returned by mach_timebase_info().
- [mach_timespec_t](mach_timespec_t.md)
- [mach_zone_info_t](mach_zone_info_t.md)
- [clock_attr_t](clock_attr_t.md)
- [clock_ctrl_port_t](clock_ctrl_port_t.md)
- [clock_ctrl_t](clock_ctrl_t.md)
- [clock_flavor_t](clock_flavor_t.md)
- [clock_id_t](clock_id_t.md)
- [clock_nsec_t](clock_nsec_t.md)
- [clock_reply_subsystem](clock_reply_subsystem.md)
- [clock_reply_t](clock_reply_t.md)
- [clock_res_t](clock_res_t.md)
- [clock_sec_t](clock_sec_t.md)
- [clock_serv_port_t](clock_serv_port_t.md)
- [clock_serv_t](clock_serv_t.md)
- [clock_t](clock_t.md)
- [clock_usec_t](clock_usec_t.md)
- [clockinfo](clockinfo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1462446-mach_absolute_time)*