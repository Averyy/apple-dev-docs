# Accessibility updates

**Framework**: Updates

Learn about important changes to Accessibility.

#### Overview

Browse notable changes in [`Accessibility`](https://developer.apple.com/documentation/accessibility).

#### June 2025

- Add [`Accessibility`](https://developer.apple.com/documentation/accessibility) to your App Store product page to indicate which accessibility features your app supports.
- Support Assistive Access in iOS and iPadOS scenes with [`AssistiveAccess`](https://developer.apple.com/documentation/swiftui/assistiveaccess).
- Use [`AXBrailleTranslator`](https://developer.apple.com/documentation/accessibility/axbrailletranslator) to translate print text to Braille and Braille to print text according to a given Braille table.
- Use [`openSettings(for:)`](https://developer.apple.com/documentation/accessibility/accessibilitysettings/opensettings(for:)) to open the Settings app to new sections of Accessibility settings, including [`AccessibilitySettings.Feature.assistiveTouch`](https://developer.apple.com/documentation/accessibility/accessibilitysettings/feature/assistivetouch), [`AccessibilitySettings.Feature.assistiveTouchDevices`](https://developer.apple.com/documentation/accessibility/accessibilitysettings/feature/assistivetouchdevices), and  [`AccessibilitySettings.Feature.dwellControl`](https://developer.apple.com/documentation/accessibility/accessibilitysettings/feature/dwellcontrol).

#### June 2024

##### General

- Enhance music with tactile feedback for people who are deaf or hard of hearing by playing Apple-generated haptic tracks along with music tracks. Add the [`MusicHapticsSupported`](https://developer.apple.com/documentation/bundleresources/information-property-list/musichapticssupported) `Info.plist` key to notify the system that your app supports the Music Haptics feature. Specify which song is playing using the [`MPNowPlayingInfoPropertyInternationalStandardRecordingCode`](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfopropertyinternationalstandardrecordingcode). Music Haptics uses the International Standard Recording Code (ISRC) to choose the correct Music Haptics track to play at the same time. Observe and respond to the status of the haptic track playback using [`MAMusicHapticsManager`](https://developer.apple.com/documentation/mediaaccessibility/mamusichapticsmanager).
- Open the Settings app to a specific section of Accessibility settings using [`openSettings(for:)`](https://developer.apple.com/documentation/accessibility/accessibilitysettings/opensettings(for:)).
- Support people’s preference to reduce the blinking animation of the text insertion indicator for custom cursor implementations. Check the value of the preference with [`prefersNonBlinkingTextInsertionIndicator`](https://developer.apple.com/documentation/accessibility/accessibilitysettings/prefersnonblinkingtextinsertionindicator), and observe when people change that preference with [`prefersNonBlinkingTextInsertionIndicatorDidChangeNotification`](https://developer.apple.com/documentation/accessibility/accessibilitysettings/prefersnonblinkingtextinsertionindicatordidchangenotification).
- Check if a device uses Assistive Access with [`isAssistiveAccessEnabled`](https://developer.apple.com/documentation/accessibility/accessibilitysettings/isassistiveaccessenabled) if you need to remove workflows or UI elements that aren’t appropriate in the context of Assistive Access.

##### Swiftui

- Specify that your accessibility element behaves as a tab bar using the [`isTabBar`](https://developer.apple.com/documentation/swiftui/accessibilitytraits/istabbar) accessibility trait with the [`accessibilityAddTraits(_:)`](https://developer.apple.com/documentation/swiftui/view/accessibilityaddtraits(_:)) modifier. In UIKit, use [`tabBar`](https://developer.apple.com/documentation/uikit/uiaccessibilitytraits/tabbar).
- Enhance how you structure accessibility labels by appending custom content using [`accessibilityLabel(content:)`](https://developer.apple.com/documentation/swiftui/view/accessibilitylabel(content:)).
- Generate a localized description of a color in a string interpolation by adding `accessibilityName:`, such as `"\(accessibilityName: myColor)"`. Pass that string to any accessibility modifier.

#### June 2023

- Provide a great experience for your app in Assistive Access, an accessibility feature that tailors the iOS and iPadOS experience for people with cognitive disabilities. Adopt [`UISupportsFullScreenInAssistiveAccess`](https://developer.apple.com/documentation/bundleresources/information-property-list/uisupportsfullscreeninassistiveaccess) to allow your app’s UI to expand into all the available space above the Back button in Assistive Access.
- Personalize your app with Personal Voice, a new feature that lets people record and recreate their voice directly on their iOS and macOS devices. Personal voices appear alongside system voices and are available for Live Speech, a type-to-speak feature that lets a person synthesize speech on the fly. Request access to synthesize speech with personal voices using a new request authorization API in [`AVSpeechSynthesizer`](https://developer.apple.com/documentation/avfaudio/avspeechsynthesizer).
- Detect and mitigate sequences of flashing effects in your video content when the Dim Flashing Lights setting is on. If your app performs custom video drawing instead of using AVFoundation APIs, implement this behavior using [`MAFlashingLightsProcessor`](https://developer.apple.com/documentation/mediaaccessibility/maflashinglightsprocessor).
- Pause animated images in your app when a person turns off the Animated Images setting on their device. Check the value of this setting using [`accessibilityPlayAnimatedImages`](https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilityplayanimatedimages).
- Send announcement, layout change, screen change, and page scroll accessibility notifications with greater ease in multiplatform apps using the new Swift type [`AccessibilityNotification`](https://developer.apple.com/documentation/accessibility/accessibilitynotification). Make sure people receive the most important information first by specifying a default, low, or high priority for announcements.
- Enhance custom accessibility elements by specifying the combination of traits and behaviors that best characterizes the element. Add the new trait [`isToggle`](https://developer.apple.com/documentation/swiftui/accessibilitytraits/istoggle) to controls that toggle on and off, and the new action [`accessibilityZoomAction(_:)`](https://developer.apple.com/documentation/swiftui/view/accessibilityzoomaction(_:)) to content that can zoom in and out.
- Configure new direct touch options through [`accessibilityDirectTouch(_:options:)`](https://developer.apple.com/documentation/swiftui/view/accessibilitydirecttouch(_:options:)) to provide the best experience for elements that support direct touch interactions in your app. Specify the [`silentOnTouch`](https://developer.apple.com/documentation/swiftui/accessibilitydirecttouchoptions/silentontouch) option to ensure VoiceOver is silent when a person interacts with the direct touch area so your app can provide its own audio feedback. Specify the [`requiresActivation`](https://developer.apple.com/documentation/swiftui/accessibilitydirecttouchoptions/requiresactivation) option to make the direct touch area require VoiceOver to activate the element before touch passthrough happens.
- Simplify how you maintain your UIKit accessibility code with block-based setters for accessibility attributes.
- Ensure robust testing of your app’s accessibility experience by performing accessibility audits using [`XCUIApplication`](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication).
- Assign automation elements to expose certain UI elements specifically for the purpose of automation without affecting the accessibility of those elements.

## See Also

- [Accelerate updates](accelerate.md)
  Learn about important changes to Accelerate.
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
- [Background Tasks updates](backgroundtasks.md)
  Learn about important changes in Background Tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/accessibility)*