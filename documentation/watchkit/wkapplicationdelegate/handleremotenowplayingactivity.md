# handleRemoteNowPlayingActivity()

**Framework**: Watchkit  
**Kind**: method

Tells the delegate when the user plays audio in the corresponding iOS app.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor optional func handleRemoteNowPlayingActivity()
```

## Overview

Use this method to update your user interface and display information about the iOS app’s content.

When the user begins playing audio content on the corresponding iOS app, your watch app automatically launches and becomes the frontmost app, similar to the behavior of the Now Playing app. It remains the frontmost app until the user pauses the audio or exits your watch app.

To opt out of this autolaunch behavior, set the Opt out of Auto-launch Audio App (`PUICAutoLaunchAudioOptOut`) key in your watchOS app’s `info.plist` file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/handleremotenowplayingactivity())*