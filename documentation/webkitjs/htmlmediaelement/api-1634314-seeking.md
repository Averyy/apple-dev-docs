# seeking

**Framework**: WebKit JS  
**Kind**: instp  
**Role**: Instance Property

A Boolean value that indicates whether the element is seeking. (read-only)

**Availability**:
- Safari Desktop 3.1+
- Safari Mobile 3.0+

## Declaration

```
readonly attribute boolean seeking;
```

## Discussion

If `true`, the media resource is playing in a nonlinear fashion; otherwise, it is not.

## See Also

### Getting State
- [buffered](./api-1628987-buffered.md)
  The time ranges of the media resource that have been downloaded. (read-only)
- [currentSrc](./api-1633960-currentsrc.md)
  The absolute URL of the media resource. (read-only)
- [duration](./api-1630916-duration.md)
  The length of the media resource in seconds. (read-only)
- [ended](./api-1630452-ended.md)
  A Boolean value that indicates whether the media played to the end. (read-only)
- [error](./api-1630743-error.md)
  The last error that occurred for this element. (read-only)
- [networkState](./api-1633289-networkstate.md)
  The state of downloading the media resource. (read-only)
- [paused](./api-1631769-paused.md)
  A Boolean value that indicates whether the media is paused. (read-only)
- [played](./api-1629079-played.md)
  The ranges of the media resource that was played. (read-only)
- [readyState](./api-1632439-readystate.md)
  The ready state of the media resource. (read-only)
- [seekable](./api-1633602-seekable.md)
  The ranges that can be played in a nonlinear fashion. (read-only)
- [startTime](./api-1805533-starttime.md)
  The earliest possible time in seconds to start playback. (read-only)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/htmlmediaelement/1634314-seeking)*