# App Intents updates

**Framework**: Updates  
**Role**: Article

Learn about important changes in App Intents.

#### Overview

Browse notable changes in [App Intents](../AppIntents/AppIntents.md).

#### June 2026

##### Apple Intelligence

- Integrate your app with Apple intelligence by conforming your app intents, app entities, and app enums to an app schema in one of the [App schema domains](../AppIntents/app-schema-domains.md).
- Indicate that your app entities have identifiers that remain stable across devices by adopting [`SyncableEntity`](../AppIntents/syncableentity.md), so people can continue a task on another device.
- Prompt for confirmation before destructive or sensitive actions on shared or publicly accessible entities by adopting [`OwnershipProvidingEntity`](../AppIntents/ownershipprovidingentity.md) and returning an [`EntityOwnership`](../AppIntents/entityownership.md) value.
- Enable Apple Intelligence to suggest media-related entities like songs or albums during workouts and similar contexts with [`RelevantEntities`](../AppIntents/relevantentities.md).
- Bridge your app entities to system intent value types by using [`IntentValueRepresentation`](../AppIntents/intentvaluerepresentation.md) in your entity’s `transferRepresentation` property.

##### App intents

- Let people perform App Shortcuts, custom shortcuts, system actions, or open another app from interactive widgets with [`RunSystemShortcutIntent`](../AppIntents/runsystemshortcutintent.md).
- Extend an app intent’s background runtime by adopting [`LongRunningIntent`](../AppIntents/longrunningintent.md) and calling [`performBackgroundTask(options:operation:)`](../AppIntents/longrunningintent/performbackgroundtask%28options,operation%29.md) with a [`LongRunningTaskOptions`](../AppIntents/longrunningtaskoptions.md) value, reporting progress as the task runs.
- Handle cancellation cleanup gracefully by adopting [`CancellableIntent`](../AppIntents/cancellableintent.md). Inspect [`IntentCancellationReason`](../AppIntents/intentcancellationreason.md) to distinguish a deliberate cancellation from a timeout.
- Reverse the effect of an app intent’s action by adopting [`UndoableIntent`](../AppIntents/undoableintent.md).
- Specify whether your app intent runs in the foreground, the background, or both by setting the `supportedModes` property to an [`IntentModes`](../AppIntents/intentmodes.md) value, then consult [`currentMode`](../AppIntents/intentsystemcontext/currentmode.md) inside `perform()` to adapt your code at runtime.
- Tell the system which target may perform your app intent or entity query — the main app, the App Intents extension, or a widget extension — by setting the `allowedExecutionTargets` property to an [`IntentExecutionTargets`](../AppIntents/intentexecutiontargets.md) option set.

##### App entities

- Refer to a large set of entities efficiently using [`EntityCollection`](../AppIntents/entitycollection.md), which stores only entity identifiers and resolves the full [`AppEntity`](../AppIntents/appentity.md) instances on demand. Use the type for an app intent parameter to avoid resolving every identifier during parameter resolution.
- Define union-type Shortcuts parameters with rich picker UI and custom metadata by adopting [`AppUnionValue`](../AppIntents/appunionvalue.md) on the type the `@UnionValue` macro generates, along with the [`AppUnionValueCasesProviding`](../AppIntents/appunionvaluecasesproviding.md) cases enum.
- Have the system retrieve indexed entities by identifier from the Spotlight index by adopting [`IndexedEntityQuery`](../AppIntents/indexedentityquery.md).

##### Errors

- Provide a localized description for failures by initializing an [`AppIntentError`](../AppIntents/appintenterror.md) with `init(description:)`, or wrap an existing error that conforms to [`CustomLocalizedStringResourceConvertible`](../Foundation/customlocalizedstringresourceconvertible.md).

#### June 2025

- Create app intents that conform to [`SnippetIntent`](../AppIntents/snippetintent.md) to display an interactive snippet.
- Make app entities available in Spotlight that conform to [`IndexedEntity`](../AppIntents/indexedentity.md) and use the `@ComputedProperty(indexingKey:)` or `@Property(indexingKey:)` Swift macros for attributes you want to add to the Spotlight index.
- Integrate your app with visual intelligence by providing app entities to the system using an [`IntentValueQuery`](../AppIntents/intentvaluequery.md).
- Create an [`AppEntity`](../AppIntents/appentity.md) that conforms to the [`Transferable`](../CoreTransferable/transferable.md) protocol and associate the app entity with a [`NSUserActivity`](../Foundation/nsuseractivity.md) using the activity’s [`appEntityIdentifier`](../Foundation/nsuseractivity/appentityidentifier.md) property to make onscreen content available to Siri without adopting an assistant schema.

