# getDefaultAudioSession(completionHandler:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Retrieves the audio session that contains all sounds that implicitly belong to this scene.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
func getDefaultAudioSession(completionHandler handler: @escaping @Sendable (AVAudioSession?) -> Void)
```

```swift
nonisolated
var defaultAudioSession: AVAudioSession? { get async }
```

```objc
- (void) getDefaultAudioSessionWithCompletionHandler:(void (^)(AVAudioSession *)) handler;
```

#### Discussion

In visionOS, the default [`AVAudioSession`](../../AVFAudio/avaudiosession.md) for a [`UIScene`](../uiscene.md) contains all of the RealityKit sounds from any [`RealityView`](../../RealityKit/realityview.md) in the scene’s view hierarchy.

The default audio session’s initial configuration is mixable, with [`isNowPlayingCandidate`](../../AVFAudio/avaudiosession/isnowplayingcandidate.md) set to [`false`](../../Swift/false.md). This configuration ensures that the scene’s default audio session doesn’t interfere with existing behavior of the app’s primary audio session, [`sharedInstance()`](../../AVFAudio/avaudiosession/sharedinstance%28%29.md). However, you can modify the default audio session’s properties as needed.

You can safely call this method on a non-main thread. It’s recommended to get a scene’s default audio session from a non-main thread to avoid calling resource-intensive [`AVAudioSession`](../../AVFAudio/avaudiosession.md) interfaces from the main thread, which can have a negative impact on the responsiveness of the user experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/getdefaultaudiosession(completionhandler:))*