# iOS & iPadOS 27.2 Beta 3 Release Notes

**Framework**: iOS & iPadOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The iOS & iPadOS 27.2 SDK provides support to develop apps for iPhone and iPad running iOS & iPadOS 27.2 beta 3. The SDK comes bundled with Xcode 27.2. For information on the compatibility requirements for Xcode 27.2, see [`Xcode 27.2 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-27_2-release-notes).

##### App Tracking Transparency

###### New Features

- `AppTrackingTransparency` ([`ATT`](https://developer.apple.comhttps://developer.apple.com/documentation/apptrackingtransparency)) now supports an alternative expanded prompt and re-prompting on a yearly basis for EU users. The alternative prompt is required for users in France, Germany, Italy, Poland, and Romania. (179504171)

###### Resolved Issues

- Fixed: The new `requestTrackingAuthorization(usingExpandedInterface:additionalInformationAction:completionHandler:)` API is renamed to `requestTrackingAuthorization(preferExpandedInterface:...)`. (187149729)
- Fixed: The new `requestTrackingAuthorization(preferExpandedInterface:...)` API is renamed to `requestTrackingAuthorizationPreferringExpandedInterface:…)`. (187610745)

##### Health

###### Known Issues

- Personalized summaries may not generate as expected in the Insights tab. (186964423)

##### Quest Lab Appointments

###### Known Issues

- If you have an upcoming lab appointment, wait to update iOS versions until you receive your results. Contact [`Quest`](https://developer.apple.comhttp://support.exp.questdiagnostics.com) directly to reschedule your appointment if you run into any issues. (184530996) **Workaround:** Lab results are also available under Browse > Lab Results.

##### Shortcuts

###### Known Issues

- Describe a Shortcut might fail with the error “Something went wrong. Try again later.” (187499433)

##### Simulator Runtimes

###### Known Issues

- Cloning a simulator device running runtime 27.2 might fail due to incorrect file permissions. (188407822) (FB24939277) **Workaround:** `find ~/Library/Developer/CoreSimulator/Devices/<SOURCE_UDID>/data -name '*.sb-????????-??????' -delete`

##### Storekit Testing in Xcode

###### Resolved Issues

- Fixed: Intro offer eligibility does not reset immediately after calling `SKTestSession.clearTransactions()`. (183933307) (FB24137836)
- Fixed: Changing the storefront or locale using `SKTestSession` doesn’t propagate through `Storefront.updates`. (184155259)
- Fixed: Failed purchases using `SKTestSession` might display error dialogs even when `dialogsDisabled` is set to true. (184255116)

###### Known Issues

- Making a purchase in-app for a subscription that is a member of a subscription bundle incorrectly allows the user to unbundle instead of throwing an error. (186018916)

##### Uikit

###### New Features

- On iOS 27.1 and later, the default layout margins for a `UIView` are zero. A view controller continues to provide its view with `systemMinimumLayoutMargins`, which vary depending on the presentation context. To inherit these margins in a subview of the view controller’s view, set its `preservesSuperviewLayoutMargins` property to `true`. (186294594)

## See Also

- [iOS & iPadOS 27 Release Notes](ios-ipados-27-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_2-release-notes)*