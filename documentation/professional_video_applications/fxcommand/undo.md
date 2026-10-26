# FxCommand.undo

**Framework**: Professional Video Applications  
**Kind**: case  
**Role**: Case

Undo the last change.

**Availability**:
- FxPlug 4.1+

## Declaration

```swift
case undo
```

```c
kFxCommand_Undo
```

## See Also

### Enumeration Cases
- [FxCommand.previousFrame](./previousframe.md)
  Move the playhead back 1 frame.
- [FxCommand.nextFrame](./nextframe.md)
  Move the playhead ahead 1 frame.
- [FxCommand.previousEdit](./previousedit.md)
  Move the playhead to the previous edit in FCPX or the selection in point in Motion.
- [FxCommand.nextEdit](./nextedit.md)
  Move the playhead to the next edit in FCPX or the selection out point in Motion.
- [FxCommand.previousMarker](./previousmarker.md)
  Move the playhead to the previous marker of the currently selected object.
- [FxCommand.nextMarker](./nextmarker.md)
  Move the playhead to the next marker of the currently selected object.
- [FxCommand.previousKeyframe](./previouskeyframe.md)
  Move the playhead to the previous keyframe of the currently selected object.
- [FxCommand.nextKeyframe](./nextkeyframe.md)
  Move the playhead to the next keyframe of the currently selected object.
- [FxCommand.reversePlayback](./reverseplayback.md)
  Jog in reverse (unavailable in Motion).
- [FxCommand.pausePlayback](./pauseplayback.md)
  Pauses playback in FCPX. In Motion, use TogglePlayback instead.
- [FxCommand.forwardPlayback](./forwardplayback.md)
  Jog forward (use TogglePlayback in Motion).
- [FxCommand.togglePlayback](./toggleplayback.md)
  If paused, starts playback; if playing back, pauses.
- [FxCommand.redo](./redo.md)
  Redo the last undone change.
- [FxCommand.toggleWaveforms](./togglewaveforms.md)
  Show the waveforms scope in FCPX (unavailable in Motion).
- [FxCommand.toggleInspectorHeight](./toggleinspectorheight.md)
  Toggles the full-height inspector in FCPX (Motion’s Inspector is always full-height).


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxcommand/undo)*