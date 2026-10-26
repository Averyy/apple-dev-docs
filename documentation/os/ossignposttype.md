# OSSignpostType

**Framework**: os  
**Kind**: struct  
**Role**: Structure

The different kinds of signpost.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

> **Deprecated**: Use [`OSSignposter`](./ossignposter.md) instead.

## Declaration

```swift
struct OSSignpostType
```

```c
typedef enum { ... } os_signpost_type_t;
```

## Topics

### Specifying Signpost Types
- [static let begin: OSSignpostType](./ossignposttype/begin.md)
  A signpost that marks the start of a time interval of interest in your code.
- [static let end: OSSignpostType](./ossignposttype/end.md)
  A signpost that marks the end of a time interval of interest in your code.
- [static let event: OSSignpostType](./ossignposttype/event.md)
  A signpost that marks an event in your code.
### Creating Signpost Types
- [init(rawValue: UInt8)](./ossignposttype/init%28rawvalue%29.md)
  Creates a signpost from a raw integer value.
- [init(UInt8)](./ossignposttype/init%28_%29.md)
  Creates a signpost from a raw integer value.
### Inspecting Signpost Types
- [var rawValue: UInt8](./ossignposttype/rawvalue.md)
  An integer value that represents the role of a signpost.
### Enumeration Cases
- [OS_SIGNPOST_EVENT](./os_signpost_type_t/os_signpost_event.md)
  A signpost that marks an event in your code.
- [OS_SIGNPOST_INTERVAL_BEGIN](./os_signpost_type_t/os_signpost_interval_begin.md)
  A signpost that marks the start of a time interval of interest in your code.
- [OS_SIGNPOST_INTERVAL_END](./os_signpost_type_t/os_signpost_interval_end.md)
  A signpost that marks the end of a time interval of interest in your code.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Measure Events
- [Recording Performance Data](./recording-performance-data.md)
  Add signposts to record interesting time-based events.
- [struct OSSignposter](./ossignposter.md)
  An object for measuring task performance using the unified logging system.
- [Legacy Signpost Symbols](./legacy-signpost-symbols.md)
  Migrate your code away from using these legacy symbols.
- [typealias os_signpost_id_t](./os_signpost_id_t.md)
  An identifier you use to distinguish between signposts that have the same name and destination log.
- [os_signpost_emit_with_type](./os_signpost_emit_with_type.md)
  Logs a point of interest in your code as a time interval or as an event for debugging performance in Instruments.
- [os_signpost_interval_begin](./os_signpost_interval_begin.md)
  Marks the start of a time interval in your code using a signpost.
- [os_signpost_interval_end](./os_signpost_interval_end.md)
  Marks the end of a time interval in your code using a signpost.
- [os_signpost_event_emit](./os_signpost_event_emit.md)
  Marks a point of interest in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/ossignposttype)*