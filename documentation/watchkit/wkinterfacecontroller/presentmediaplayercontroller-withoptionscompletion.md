# presentMediaPlayerController(with:options:completion:)

**Framework**: Watchkit  
**Kind**: method

Displays a modal interface for playing the specified media file.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor func presentMediaPlayerController(with URL: URL, options: [AnyHashable : Any]? = nil) async throws -> (Bool, TimeInterval)
```

## Mentions

- [Navigating Between Scenes](navigating-between-scenes.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/navigating-between-scenes))

## Overview

Use this method to present short media clips to the user. This method executes asynchronously, returning shortly after you call it. During a subsequent run loop cycle, the system presents a media interface controller over the current interface controller. For video, the interface controller displays the video content along with controls to start and stop playback. For audio, the interface controller displays information about the content being played. Always call this method from your WatchKit extension’s main thread.

When the user dismisses the interface, or when you dismiss the media player programmatically, WatchKit calls the block provided in the `completion` parameter. Use that block to find out how much of the media file was played or other relevant information. For example, you might note the stopping point and start playback of the same clip from that point later.

The following table lists the encoding information to use when creating media files. For audio and video assets played directly from your app, keep your clips relatively short. Short clips consume less space on disk, use less power, and take less time to download.

| r | o | w |
| --- | --- | --- |
| [{'inlineContent': [{'text': 'Media type', 'type': 'text'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'Recommended encoding'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'text': 'Video assets', 'type': 'text'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': 'Video codec: H.264 High Profile ', 'type': 'text'}, {'type': 'image', 'identifier': 'spacer'}, {'text': ' Bit rate: 160 kpbs at up to 30 fps ', 'type': 'text'}, {'type': 'image', 'identifier': 'spacer'}, {'text': ' Full screen resolution: 208 x 260 in portrait orientation ', 'type': 'text'}, {'type': 'image', 'identifier': 'spacer'}, {'text': ' 16:9 resolution: 320 x 180 in landscape orientation ', 'type': 'text'}, {'type': 'image', 'identifier': 'spacer'}, {'text': ' Audio bit rate: 32 kpbs stereo', 'type': 'text'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'type': 'text', 'text': 'Audio-only assets'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': 'Bit rate: 32 kbps stereo', 'type': 'text'}], 'type': 'paragraph'}] |

> **Note**:  Do not attempt to play audio or video content while gathering heart rate data using Health Kit. If you present a media interface, WatchKit automatically disables the gathering of heart rate data.

 Do not attempt to play audio or video content while gathering heart rate data using Health Kit. If you present a media interface, WatchKit automatically disables the gathering of heart rate data.

Any audio you play using this method is routed to a paired Bluetooth audio device if one is available. If no Bluetooth audio device is available, audio is routed to to the Apple Watch speaker.

## Parameters

- `URL`: If you specify a URL for a file on a remote server, this method downloads the file first and displays a progress indicator showing the progress of the operation. Because WatchKit uses App Transport Security (ATS) when downloading files from a web server, the file must be on a secure server, and the URL must use the   scheme. If your server does not support ATS–level security, download the file yourself before playing it.
- `options`: An optional dictionary of playback options for the media file. For a list of keys to include in the dictionary, see  .
- `completion`: The block to execute when playback ends. Use this block to determine the status of playback and to perform any cleanup. This block has no return value and takes the following parameters:

## See Also

- [Media Player Options](media-player-options.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/media-player-options))
- [func dismissMediaPlayerController()](dismissmediaplayercontroller().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismissmediaplayercontroller()))
- [func presentAudioRecorderController(withOutputURL: URL, preset: WKAudioRecorderPreset, options: [AnyHashable : Any]?, completion: (Bool, (any Error)?) -> Void)](presentaudiorecordercontroller(withoutputurl:preset:options:completion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentaudiorecordercontroller(withoutputurl:preset:options:completion:)))
- [enum WKAudioRecorderPreset](wkaudiorecorderpreset.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiorecorderpreset))
- [Audio Recording Options](audio-recording-options.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/audio-recording-options))
- [func dismissAudioRecorderController()](dismissaudiorecordercontroller().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismissaudiorecordercontroller()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentmediaplayercontroller(with:options:completion:))*