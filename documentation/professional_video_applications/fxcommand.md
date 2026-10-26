# FxCommand

**Framework**: Professional Video Applications  
**Kind**: enum  
**Role**: Enumeration

Defines the commands that can be performed by the host.

**Availability**:
- FxPlug 4.1+

## Declaration

```swift
enum FxCommand
```

```c
enum FxCommand: NSUInteger;
```

## Topics

### Enumeration Cases
- [FxCommand.previousFrame](./fxcommand/previousframe.md)
  Move the playhead back 1 frame.
- [FxCommand.nextFrame](./fxcommand/nextframe.md)
  Move the playhead ahead 1 frame.
- [FxCommand.previousEdit](./fxcommand/previousedit.md)
  Move the playhead to the previous edit in FCPX or the selection in point in Motion.
- [FxCommand.nextEdit](./fxcommand/nextedit.md)
  Move the playhead to the next edit in FCPX or the selection out point in Motion.
- [FxCommand.previousMarker](./fxcommand/previousmarker.md)
  Move the playhead to the previous marker of the currently selected object.
- [FxCommand.nextMarker](./fxcommand/nextmarker.md)
  Move the playhead to the next marker of the currently selected object.
- [FxCommand.previousKeyframe](./fxcommand/previouskeyframe.md)
  Move the playhead to the previous keyframe of the currently selected object.
- [FxCommand.nextKeyframe](./fxcommand/nextkeyframe.md)
  Move the playhead to the next keyframe of the currently selected object.
- [FxCommand.reversePlayback](./fxcommand/reverseplayback.md)
  Jog in reverse (unavailable in Motion).
- [FxCommand.pausePlayback](./fxcommand/pauseplayback.md)
  Pauses playback in FCPX. In Motion, use TogglePlayback instead.
- [FxCommand.forwardPlayback](./fxcommand/forwardplayback.md)
  Jog forward (use TogglePlayback in Motion).
- [FxCommand.togglePlayback](./fxcommand/toggleplayback.md)
  If paused, starts playback; if playing back, pauses.
- [FxCommand.undo](./fxcommand/undo.md)
  Undo the last change.
- [FxCommand.redo](./fxcommand/redo.md)
  Redo the last undone change.
- [FxCommand.toggleWaveforms](./fxcommand/togglewaveforms.md)
  Show the waveforms scope in FCPX (unavailable in Motion).
- [FxCommand.toggleInspectorHeight](./fxcommand/toggleinspectorheight.md)
  Toggles the full-height inspector in FCPX (Motion’s Inspector is always full-height).
- [FxCommand.toggleSidebar](./fxcommand/togglesidebar.md)
  Toggles the Sidebar in FCPX or the Library in Motion.
- [FxCommand.toggleEvents](./fxcommand/toggleevents.md)
  Toggles the event viewer in FCPX or the Media tab in Motion.
- [FxCommand.preferences](./fxcommand/preferences.md)
  Shows the application’s preferences.
### Initializers
- [init?(rawValue: UInt)](./fxcommand/init%28rawvalue%29.md)
### Default Implementations
- [Equatable Implementations](./fxcommand/equatable-implementations.md)
- [RawRepresentable Implementations](./fxcommand/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Handling and Defining Commands
- [protocol FxCommandHandler](./fxcommandhandler.md)
  Defines the methods a plug-in must implement to be notified of the application’s key binding for common commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxcommand)*