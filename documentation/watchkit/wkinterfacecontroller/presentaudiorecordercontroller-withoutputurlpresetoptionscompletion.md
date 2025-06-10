# presentAudioRecorderController(withOutputURL:preset:options:completion:)

**Framework**: WatchKit  
**Kind**: method

Display a standard interface for recording audio from the user’s Apple Watch.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
func presentAudioRecorderController(withOutputURL URL: URL, preset: WKAudioRecorderPreset, options: [AnyHashable : Any]? = nil) async throws -> Bool
```

## Mentions

- [Navigating Between Scenes](navigating-between-scenes.md)

#### Discussion

Use this method to obtain recorded audio from the user. This method executes asynchronously, returning shortly after you call it. During a subsequent run loop cycle, the system displays the audio recording controller to the user. The interface includes a Cancel button to dismiss the interface, and controls to manage recording. After some audio has been recorded, the interface displays the title string specified in the [`WKAudioRecorderControllerOptionsActionTitleKey`](wkaudiorecordercontrolleroptionsactiontitlekey.md) option so that the user can accept the content and save it to the specified URL. When the user taps the Cancel button or your title string, WatchKit automatically dismisses the audio recording interface controller.

When the user dismisses the interface, or when you dismiss it programmatically, the system calls your completion block. Use that block to process the results.

Always call this method from your WatchKit extension’s main thread.

When specifying a filename with the `.wav` extension, the resulting audio format is LPCM. For all other file types, the audio format is AAC. For information about the audio recording options, see the values for [`WKAudioRecorderPreset`](wkaudiorecorderpreset.md).

> **Note**:  Do not attempt to record audio while gathering heart rate data using Health Kit. If you present a media interface, WatchKit automatically disables the gathering of heart rate data.

## Parameters

- `URL`: The URL at which to store the recorded output. The filename extension determines the type of audio to record. You may specify the extensions  ,  , and  .
- `preset`: The recording quality. Specify the constant that best represents the type of audio you want to record. For a list of possible values, see  .
- `options`: A dictionary of options to use during recording. If you specify   for this parameter, the audio recording interface uses the default options. For a list of keys and values you can include in the dictionary, see  .
- `completion`: The block to execute when recording ends. Use this block to determine the status of the recording and to perform any cleanup. This block has no return value and takes the following parameters:

## See Also

- [func presentMediaPlayerController(with: URL, options: [AnyHashable : Any]?, completion: (Bool, TimeInterval, (any Error)?) -> Void)](wkinterfacecontroller/presentmediaplayercontroller(with:options:completion:).md)
  Displays a modal interface for playing the specified media file.
- [Media Player Options](media-player-options.md)
  Keys indicating media playback options.
- [func dismissMediaPlayerController()](wkinterfacecontroller/dismissmediaplayercontroller.md)
  Dismisses the media interface controller.
- [enum WKAudioRecorderPreset](wkaudiorecorderpreset.md)
  Constants indicating the quality of audio recordings.
- [Audio Recording Options](audio-recording-options.md)
  Options to specify when recording audio.
- [func dismissAudioRecorderController()](wkinterfacecontroller/dismissaudiorecordercontroller.md)
  Dismisses the audio recording interface controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentaudiorecordercontroller(withoutputurl:preset:options:completion:))*