# iOS & iPadOS 27.2 Release Notes

**Framework**: iOS & iPadOS Release Notes  
**Role**: Article

Update your apps to use new features, and test your apps against API changes.

#### Overview

The iOS & iPadOS 27.2 SDK provides support to develop apps for iPhone and iPad running iOS & iPadOS 27.2. The SDK comes bundled with Xcode 27.2. For information on the compatibility requirements for Xcode 27.2, see [Xcode 27.2 Release Notes](../Xcode-Release-Notes/xcode-27_2-release-notes.md).

##### App Tracking Transparency

###### New Features

- `AppTrackingTransparency` ([ATT](../AppTrackingTransparency/AppTrackingTransparency.md)) now supports an alternative expanded prompt and reprompting on a yearly basis for EU users. The alternative prompt is required for users in France, Germany, Italy, Poland, and Romania. (179504171)

###### Resolved Issues

- Fixed: The new `requestTrackingAuthorization(usingExpandedInterface:additionalInformationAction:completionHandler:)` API is renamed to `requestTrackingAuthorization(preferExpandedInterface:...)`. (187149729)
- Fixed: The new `requestTrackingAuthorizationPreferExpandedInterface:...` API is renamed to `requestTrackingAuthorizationPreferringExpandedInterface:...`. (187610745)

##### Health

###### Known Issues

- Personalized summaries might not generate as expected in the Insights tab. (186964423)
- The redesigned Health app is not included in this beta and was available in the previous beta for testing purposes only. If you update to this beta, your Health app data from the previous beta remains on your device and is viewable in Settings. The redesigned Health app will be available again in an upcoming iOS beta. (188843443)

##### Nearby Interaction

###### Known Issues

- An `NISession` running with a DL-TDoA configuration in a foreground app might be invalidated unexpectedly with a resource timeout error (`NIErrorCodeResourceUsageTimeout`). (189664070)

  **Workaround:** Run a new `NISession` with the same DL-TDoA configuration.

##### Quest Lab Appointments

###### Known Issues

- If you have an upcoming lab appointment, wait to update iOS versions until you receive your results. Contact [Quest](https://support.exp.questdiagnostics.com) directly to reschedule your appointment if you run into any issues. (184530996)

  **Workaround:** Lab results are also available under Browse > Lab Results.

##### Shortcuts

###### Known Issues

- Describe a Shortcut might fail with the error “Something went wrong. Try again later.” (187499433)

##### Simulator

###### Known Issues

- Cloning a simulator device running runtime 27.2 might fail due to incorrect file permissions. (188407822) (FB24939277)

  **Workaround:** `find ~/Library/Developer/CoreSimulator/Devices/<SOURCE_UDID>/data -name '*.sb-????????-??????' -delete`

##### StoreKit Testing in Xcode

###### Resolved Issues

- Fixed: Intro offer eligibility does not reset immediately after calling `SKTestSession.clearTransactions()`. (183933307) (FB24137836)
- Fixed: Changing the storefront or locale using `SKTestSession` doesn’t propagate through `Storefront.updates`. (184155259)
- Fixed: Failed purchases using `SKTestSession` might display error dialogs even when `dialogsDisabled` is set to `true`. (184255116)

###### Known Issues

- Making a purchase in-app for a subscription that is a member of a subscription bundle incorrectly allows the user to unbundle instead of throwing an error. (186018916)

##### UIKit

###### New Features

- On iOS 27.1 and later, the default layout margins for a `UIView` are zero. A view controller continues to provide its view with `systemMinimumLayoutMargins`, which vary depending on the presentation context. To inherit these margins in a subview of the view controller’s view, set its `preservesSuperviewLayoutMargins` property to `true`. (186294594)

## See Also

### iOS & iPadOS 27
- [iOS & iPadOS 27 Release Notes](./ios-ipados-27-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_2-release-notes)*