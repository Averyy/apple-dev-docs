# FCPXSequenceTimecodeFormat

**Framework**: Professional Video Applications  
**Kind**: enum  
**Role**: Enumeration

The display format of the sequence timecode.

**Availability**:
- ProVideo Workflow Extensions 1.0+

## Declaration

```swift
enum FCPXSequenceTimecodeFormat
```

```c
enum FCPXSequenceTimecodeFormat: NSInteger;
```

## Topics

### Sequence Timecode Formats
- [FCPXSequenceTimecodeFormat.dropFrame](./fcpxsequencetimecodeformat/dropframe.md)
  A value that indicates drop-frame timecode format.
- [FCPXSequenceTimecodeFormat.nonDropFrame](./fcpxsequencetimecodeformat/nondropframe.md)
  A value that indicates non-drop-frame timecode format.
- [FCPXSequenceTimecodeFormat.unspecified](./fcpxsequencetimecodeformat/unspecified.md)
  An unspecified timecode format.
### Initializers
- [init?(rawValue: Int)](./fcpxsequencetimecodeformat/init%28rawvalue%29.md)
### Default Implementations
- [Equatable Implementations](./fcpxsequencetimecodeformat/equatable-implementations.md)
- [RawRepresentable Implementations](./fcpxsequencetimecodeformat/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### FCPX Timeline Proxy Objects
- [class FCPXObject](./fcpxobject.md)
  An abstract superclass for Final Cut Pro timeline proxy objects.
- [enum FCPXObjectType](./fcpxobjecttype.md)
  The Final Cut Pro timeline object types.
- [class FCPXLibrary](./fcpxlibrary.md)
  An object that contains details of a Final Cut Pro library.
- [class FCPXEvent](./fcpxevent.md)
  An object that contains details of an event in the Final Cut Pro library.
- [class FCPXProject](./fcpxproject.md)
  An object that contains details of a project with the sequence open in the Final Cut Pro timeline.
- [class FCPXSequence](./fcpxsequence.md)
  An object that contains details of a sequence that’s open in the Final Cut Pro timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fcpxsequencetimecodeformat)*