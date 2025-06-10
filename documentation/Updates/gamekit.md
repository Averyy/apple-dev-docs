# GameKit updates

**Framework**: Updates

Learn about important changes to GameKit.

#### Overview

Browse notable changes in [`GameKit`](https://developer.apple.com/documentation/GameKit).

#### June 2025

- Use a GameKit Configuration file in Xcode to configure Game Activities and Challenges.
- Test leaderboard score submissions by receiving system notifications when they happen. On iOS, open Settings > Developer, then turn on Notify About Score Submissions.
- Use [`GKGameActivity`](https://developer.apple.com/documentation/GameKit/GKGameActivity) to present players with ways to engage each other in your game.
- Configure challenges in Xcode or App Store Connect and use  [`GKChallengeDefinition`](https://developer.apple.com/documentation/GameKit/GKChallengeDefinition) to retrieve the metadata you define.

#### June 2024

##### Dashboard

- Create a [`GKGameCenterViewController`](https://developer.apple.com/documentation/GameKit/GKGameCenterViewController) object using the [`init(leaderboardSetID:)`](https://developer.apple.com/documentation/GameKit/GKGameCenterViewController/init(leaderboardSetID:)) initializer to display a set of leaderboards in the dashboard.
- Use the [`init(player:)`](https://developer.apple.com/documentation/GameKit/GKGameCenterViewController/init(player:)) initializer to display a player’s profile in the dashboard.

##### Voice Chat

- Use SharePlay to allow voice chat in your real-time games instead of [`GKVoiceChat`](https://developer.apple.com/documentation/GameKit/GKVoiceChat) which is deprecated. When you present a [`GKMatchmakerViewController`](https://developer.apple.com/documentation/GameKit/GKMatchmakerViewController) object, it automatically shows a SharePlay button on iOS. To implement a custom SharePlay experience, see [`GKMatchmaker`](https://developer.apple.com/documentation/GameKit/GKMatchmaker).

## See Also

- [Accelerate updates](accelerate.md)
  Learn about important changes to Accelerate.
- [Accessibility updates](accessibility.md)
  Learn about important changes to Accessibility.
- [ActivityKit updates](activitykit.md)
  Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](adattributionkit.md)
  Learn about important changes to AdAttributionKit.
- [App Clips updates](appclips.md)
  Learn about important changes in App Clips.
- [App Intents updates](appintents.md)
  Learn about important changes in App Intents.
- [AppKit updates](appkit.md)
  Learn about important changes to AppKit.
- [Apple Intelligence updates](apple-intelligence.md)
  Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](applemapsserverapi.md)
  Learn about important changes to AppleMapsServerAPI.
- [Apple Pencil updates](applepencil.md)
  Learn about important changes to Apple Pencil.
- [ARKit updates](arkit.md)
  Learn about important changes to ARKit.
- [Audio Toolbox updates](audiotoolbox.md)
  Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](authenticationservices.md)
  Learn about important changes to AuthenticationServices.
- [AVFAudio updates](avfaudio.md)
  Learn about important changes to AVFAudio.
- [AVFoundation updates](avfoundation.md)
  Learn about important changes to AVFoundation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/gamekit)*