#### November 2024

##### Siri and Apple Intelligence

- Make onscreen content available to Siri and Apple Intelligence by describing it as an [`AppEntity`](../AppIntents/appentity.md) and adopting an assistant schema. Additionally, adopt the [`Transferable`](../CoreTransferable/transferable.md) protocol, and associate the app entity with a [`NSUserActivity`](../Foundation/nsuseractivity.md) using the activity’s [`appEntityIdentifier`](../Foundation/nsuseractivity/appentityidentifier.md) property.

#### June 2024

##### System integration

- Integrate your app with Siri and Apple Intelligence using [App schema domains](../AppIntents/app-schema-domains.md).
- Use [`ControlConfigurationIntent`](../AppIntents/controlconfigurationintent.md) and [WidgetKit](../WidgetKit/WidgetKit.md) to allow users to put controls on the Lock Screen or in Control Center.
- Create a locked camera capture extension for your app and implement a [`CameraCaptureIntent`](../AppIntents/cameracaptureintent.md) to allow people to capture photos and videos from controls or the Action button.
- Create app intents that capture audio by implementing [`AudioRecordingIntent`](../AppIntents/audiorecordingintent.md).
- Allow people to find app entities in Spotlight by adopting the [`IndexedEntity`](../AppIntents/indexedentity.md) protocol.

##### Content sharing

- Make it possible to share and transfer data you describe as [App entities](../AppIntents/app-entities.md) by conforming to [`Transferable`](../CoreTransferable/transferable.md).
- Receive content other apps make available with app intents by using [`IntentFile`](../AppIntents/intentfile.md) for your app intent parameters.
- Describe the file that stores your app intent data using [`FileEntity`](../AppIntents/fileentity.md).

##### General

- Provide additional information about errors with [`AppIntentError.PermissionRequired`](../AppIntents/appintenterror/permissionrequired.md), [`AppIntentError.Unrecoverable`](../AppIntents/appintenterror/unrecoverable.md), and [`AppIntentError.UserActionRequired`](../AppIntents/appintenterror/useractionrequired.md).
- Pass a condition to [`requestConfirmation(conditions:actionName:dialog:)`](../AppIntents/appintent/requestconfirmation%28conditions,actionname,dialog%29.md) to only require user confirmation if a person’s context meets the provided condition.
- Use [`URLRepresentableIntent`](../AppIntents/urlrepresentableintent.md), [`URLRepresentableEntity`](../AppIntents/urlrepresentableentity.md), and [`URLRepresentableEnum`](../AppIntents/urlrepresentableenum.md) to represent your app intents, app entities, and app enums as universal links that you use to provide deep links to your app’s content.
- Define a set of types for an intent parameter using the [`UnionValue()`](../AppIntents/unionvalue%28%29.md) macro to create flexible app intents because a parameter can be of one of several pre-defined union types.
- Create entities that have just one singular instance with [`UniqueAppEntity`](../AppIntents/uniqueappentity.md) and the corresponding [`UniqueAppEntityQuery`](../AppIntents/uniqueappentityquery.md). For example, to provide an app intent for app settings that appear in your app or in System Settings, create a singleton entity that encapsulates all settings as properties. Use it in the app intent that offers actions to change your app’s settings.

## See Also

### Technology and frameworks
- [Accelerate updates](./accelerate.md)
  Learn about important changes to Accelerate.
- [Accessibility updates](./accessibility.md)
  Learn about important changes to Accessibility.
- [ActivityKit updates](./activitykit.md)
  Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](./adattributionkit.md)
  Learn about important changes to AdAttributionKit.
- [App Clips updates](./appclips.md)
  Learn about important changes in App Clips.
- [AppKit updates](./appkit.md)
  Learn about important changes to AppKit.
- [Apple Intelligence updates](./apple-intelligence.md)
  Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](./applemapsserverapi.md)
  Learn about important changes to AppleMapsServerAPI.
- [Apple Pencil updates](./applepencil.md)
  Learn about important changes to Apple Pencil.
- [ARKit updates](./arkit.md)
  Learn about important changes to ARKit.
- [Audio Toolbox updates](./audiotoolbox.md)
  Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](./authenticationservices.md)
  Learn about important changes to AuthenticationServices.
- [AVFAudio updates](./avfaudio.md)
  Learn about important changes to AVFAudio.
- [AVFoundation updates](./avfoundation.md)
  Learn about important changes to AVFoundation.
- [AVKit updates](./avkit.md)
  Learn about important changes to AVKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/appintents)*