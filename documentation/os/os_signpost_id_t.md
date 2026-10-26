# os_signpost_id_t

**Framework**: os  
**Kind**: typealias  
**Role**: Type Alias

An identifier you use to distinguish between signposts that have the same name and destination log.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias os_signpost_id_t = UInt64
```

```c
typedef uint64_t os_signpost_id_t;
```

#### Discussion

Multiple intervals with matching log objects and interval names can be in-flight simultaneously. In order for data-processing tools to correctly match the beginning and end of an interval, you need to identify each interval with a unique signpost identifier. Use the first strategy in the list below that matches your use case:

- If you can guarantee that intervals with the same log and name can never overlap in time, specify [`OS_SIGNPOST_ID_EXCLUSIVE`](./os_signpost_id_exclusive.md) as the signpost ID.
- If you already have your own integer data that can uniquely identify each instance of the task being measured, cast the data from a [`uint64_t`](../kernel/uint64_t.md) value directly to a `os_signpost_id_t`. The value must not match one of the predefined signpost values.
- If you have a pointer that can uniquely identify begin/end pairs (such as a pointer to a data object used by the code being measured), call [`os_signpost_id_make_with_pointer`](./os_signpost_id_make_with_pointer.md). Don’t use this function for signposts that span process boundaries.
- Otherwise, call [`os_signpost_id_generate`](./os_signpost_id_generate.md) each time you create a new pair of signposts to generate a unique value for that pair.

## Topics

### Creating a Signpost Identifier
- [os_signpost_id_generate](./os_signpost_id_generate.md)
  Creates a signpost identifier that’s unique among signposts logged to a specified log.
- [os_signpost_id_make_with_pointer](./os_signpost_id_make_with_pointer.md)
  Creates a signpost identifier that’s unique among signposts logging to the specified log, using a pointer value to generate the unique value.
### Using Built-in Signpost Identifiers
- [OS_SIGNPOST_ID_EXCLUSIVE](./os_signpost_id_exclusive.md)
  A signpost identifier that indicates no overlap among different signpost time intervals.
- [OS_SIGNPOST_ID_INVALID](./os_signpost_id_invalid.md)
  A signpost identifier that indicates an error.
- [OS_SIGNPOST_ID_NULL](./os_signpost_id_null.md)
  The signpost identifier that represents a disabled signpost.
### Supporting Types
- [OS_SIGNPOST_TYPE_MASK](./os_signpost_type_mask.md)
  A value the system uses to create built-in signpost identifiers; don’t use directly.

## See Also

### Measure Events
- [Recording Performance Data](./recording-performance-data.md)
  Add signposts to record interesting time-based events.
- [struct OSSignposter](./ossignposter.md)
  An object for measuring task performance using the unified logging system.
- [Legacy Signpost Symbols](./legacy-signpost-symbols.md)
  Migrate your code away from using these legacy symbols.
- [struct OSSignpostType](./ossignposttype.md)
  The different kinds of signpost.
- [os_signpost_emit_with_type](./os_signpost_emit_with_type.md)
  Logs a point of interest in your code as a time interval or as an event for debugging performance in Instruments.
- [os_signpost_interval_begin](./os_signpost_interval_begin.md)
  Marks the start of a time interval in your code using a signpost.
- [os_signpost_interval_end](./os_signpost_interval_end.md)
  Marks the end of a time interval in your code using a signpost.
- [os_signpost_event_emit](./os_signpost_event_emit.md)
  Marks a point of interest in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_signpost_id_t)*