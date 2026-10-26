# os_signpost_emit_with_type

**Framework**: os  
**Kind**: macro  
**Role**: Macro

Logs a point of interest in your code as a time interval or as an event for debugging performance in Instruments.

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
#define os_signpost_emit_with_type(log, type, spid, name, ...)
```

## Parameters

- `log`: A log object to log the signpost to.
- `type`: The type of signpost to log.
- `spid`: A signpost identifier used to disambiguate between signposts with the same name.
- `name`: The name of the signpost.
- `…`: Optional. If specified, provide a format string, followed by the expected number of arguments in the order that they appear in the string.

## See Also

### Measure Events
- [Recording Performance Data](./recording-performance-data.md)
  Add signposts to record interesting time-based events.
- [Legacy Signpost Symbols](./legacy-signpost-symbols.md)
  Migrate your code away from using these legacy symbols.
- [struct OSSignpostType](./ossignposttype.md)
  The different kinds of signpost.
- [os_signpost_interval_begin](./os_signpost_interval_begin.md)
  Marks the start of a time interval in your code using a signpost.
- [os_signpost_interval_end](./os_signpost_interval_end.md)
  Marks the end of a time interval in your code using a signpost.
- [os_signpost_event_emit](./os_signpost_event_emit.md)
  Marks a point of interest in time.
- [typealias os_signpost_id_t](./os_signpost_id_t.md)
  An identifier you use to distinguish between signposts that have the same name and destination log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_signpost_emit_with_type)*