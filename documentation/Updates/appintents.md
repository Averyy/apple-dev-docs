# App Intents updates

**Framework**: Updates

Learn about important changes in App Intents.

#### Overview

Browse notable changes in [`App Intents`](https://developer.apple.com/documentation/AppIntents).

#### November 2024

##### Siri and Apple Intelligence

- Make onscreen content available to Siri and Apple Intelligence by describing it as an [`AppEntity`](https://developer.apple.com/documentation/AppIntents/AppEntity) and adopting an assistant schema. Additionally, adopt the [`Transferable`](https://developer.apple.com/documentation/CoreTransferable/Transferable) protocol, and associate the app entity with a [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) using the activity’s [`appEntityIdentifier`](https://developer.apple.com/documentation/foundation/nsuseractivity/4485360-appentityidentifier) property.

#### June 2024

##### System Integration

- Integrate your app with Siri and Apple Intelligence using [`App intent domains`](https://developer.apple.com/documentation/AppIntents/app-intent-domains).
- Use [`ControlConfigurationIntent`](https://developer.apple.com/documentation/AppIntents/ControlConfigurationIntent) and [`WidgetKit`](https://developer.apple.com/documentation/WidgetKit) to allow users to put controls on the Lock Screen or in Control Center.
- Create a locked camera capture extension for your app and implement a [`CameraCaptureIntent`](https://developer.apple.com/documentation/AppIntents/CameraCaptureIntent) to allow people to capture photos and videos from controls or the Action button.
- Create app intents that capture audio by implementing [`AudioRecordingIntent`](https://developer.apple.com/documentation/AppIntents/AudioRecordingIntent).
- Allow people to find app entities in Spotlight by adopting the [`IndexedEntity`](https://developer.apple.com/documentation/AppIntents/IndexedEntity) protocol.

##### Content Sharing

- Make it possible to share and transfer data you describe as [`App entities`](https://developer.apple.com/documentation/AppIntents/app-entities) by conforming to [`Transferable`](https://developer.apple.com/documentation/CoreTransferable/Transferable).
- Receive content other apps make available with app intents by using [`IntentFile`](https://developer.apple.com/documentation/AppIntents/IntentFile) for your app intent parameters.
- Describe the file that stores your app intent data using [`FileEntity`](https://developer.apple.com/documentation/AppIntents/FileEntity).

##### General

- Provide additional information about errors with [`AppIntentError.PermissionRequired`](https://developer.apple.com/documentation/AppIntents/AppIntentError/PermissionRequired), [`AppIntentError.Unrecoverable`](https://developer.apple.com/documentation/AppIntents/AppIntentError/Unrecoverable), and [`AppIntentError.UserActionRequired`](https://developer.apple.com/documentation/AppIntents/AppIntentError/UserActionRequired).
- Pass a condition to [`requestConfirmation(conditions:actionName:dialog:)`](https://developer.apple.com/documentation/AppIntents/AppIntent/requestConfirmation(conditions:actionName:dialog:)) to only require user confirmation if a person’s context meets the provided condition.
- Use [`URLRepresentableIntent`](https://developer.apple.com/documentation/AppIntents/URLRepresentableIntent), [`URLRepresentableEntity`](https://developer.apple.com/documentation/AppIntents/URLRepresentableEntity), and [`URLRepresentableEnum`](https://developer.apple.com/documentation/AppIntents/URLRepresentableEnum) to represent your app intents, app entities, and app enums as universal links that you use to provide deep links to your app’s content.
- Define a set of types for an intent parameter using the [`UnionValue()`](https://developer.apple.com/documentation/AppIntents/UnionValue()) macro to create flexible app intents because a parameter can be of one of several pre-defined union types.
- Create entities that have just one singular instance with [`UniqueAppEntity`](https://developer.apple.com/documentation/AppIntents/UniqueAppEntity) and the corresponding [`UniqueAppEntityQuery`](https://developer.apple.com/documentation/AppIntents/UniqueAppEntityQuery). For example, to provide an app intent for app settings that appear in your app or in System Settings, create a singleton entity that encapsulates all settings as properties. Use it in the app intent that offers actions to change your app’s settings.

## See Also

- [Accelerate updates](accelerate.md)
  Learn about important changes to Accelerate.
- [Accessibility updates](accessibility.md)
  Learn about important changes to Accessibility.
- [ActivityKit updates](activitykit.md)
  Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](adattributionkit.md)
  Learn about important changes to AdAttributionKit.
- [AppKit updates](appkit.md)
  Learn about important changes to AppKit.
- [Apple Intelligence updates](apple-intelligence.md)
  Learn about important changes to Apple Intelligence.
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
- [Bundle Resources updates](bundleresources.md)
  Learn about important changes to Bundle Resources.
- [ContactsUI updates](contactsui.md)
  Learn about important changes to ContactsUI.
- [Core Location updates](corelocation.md)
  Learn about important changes to Core Location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/appintents)*