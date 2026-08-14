# Apple Intelligence updates

**Framework**: Updates

Learn about important changes to Apple Intelligence.

#### Overview

Browse notable changes in [`Apple Intelligence`](https://developer.apple.comhttps://developer.apple.com/apple-intelligence/).

#### February 2025

- Use [`ImageCreator`](https://developer.apple.com/documentation/imageplayground/imagecreator) to generate images programmatically from your app on devices that support the capability.  The system’s generative models use your provided description to generate one or more images and return them to your code. The [`ImagePlaygroundConcept`](https://developer.apple.com/documentation/imageplayground/imageplaygroundconcept) type includes text you use to describe the image you wish to create, and [`ImagePlaygroundStyle`](https://developer.apple.com/documentation/imageplayground/imageplaygroundstyle) sets the style to apply to that image.
- Start [`Generating summary and priority data for indexed items`](https://developer.apple.com/documentation/corespotlight/generating-summary-and-priority-data-for-indexed-items) using a Spotlight delegate app extension in your app.
- Learn about  [`Adopting Smart Reply in your messaging or email app`](https://developer.apple.com/documentation/uikit/adopting-smart-reply-in-your-messaging-or-email-app) to give Apple Intelligence the context of your messaging or mail thread, and insert the generated response back into your app’s UI. Use [`UIMessageConversationContext`](https://developer.apple.com/documentation/uikit/uimessageconversationcontext) for messaging, and [`UIMailConversationContext`](https://developer.apple.com/documentation/uikit/uimailconversationcontext) for email.

#### January 2025

Writing Tools in UIKit:

- Display a bar button item to launch Writing Tools using [`UIBarButtonItem.SystemItem.writingTools`](https://developer.apple.com/documentation/uikit/uibarbuttonitem/systemitem/writingtools).
- Integrate Writing Tools into your custom text engine using the API in [`Writing Tools`](https://developer.apple.com/documentation/uikit/writing-tools).

Writing Tools in AppKit:

- Display a toolbar item to launch Writing Tools using [`writingToolsItemIdentifier`](https://developer.apple.com/documentation/appkit/nstoolbaritem/identifier/writingtoolsitemidentifier).
- Integrate Writing Tools into your custom text engine using the API in [`Writing Tools`](https://developer.apple.com/documentation/appkit/writing-tools).

#### November 2024

- Make onscreen content available to Siri and Apple Intelligence with App Intents. Describe content as an [`AppEntity`](https://developer.apple.com/documentation/appintents/appentity) and adopt an assistant schema. Conform the entity to the [`Transferable`](https://developer.apple.com/documentation/coretransferable/transferable) protocol, and associate it with a [`NSUserActivity`](https://developer.apple.com/documentation/foundation/nsuseractivity) using the activity’s [`appEntityIdentifier`](https://developer.apple.com/documentation/foundation/nsuseractivity/appentityidentifier) property.

#### July 2024

> **Note**: Testing and using Apple Intelligence features requires iOS 18.1 or later, or macOS 15.1 or later.

##### Writing Tools

- In SwiftUI, adjust the level of support for Writing Tools features using the [`writingToolsBehavior(_:)`](https://developer.apple.com/documentation/swiftui/view/writingtoolsbehavior(_:)) modifier on the [`Text`](https://developer.apple.com/documentation/swiftui/text), [`TextField`](https://developer.apple.com/documentation/swiftui/textfield), and [`TextEditor`](https://developer.apple.com/documentation/swiftui/texteditor) types.
- In UIKit, detect activity using new [`UITextViewDelegate`](https://developer.apple.com/documentation/uikit/uitextviewdelegate) methods. Set your text view’s level of support for Writing Tools features using the [`writingToolsBehavior`](https://developer.apple.com/documentation/uikit/uitextinputtraits/writingtoolsbehavior) property of [`UITextInputTraits`](https://developer.apple.com/documentation/uikit/uitextinputtraits).
- In AppKit, detect activity using new [`NSTextViewDelegate`](https://developer.apple.com/documentation/appkit/nstextviewdelegate) methods. Set your text view’s level of support for Writing Tools features using the [`writingToolsBehavior`](https://developer.apple.com/documentation/appkit/nstextinputtraits/writingtoolsbehavior) property of [`NSTextInputTraits`](https://developer.apple.com/documentation/appkit/nstextinputtraits).

##### Genmoji

- Handle Genmoji in text content using [`NSAdaptiveImageGlyph`](https://developer.apple.com/documentation/uikit/nsadaptiveimageglyph).

##### Siri and App Intents

- Conform your [`AppIntent`](https://developer.apple.com/documentation/appintents/appintent), [`AppEntity`](https://developer.apple.com/documentation/appintents/appentity), and [`AppEnum`](https://developer.apple.com/documentation/appintents/appenum) implementations to the assistant schemas by applying the [`relevant macros`](https://developer.apple.comhttps://developer.apple.com/documentation/appintents/app-intent-domains) to your types.

##### Core Spotlight

- Search your indexed content for items that are similar in meaning to the query string, but not necessarily a lexical match, using [`CSUserQuery`](https://developer.apple.com/documentation/corespotlight/csuserquery). Disable this semantic search support using the [`disableSemanticSearch`](https://developer.apple.com/documentation/corespotlight/csuserquerycontext/disablesemanticsearch) property of [`CSUserQueryContext`](https://developer.apple.com/documentation/corespotlight/csuserquerycontext).

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

*[View on Apple Developer](https://developer.apple.com/documentation/updates/apple-intelligence)*