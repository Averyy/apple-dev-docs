# App Intents updates

**Framework**: Updates

Learn about important changes in App Intents.

#### Overview

Browse notable changes in [`App Intents`](https://developer.apple.com/documentation/appintents).

#### June 2026

##### Apple Intelligence

- Integrate your app with Apple intelligence by conforming your app intents, app entities, and app enums to an app schema in one of the [`App schema domains`](https://developer.apple.com/documentation/appintents/app-schema-domains).
- Indicate that your app entities have identifiers that remain stable across devices by adopting [`SyncableEntity`](https://developer.apple.com/documentation/appintents/syncableentity), so people can continue a task on another device.
- Prompt for confirmation before destructive or sensitive actions on shared or publicly accessible entities by adopting [`OwnershipProvidingEntity`](https://developer.apple.com/documentation/appintents/ownershipprovidingentity) and returning an [`EntityOwnership`](https://developer.apple.com/documentation/appintents/entityownership) value.
- Enable Apple Intelligence to suggest media-related entities like songs or albums during workouts and similar contexts with [`RelevantEntities`](https://developer.apple.com/documentation/appintents/relevantentities).
- Bridge your app entities to system intent value types by using [`IntentValueRepresentation`](https://developer.apple.com/documentation/appintents/intentvaluerepresentation) in your entity’s `transferRepresentation` property.

##### App Intents

- Let people perform App Shortcuts, custom shortcuts, system actions, or open another app from interactive widgets with [`RunSystemShortcutIntent`](https://developer.apple.com/documentation/appintents/runsystemshortcutintent).
- Extend an app intent’s background runtime by adopting [`LongRunningIntent`](https://developer.apple.com/documentation/appintents/longrunningintent) and calling [`performBackgroundTask(options:operation:)`](https://developer.apple.com/documentation/appintents/longrunningintent/performbackgroundtask(options:operation:)) with a [`LongRunningTaskOptions`](https://developer.apple.com/documentation/appintents/longrunningtaskoptions) value, reporting progress as the task runs.
- Handle cancellation cleanup gracefully by adopting [`CancellableIntent`](https://developer.apple.com/documentation/appintents/cancellableintent). Inspect [`IntentCancellationReason`](https://developer.apple.com/documentation/appintents/intentcancellationreason) to distinguish a deliberate cancellation from a timeout.
- Reverse the effect of an app intent’s action by adopting [`UndoableIntent`](https://developer.apple.com/documentation/appintents/undoableintent).
- Specify whether your app intent runs in the foreground, the background, or both by setting the `supportedModes` property to an [`IntentModes`](https://developer.apple.com/documentation/appintents/intentmodes) value, then consult [`currentMode`](https://developer.apple.com/documentation/appintents/intentsystemcontext/currentmode) inside `perform()` to adapt your code at runtime.
- Tell the system which target may perform your app intent or entity query — the main app, the App Intents extension, or a widget extension — by setting the `allowedExecutionTargets` property to an [`IntentExecutionTargets`](https://developer.apple.com/documentation/appintents/intentexecutiontargets) option set.

##### App Entities

- Refer to a large set of entities efficiently using [`EntityCollection`](https://developer.apple.com/documentation/appintents/entitycollection), which stores only entity identifiers and resolves the full [`AppEntity`](https://developer.apple.com/documentation/appintents/appentity) instances on demand. Use the type for an app intent parameter to avoid resolving every identifier during parameter resolution.
- Define union-type Shortcuts parameters with rich picker UI and custom metadata by adopting [`AppUnionValue`](https://developer.apple.com/documentation/appintents/appunionvalue) on the type the `@UnionValue` macro generates, along with the [`AppUnionValueCasesProviding`](https://developer.apple.com/documentation/appintents/appunionvaluecasesproviding) cases enum.
- Have the system retrieve indexed entities by identifier from the Spotlight index by adopting [`IndexedEntityQuery`](https://developer.apple.com/documentation/appintents/indexedentityquery).

##### Errors

- Provide a localized description for failures by initializing an [`AppIntentError`](https://developer.apple.com/documentation/appintents/appintenterror) with `init(description:)`, or wrap an existing error that conforms to [`CustomLocalizedStringResourceConvertible`](https://developer.apple.com/documentation/foundation/customlocalizedstringresourceconvertible).

#### June 2025

- Create app intents that conform to [`SnippetIntent`](https://developer.apple.com/documentation/appintents/snippetintent) to display an interactive snippet.
- Make app entities available in Spotlight that conform to [`IndexedEntity`](https://developer.apple.com/documentation/appintents/indexedentity) and use the `@ComputedProperty(indexingKey:)` or `@Property(indexingKey:)` Swift macros for attributes you want to add to the Spotlight index.
- Integrate your app with visual intelligence by providing app entities to the system using an [`IntentValueQuery`](https://developer.apple.com/documentation/appintents/intentvaluequery).
- Create an [`AppEntity`](https://developer.apple.com/documentation/appintents/appentity) that conforms to the [`Transferable`](https://developer.apple.com/documentation/coretransferable/transferable) protocol and associate the app entity with a [`NSUserActivity`](https://developer.apple.com/documentation/foundation/nsuseractivity) using the activity’s [`appEntityIdentifier`](https://developer.apple.com/documentation/foundation/nsuseractivity/appentityidentifier) property to make onscreen content available to Siri without adopting an assistant schema.

#### November 2024

##### Siri and Apple Intelligence

- Make onscreen content available to Siri and Apple Intelligence by describing it as an [`AppEntity`](https://developer.apple.com/documentation/appintents/appentity) and adopting an assistant schema. Additionally, adopt the [`Transferable`](https://developer.apple.com/documentation/coretransferable/transferable) protocol, and associate the app entity with a [`NSUserActivity`](https://developer.apple.com/documentation/foundation/nsuseractivity) using the activity’s [`appEntityIdentifier`](https://developer.apple.com/documentation/foundation/nsuseractivity/appentityidentifier) property.

#### June 2024

##### System Integration

- Integrate your app with Siri and Apple Intelligence using [`App schema domains`](https://developer.apple.com/documentation/appintents/app-schema-domains).
- Use [`ControlConfigurationIntent`](https://developer.apple.com/documentation/appintents/controlconfigurationintent) and [`WidgetKit`](https://developer.apple.com/documentation/widgetkit) to allow users to put controls on the Lock Screen or in Control Center.
- Create a locked camera capture extension for your app and implement a [`CameraCaptureIntent`](https://developer.apple.com/documentation/appintents/cameracaptureintent) to allow people to capture photos and videos from controls or the Action button.
- Create app intents that capture audio by implementing [`AudioRecordingIntent`](https://developer.apple.com/documentation/appintents/audiorecordingintent).
- Allow people to find app entities in Spotlight by adopting the [`IndexedEntity`](https://developer.apple.com/documentation/appintents/indexedentity) protocol.

##### Content Sharing

- Make it possible to share and transfer data you describe as [`App entities`](https://developer.apple.com/documentation/appintents/app-entities) by conforming to [`Transferable`](https://developer.apple.com/documentation/coretransferable/transferable).
- Receive content other apps make available with app intents by using [`IntentFile`](https://developer.apple.com/documentation/appintents/intentfile) for your app intent parameters.
- Describe the file that stores your app intent data using [`FileEntity`](https://developer.apple.com/documentation/appintents/fileentity).

##### General

- Provide additional information about errors with [`AppIntentError.PermissionRequired`](https://developer.apple.com/documentation/appintents/appintenterror/permissionrequired), [`AppIntentError.Unrecoverable`](https://developer.apple.com/documentation/appintents/appintenterror/unrecoverable), and [`AppIntentError.UserActionRequired`](https://developer.apple.com/documentation/appintents/appintenterror/useractionrequired).
- Pass a condition to [`requestConfirmation(conditions:actionName:dialog:)`](https://developer.apple.com/documentation/appintents/appintent/requestconfirmation(conditions:actionname:dialog:)) to only require user confirmation if a person’s context meets the provided condition.
- Use [`URLRepresentableIntent`](https://developer.apple.com/documentation/appintents/urlrepresentableintent), [`URLRepresentableEntity`](https://developer.apple.com/documentation/appintents/urlrepresentableentity), and [`URLRepresentableEnum`](https://developer.apple.com/documentation/appintents/urlrepresentableenum) to represent your app intents, app entities, and app enums as universal links that you use to provide deep links to your app’s content.
- Define a set of types for an intent parameter using the [`UnionValue()`](https://developer.apple.com/documentation/appintents/unionvalue()) macro to create flexible app intents because a parameter can be of one of several pre-defined union types.
- Create entities that have just one singular instance with [`UniqueAppEntity`](https://developer.apple.com/documentation/appintents/uniqueappentity) and the corresponding [`UniqueAppEntityQuery`](https://developer.apple.com/documentation/appintents/uniqueappentityquery). For example, to provide an app intent for app settings that appear in your app or in System Settings, create a singleton entity that encapsulates all settings as properties. Use it in the app intent that offers actions to change your app’s settings.

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
- [Background Tasks updates](backgroundtasks.md)
  Learn about important changes in Background Tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/appintents)*