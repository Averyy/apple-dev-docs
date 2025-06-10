# XPC updates

**Framework**: Updates

Learn about important changes to XPC.

#### Overview

Browse notable changes in [`XPC`](https://developer.apple.comhttps://developer.apple.com/documentation/xpc).

#### March 2024

##### Security

- Test whether the peer executable that communicates with your app over an XPC connection has an expected entitlement by calling [`xpc_connection_set_peer_entitlement_exists_requirement(_:_:)`](https://developer.apple.com/documentation/XPC/xpc_connection_set_peer_entitlement_exists_requirement(_:_:)), and whether it has a specific value for an entitlement by calling [`xpc_connection_set_peer_entitlement_matches_value_requirement(_:_:_:)`](https://developer.apple.com/documentation/XPC/xpc_connection_set_peer_entitlement_matches_value_requirement(_:_:_:)).
- Test whether the peer executable that communicates with your app over an XPC connection is an Apple platform binary with a given signing identifier by calling [`xpc_connection_set_peer_platform_identity_requirement(_:_:)`](https://developer.apple.com/documentation/XPC/xpc_connection_set_peer_platform_identity_requirement(_:_:)).
- Test whether your Apple Developer team signed the peer executable that communicates with your app over an XPC connection by calling [`xpc_connection_set_peer_team_identity_requirement(_:_:)`](https://developer.apple.com/documentation/XPC/xpc_connection_set_peer_team_identity_requirement(_:_:)).
- Test whether the peer executable that communicates with your app over an XPC connection satisfies a lightweight code requirement by calling [`xpc_connection_set_peer_lightweight_code_requirement(_:_:)`](https://developer.apple.com/documentation/XPC/xpc_connection_set_peer_lightweight_code_requirement(_:_:)).

#### June 2023

- Create XPC services using native Swift syntax. Use [`XPCListener`](https://developer.apple.com/documentation/XPC/XPCListener) to create an XPC server that listens for messages from other processes. Use [`XPCSession`](https://developer.apple.com/documentation/XPC/XPCSession) to create clients that connect to servers and exchange messages.
- For C and Objective-C projects, use the corresponding [`xpc_listener_t`](https://developer.apple.com/documentation/XPC/xpc_listener_t) and [`xpc_session_t`](https://developer.apple.com/documentation/XPC/xpc_session_t-10if0) APIs.
- In Xcode, use the updated XPC services target template to choose whether you want to use the high-level [`NSXPCConnection`](https://developer.apple.com/documentation/Foundation/NSXPCConnection) or the low-level `libXPC` APIs.

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

*[View on Apple Developer](https://developer.apple.com/documentation/updates/xpc)*