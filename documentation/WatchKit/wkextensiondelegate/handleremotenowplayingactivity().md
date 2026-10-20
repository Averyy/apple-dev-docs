# handleRemoteNowPlayingActivity()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the user plays audio in the corresponding iOS app.

**Availability**:
- watchOS 5.0+ - Deprecated in 9.2

## Declaration

```swift
optional func handleRemoteNowPlayingActivity()
```

```objc
- (void) handleRemoteNowPlayingActivity;
```

#### Discussion

Use this method to update your user interface and display information about the iOS app’s content.

When the user begins playing audio content on the corresponding iOS app, your watch app automatically launches and becomes the frontmost app, similar to the behavior of the Now Playing app. It remains the frontmost app until the user pauses the audio or exits your watch app.

To opt out of this autolaunch behavior, set the Opt out of Auto-launch Audio App (`PUICAutoLaunchAudioOptOut`) key in your WatchKit extension’s `Info.plist` file, as shown in [Figure 1](./api-2980708-handleremotenowplayingactivity.md#3002766).

![A screenshot showing the Opt out of Auto-launch Audio App key in the Info.plist editor.](https://developer.apple.com/tutorials/images/com.apple.watchkit/media-3002766@2x.png)


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handleremotenowplayingactivity())*