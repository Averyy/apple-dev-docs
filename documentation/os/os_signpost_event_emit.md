# os_signpost_event_emit

**Framework**: os  
**Kind**: macro  
**Role**: Macro

Marks a point of interest in time.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
#define os_signpost_event_emit(log, event_id, name, ...)
```

## Discussion

This function is equivalent to calling [`os_signpost_emit_with_type`](./os_signpost_emit_with_type.md) with a type of [`OS_SIGNPOST_EVENT`](./os_signpost_type_t/os_signpost_event.md).

## Parameters

- `log`: The log that provides the subsystem and category to use. For more information, see [`os_log_create`](./os_log_create.md).
- `event_id`: The event’s identifier.
- `name`: The event’s name.
- `…`: An optional format string. If you provide the string, you must follow it with any required arguments in the order that they appear in the string.

## See Also

### Measure Events
- [Recording Performance Data](./recording-performance-data.md)
  Add signposts to record interesting time-based events.
- [Legacy Signpost Symbols](./legacy-signpost-symbols.md)
  Migrate your code away from using these legacy symbols.
- [os_signpost_emit_with_type](./os_signpost_emit_with_type.md)
  Logs a point of interest in your code as a time interval or as an event for debugging performance in Instruments.
- [struct OSSignpostType](./ossignposttype.md)
  The different kinds of signpost.
- [os_signpost_interval_begin](./os_signpost_interval_begin.md)
  Marks the start of a time interval in your code using a signpost.
- [os_signpost_interval_end](./os_signpost_interval_end.md)
  Marks the end of a time interval in your code using a signpost.
- [typealias os_signpost_id_t](./os_signpost_id_t.md)
  An identifier you use to distinguish between signposts that have the same name and destination log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_signpost_event_emit)*