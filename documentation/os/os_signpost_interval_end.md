# os_signpost_interval_end

**Framework**: os  
**Kind**: macro  
**Role**: Macro

Marks the end of a time interval in your code using a signpost.

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
#define os_signpost_interval_end(log, interval_id, name, ...)
```

#### Discussion

Calling this function is equivalent to calling [`os_signpost_emit_with_type`](./os_signpost_emit_with_type.md) with a type of [`OS_SIGNPOST_INTERVAL_END`](./os_signpost_type_t/os_signpost_interval_end.md).

## Parameters

- `log`: A log object to log the signpost to.
- `interval_id`: A signpost identifier used to disambiguate between signposts with the same name.
- `name`: The name of the signpost.
- `…`: Optional. If specified, provide a format string, followed by the expected number of arguments in the order that they appear in the string.

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
- [os_signpost_event_emit](./os_signpost_event_emit.md)
  Marks a point of interest in time.
- [typealias os_signpost_id_t](./os_signpost_id_t.md)
  An identifier you use to distinguish between signposts that have the same name and destination log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_signpost_interval_end)*