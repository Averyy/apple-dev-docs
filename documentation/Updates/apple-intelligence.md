# Apple Intelligence updates

**Framework**: Updates  
**Role**: Article

Learn about important changes to Apple Intelligence.

## Overview

Browse notable changes in [Apple Intelligence](https://developer.apple.com/apple-intelligence/).

## February 2025

- Use [`ImageCreator`](../ImagePlayground/imagecreator.md) to generate images programmatically from your app on devices that support the capability.  The system’s generative models use your provided description to generate one or more images and return them to your code. The [`ImagePlaygroundConcept`](../ImagePlayground/imageplaygroundconcept.md) type includes text you use to describe the image you wish to create, and [`ImagePlaygroundStyle`](../ImagePlayground/imageplaygroundstyle.md) sets the style to apply to that image.
- Start [Generating summary and priority data for indexed items](../CoreSpotlight/generating-summary-and-priority-data-for-indexed-items.md) using a Spotlight delegate app extension in your app.
- Learn about  [Adopting Smart Reply in your messaging or email app](../UIKit/adopting-smart-reply-in-your-messaging-or-email-app.md) to give Apple Intelligence the context of your messaging or mail thread, and insert the generated response back into your app’s UI. Use [`UIMessageConversationContext`](../UIKit/uimessageconversationcontext.md) for messaging, and [`UIMailConversationContext`](../UIKit/uimailconversationcontext.md) for email.

## January 2025

Writing Tools in UIKit:

- Display a bar button item to launch Writing Tools using [`UIBarButtonItem.SystemItem.writingTools`](../UIKit/uibarbuttonitem/systemitem/writingtools.md).
- Integrate Writing Tools into your custom text engine using the API in [Writing Tools](../UIKit/writing-tools.md).

Writing Tools in AppKit:

- Display a toolbar item to launch Writing Tools using [`writingToolsItemIdentifier`](../AppKit/nstoolbaritem/identifier/writingtoolsitemidentifier.md).
- Integrate Writing Tools into your custom text engine using the API in [Writing Tools](../AppKit/writing-tools.md).

## November 2024

- Make onscreen content available to Siri and Apple Intelligence with App Intents. Describe content as an [`AppEntity`](../AppIntents/appentity.md) and adopt an assistant schema. Conform the entity to the [`Transferable`](../CoreTransferable/transferable.md) protocol, and associate it with a [`NSUserActivity`](../Foundation/nsuseractivity.md) using the activity’s [`appEntityIdentifier`](../Foundation/nsuseractivity/appentityidentifier.md) property.

## July 2024

> **Note**: Testing and using Apple Intelligence features requires iOS 18.1 or later, or macOS 15.1 or later.

### Writing Tools

- In SwiftUI, adjust the level of support for Writing Tools features using the [`writingToolsBehavior(_:)`](../SwiftUI/view/writingtoolsbehavior%28_%29.md) modifier on the [`Text`](../SwiftUI/text.md), [`TextField`](../SwiftUI/textfield.md), and [`TextEditor`](../SwiftUI/texteditor.md) types.
- In UIKit, detect activity using new [`UITextViewDelegate`](../UIKit/uitextviewdelegate.md) methods. Set your text view’s level of support for Writing Tools features using the [`writingToolsBehavior`](../UIKit/uitextinputtraits/writingtoolsbehavior.md) property of [`UITextInputTraits`](../UIKit/uitextinputtraits.md).
- In AppKit, detect activity using new [`NSTextViewDelegate`](../AppKit/nstextviewdelegate.md) methods. Set your text view’s level of support for Writing Tools features using the [`writingToolsBehavior`](../AppKit/nstextinputtraits/writingtoolsbehavior.md) property of [`NSTextInputTraits`](../AppKit/nstextinputtraits.md).

### Genmoji

- Handle Genmoji in text content using [`NSAdaptiveImageGlyph`](../UIKit/nsadaptiveimageglyph.md).

### Siri and App Intents

- Conform your [`AppIntent`](../AppIntents/appintent.md), [`AppEntity`](../AppIntents/appentity.md), and [`AppEnum`](../AppIntents/appenum.md) implementations to the assistant schemas by applying the [relevant macros](../AppIntents/app-schema-domains.md) to your types.

### Core Spotlight

- Search your indexed content for items that are similar in meaning to the query string, but not necessarily a lexical match, using [`CSUserQuery`](../CoreSpotlight/csuserquery.md). Disable this semantic search support using the [`disableSemanticSearch`](../CoreSpotlight/csuserquerycontext/disablesemanticsearch.md) property of [`CSUserQueryContext`](../CoreSpotlight/csuserquerycontext.md).

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
- [App Intents updates](./appintents.md)
  Learn about important changes in App Intents.
- [AppKit updates](./appkit.md)
  Learn about important changes to AppKit.
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

*[View on Apple Developer](https://developer.apple.com/documentation/updates/apple-intelligence)*