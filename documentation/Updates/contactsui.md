# ContactsUI updates

**Framework**: Updates

Learn about important changes to ContactsUI.

#### Overview

Browse notable changes in [`ContactsUI`](https://developer.apple.comhttps://developer.apple.com/documentation/contactsui).

#### June 2024

##### Limited Access to Contacts

- Check your app’s authorization status for a new value, `CNAuthorizationStatus.limited`. This represents a new status in which a person can grant your app access to a limited subset of their contacts, rather than make an all-or-nothing choice. When your app first calls `CNContactStore.requestAccess(for:completionHandler:)`, an alert asks the person using the app whether to allow contacts access at all. If they allow access, they can choose either full access or choose which contacts to allow, which appears to your app as the `.limited` authorization status. They can revise their choices later in the Settings app.
- Allow someone to quickly add more contacts to this limited-access group by displaying a `ContactAccessButton` in your app’s contact search UI. You initialize this SwiftUI view with a search substring and sets of ignored emails and phone numbers. If a single person matches this query, the button shows the contact and offers to add them to the contacts your app can access. If there are multiple matches, tapping the button shows a separate view to select contacts.
- Use the SwiftUI view modifier `contactAccessPicker(isPresented:completionHandler:)` if you want to conditionally show a full-screen picker that adds contacts to your limited-access app. The `isPresented` parameter binds to a `Bool` value, and shows the picker when the bound value becomes `true`.

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

*[View on Apple Developer](https://developer.apple.com/documentation/updates/contactsui)*