# FCPXObjectType

**Framework**: Professional Video Applications  
**Kind**: enum  
**Role**: Enumeration

The Final Cut Pro timeline object types.

**Availability**:
- ProVideo Workflow Extensions 1.0+

## Declaration

```swift
enum FCPXObjectType
```

```c
enum FCPXObjectType: NSInteger;
```

## Topics

### Final Cut Pro Timeline Object Types
- [FCPXObjectType.event](./fcpxobjecttype/event.md)
  A Final Cut Pro timeline event.
- [FCPXObjectType.library](./fcpxobjecttype/library.md)
  A Final Cut Pro timeline library.
- [FCPXObjectType.project](./fcpxobjecttype/project.md)
  A Final Cut Pro timeline project.
- [FCPXObjectType.sequence](./fcpxobjecttype/sequence.md)
  A Final Cut Pro timeline sequence.
### Initializers
- [init?(rawValue: Int)](./fcpxobjecttype/init%28rawvalue%29.md)
### Default Implementations
- [Equatable Implementations](./fcpxobjecttype/equatable-implementations.md)
- [RawRepresentable Implementations](./fcpxobjecttype/rawrepresentable-implementations.md)

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
- [class FCPXLibrary](./fcpxlibrary.md)
  An object that contains details of a Final Cut Pro library.
- [class FCPXEvent](./fcpxevent.md)
  An object that contains details of an event in the Final Cut Pro library.
- [class FCPXProject](./fcpxproject.md)
  An object that contains details of a project with the sequence open in the Final Cut Pro timeline.
- [class FCPXSequence](./fcpxsequence.md)
  An object that contains details of a sequence that’s open in the Final Cut Pro timeline.
- [enum FCPXSequenceTimecodeFormat](./fcpxsequencetimecodeformat.md)
  The display format of the sequence timecode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fcpxobjecttype)*