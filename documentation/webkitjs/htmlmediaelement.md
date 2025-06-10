# HTMLMediaElement

**Framework**: WebKit JS  
**Kind**: cl

An abstract superclass for media classes that display audio or video in webpages. This class defines common properties and methods inherited by the [`HTMLAudioElement`](htmlaudioelement.md) and [`HTMLVideoElement`](htmlvideoelement.md) classes representing the HTML `audio` and `video` elements.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 3.0+

## Declaration

```swift
interface HTMLMediaElement
```

#### Overview

##### 1664118

The different types of media events that can occur are described in [`Table 1`](htmlmediaelement#1965705.md).

| Event | Description |
| --- | --- |
| `abort` | Sent when the browser stops fetching the media data before the media resource was completely downloaded. |
| `canplay` | Sent when the browser can resume playback of the media data, but estimates that if playback is started now, the media resource could not be rendered at the current playback rate up to its end without having to stop for further buffering of content. |
| `canplaythrough` | Sent when the browser estimates that if playback is started now, the media resource could be rendered at the current playback rate all the way to its end without having to stop for further buffering. |
| `durationchange` | Sent when the [`duration`](htmlmediaelement/1630916-duration.md) property changes. |
| `emptied` | Sent when the media element network state changes to the  [`NETWORK_EMPTY`](htmlmediaelement/1629429-network_empty.md) state. |
| `ended` | Sent when playback has stopped at the end of the media resource and the [`ended`](htmlmediaelement/1630452-ended.md) property is set to `true`. |
| `error` | Sent when an error occurs while fetching the media data. Use the [`error`](htmlmediaelement/1630743-error.md) property to get the current error. |
| `loadeddata` | Sent when the browser can render the media data at the current playback position for the first time. |
| `loadedmetadata` | Sent when the browser knows the duration and dimensions of the media resource. |
| `loadstart` | Sent when the browser begins loading the media data. |
| `pause` | Sent when playback pauses after the [`pause`](htmlmediaelement/1633571-pause.md) method returns. |
| `play` | Sent when playback starts after the [`play`](htmlmediaelement/1630114-play.md) method returns. |
| `playing` | Sent when playback starts. |
| `progress` | Sent when the browser is fetching the media data. |
| `ratechange` | Sent when either the [`defaultPlaybackRate`](htmlmediaelement/1631650-defaultplaybackrate.md) or the  [`playbackRate`](htmlmediaelement/1629746-playbackrate.md) property changes. |
| `seeked` | Sent when the [`seeking`](htmlmediaelement/1634314-seeking.md) property is set to `false` |
| `seeking` | Sent when the [`seeking`](htmlmediaelement/1634314-seeking.md) property is set to `true` and there is time to send this event. |
| `stalled` | Sent when the browser is fetching media data but it has stopped arriving. |
| `suspend` | Sent when the browser suspends loading the media data and does not have the entire media resource downloaded. |
| `timeupdate` | Sent when the [`currentTime`](htmlmediaelement/1631307-currenttime.md) property changes as part of normal playback or because of some other condition. |
| `volumechange` | Sent when either the [`volume`](htmlmediaelement/1631549-volume.md) property or the [`muted`](htmlmediaelement/1630580-muted.md) property changes. |
| `waiting` | Sent when the browser stops playback because it is waiting for the next frame. |

## Topics

### Getting and Setting Properties
- [autoplay](htmlmediaelement/1629662-autoplay.md)
  A Boolean value that determines whether the media resource plays automatically when available.
- [controls](htmlmediaelement/1631980-controls.md)
  A Boolean value that determines whether the playback controls appear.
- [currentTime](htmlmediaelement/1631307-currenttime.md)
  The current playback position in seconds.
- [defaultPlaybackRate](htmlmediaelement/1631650-defaultplaybackrate.md)
  The default rate used to play the media resource.
- [loop](htmlmediaelement/1633760-loop.md)
  A Boolean value that determines whether the playback should loop.
- [muted](htmlmediaelement/1630580-muted.md)
  A Boolean value that determines whether the audio content should be muted.
- [playbackRate](htmlmediaelement/1629746-playbackrate.md)
  The speed that the media resource is playing.
- [preload](htmlmediaelement/1633059-preload.md)
  A DOMString value that gives a hint to the browser how much of the media should be fetched when the webpage is loaded.
- [src](htmlmediaelement/1629312-src.md)
  The URI address of the media resource to play.
- [volume](htmlmediaelement/1631549-volume.md)
  The volume of the audio portion of the media element.
### Getting State
- [buffered](htmlmediaelement/1628987-buffered.md)
  The time ranges of the media resource that have been downloaded. (read-only)
- [currentSrc](htmlmediaelement/1633960-currentsrc.md)
  The absolute URL of the media resource. (read-only)
- [duration](htmlmediaelement/1630916-duration.md)
  The length of the media resource in seconds. (read-only)
- [ended](htmlmediaelement/1630452-ended.md)
  A Boolean value that indicates whether the media played to the end. (read-only)
- [error](htmlmediaelement/1630743-error.md)
  The last error that occurred for this element. (read-only)
- [networkState](htmlmediaelement/1633289-networkstate.md)
  The state of downloading the media resource. (read-only)
- [paused](htmlmediaelement/1631769-paused.md)
  A Boolean value that indicates whether the media is paused. (read-only)
- [played](htmlmediaelement/1629079-played.md)
  The ranges of the media resource that was played. (read-only)
- [readyState](htmlmediaelement/1632439-readystate.md)
  The ready state of the media resource. (read-only)
- [seekable](htmlmediaelement/1633602-seekable.md)
  The ranges that can be played in a nonlinear fashion. (read-only)
- [seeking](htmlmediaelement/1634314-seeking.md)
  A Boolean value that indicates whether the element is seeking. (read-only)
- [startTime](htmlmediaelement/1805533-starttime.md)
  The earliest possible time in seconds to start playback. (read-only)
### Controlling Playback
- [canPlayType](htmlmediaelement/1630268-canplaytype.md)
  Returns whether the media element supports the specified MIME type.
- [load](htmlmediaelement/1629903-load.md)
  Starts loading the media resource.
- [pause](htmlmediaelement/1633571-pause.md)
  Pauses the media playback if in progress.
- [play](htmlmediaelement/1630114-play.md)
  Begins playing the media resource.
### Constants
- [Media Ready States](htmlmediaelement/media_ready_states.md)
  Possible values for the [`readyState`](htmlmediaelement/1632439-readystate.md) property.
- [Network States](htmlmediaelement/network_states.md)
  Possible values for the [`networkState`](htmlmediaelement/1633289-networkstate.md) property.
### Instance Properties
- [audioTracks](htmlmediaelement/1634091-audiotracks.md)
- [controller](htmlmediaelement/1634496-controller.md)
- [crossOrigin](htmlmediaelement/2528116-crossorigin.md)
- [defaultMuted](htmlmediaelement/1632461-defaultmuted.md)
- [kind](htmlmediaelement/1634181-kind.md)
- [mediaGroup](htmlmediaelement/1632684-mediagroup.md)
- [session](htmlmediaelement/1633703-session.md)
- [srcObject](htmlmediaelement/1630228-srcobject.md)
- [textTracks](htmlmediaelement/1628855-texttracks.md)
- [videoTracks](htmlmediaelement/1632338-videotracks.md)
- [webkitClosedCaptionsVisible](htmlmediaelement/1629386-webkitclosedcaptionsvisible.md)
- [webkitCurrentPlaybackTargetIsWireless](htmlmediaelement/1634003-webkitcurrentplaybacktargetiswir.md)
- [webkitHasClosedCaptions](htmlmediaelement/1633311-webkithasclosedcaptions.md)
- [webkitKeys](htmlmediaelement/1633588-webkitkeys.md)
- [webkitPreservesPitch](htmlmediaelement/1631414-webkitpreservespitch.md)
### Instance Methods
- [addTextTrack](htmlmediaelement/1630850-addtexttrack.md)
- [fastSeek](htmlmediaelement/1629646-fastseek.md)
- [getStartDate](htmlmediaelement/1634352-getstartdate.md)
- [getVideoPlaybackQuality](htmlmediaelement/1633900-getvideoplaybackquality.md)
- [webkitSetMediaKeys](htmlmediaelement/1633293-webkitsetmediakeys.md)
- [webkitShowPlaybackTargetPicker](htmlmediaelement/1632172-webkitshowplaybacktargetpicker.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/htmlmediaelement)*