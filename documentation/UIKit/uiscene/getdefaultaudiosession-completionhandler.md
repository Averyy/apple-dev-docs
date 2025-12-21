# getDefaultAudioSession(completionHandler:)

**Framework**: UIKit  
**Kind**: method

Retrieves the audio session that contains all sounds that implicitly belong to this scene.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
var defaultAudioSession: AVAudioSession? { get async }
```

#### Discussion

In visionOS, the default [`AVAudioSession`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession) for a [`UIScene`](uiscene.md) contains all of the RealityKit sounds from any [`RealityView`](https://developer.apple.com/documentation/RealityKit/RealityView) in the scene’s view hierarchy.

The default audio session’s initial configuration is mixable, with [`isNowPlayingCandidate`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession/isNowPlayingCandidate) set to [`false`](https://developer.apple.com/documentation/Swift/false). This configuration ensures that the scene’s default audio session doesn’t interfere with existing behavior of the app’s primary audio session, [`sharedInstance()`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession/sharedInstance()). However, you can modify the default audio session’s properties as needed.

You can safely call this method on a non-main thread. It’s recommended to get a scene’s default audio session from a non-main thread to avoid calling resource-intensive [`AVAudioSession`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession) interfaces from the main thread, which can have a negative impact on the responsiveness of the user experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/getdefaultaudiosession(completionhandler:))*