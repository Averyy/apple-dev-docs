# PlaybackOptions.LoopOption

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The behavior of playback when it reaches the end time.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string PlaybackOptions.LoopOption
```

## Discussion

This value takes one of the following forms:

- `back_and_forth`: Plays the media repeatedly forward from `start_time` to `end_time` and then backward from `end_time` to `start_time`. Not supported by all media; `none` is used instead. Shown in Keynote as Loop Back and Forth.
- `none`: Plays the media once through and then stops.
- `repeating`: Plays the media repeatedly from `start_time` to `end_time`. Shown in Keynote as Loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/playbackoptions.loopoption)*