# iOS & iPadOS 27 Beta Release Notes

**Framework**: iOS & iPadOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The iOS & iPadOS 27 SDK provides support to develop apps for iPhone and iPad running iOS & iPadOS 27 beta. The SDK comes bundled with Xcode 27, available from the Mac App Store. For information on the compatibility requirements for Xcode 27, see [`Xcode 27 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-27-release-notes).

##### Airplay

###### Known Issues

- AirPlay to Home Theaters fails when a PIN or password is required.  (176462871) **Workaround:** Disable the Home Theater configuration.

##### Airpods Max 2

###### Known Issues

- You cannot update AirPods Max 2 firmware beta in iOS 27 Beta 1 and macOS 27 Beta 1. AirPods Max 2 firmware beta updates are supported in iOS 27 Beta 2 and macOS 27 Beta 2.  (178280323)

##### App Intents

###### Known Issues

- Non-SF Symbol custom images for app entities might not always appear in Siri.  (175031314)
- Default values from schemas might not be applied for parameters that are of “Set” type.  (175534195) **Workaround:** Provide a default value explicitly using `@Parameter`, such as an empty set.
- Entities you register using `RelevantEntities` for the workout audio context might not appear as suggestions in Fitness media picker.  (177996973)

##### Apple Intelligence Report

###### Known Issues

- When you view Apple Intelligence Report entries for Home Intelligence, some data that was sent to Private Cloud Compute won’t appear in the report.  (176056930)

##### Audioaccessorykit

###### New Features

- AudioAccessoryKit now allows third-party audio accessory manufacturers to provide headphone information to the system to support fixed spatial audio. It is only available for developer testing on iPhone and iPad in this release, and will be available to customers in the EU in a future iOS 27 and iPadOS 27 release.  (178275661)

##### Background Assets

###### New Features

- You can reduce your app’s storage usage with localized asset packs. The system delivers the appropriately localized asset packs based on the user’s preferred languages.  (163944365)

##### Battery Power Management

###### Resolved Issues

- Fixed: Devices with a deeply discharged battery might fail to boot into the OS and remain stuck on the red dead battery icon screen indefinitely until the device is rebooted or the power adapter is unplugged and reconnected.  (177346712)

##### Camera

###### Known Issues

- In the Camera app, Portrait mode blur effect might render incorrectly for photos.  (177335723)

##### Carplay

###### Known Issues

- `CPNavigationSession` ETA Tray panel items might not receive focus.  (177508893)
- The panel delegate method `panelDidHide(_ panel: CPMapPanel)` might not be called.  (177590525)
- Under certain configurations, `CPMapPanel` might not dismiss when you tap the close button.  (177592347)
- The symbol button handler of `CPMapPanelButtonConfiguration` might not be called.  (177595560)
- Your vehicle’s next and previous track steering wheel buttons might not function correctly in CarPlay.   (177832695) **Workaround:** Use the on-screen playback controls in CarPlay to advance or go back to the previous track.
- Siri might respond more slowly than expected in CarPlay, particularly under higher device temperatures or poor network conditions.   (178952858) **Workaround:** Try the request again after the device has cooled down or once you are in an area with better cellular reception.

##### Clock

###### Known Issues

- You might be unable to stop a ringing alarm from the lock screen without unlocking your device.   (177728602) **Workaround:** Unlock your device, or say “stop the alarm,” or say “stop music.”

##### Control Center

###### Known Issues

- The “Add a Control” button in edit mode might appear small and clipped.  (170774279)

##### Core Ai

###### Known Issues

- `AIModelCache` entries might not honor the cache policy you provide, causing re-specialization to occur more often than expected.  (169746264)
- When inference runs on the GPU, `InferenceFunction.encode` blocks until all compute is complete instead of returning as soon as encoding is done, unless the model is specialized with a preferred compute device of GPU.  (175789258)
- Certain weight and activation configurations may not run on the Neural Engine, such as FP8-quantized weights and activations, palettized weights with quantized (non-Float16) values, and sparse weights. Affected models may run on the CPU or GPU instead.  (176210080)
- When you run `InferenceFunction.run` on functions with both state arguments and outputs with dynamic shapes, the framework might be unable to infer the shape of the outputs and throw an error.  (176807213) **Workaround:** If you know what the output shape will be, pre-allocate the output and provide it through the `outputViews` arguments on `InferenceFunction.run`.
- Inference might fail or crash for models with control flow over dynamic-shape tensors (for example, linear-attention LLMs such as Qwen3.5/3.6).  (177354777)
- Ahead-of-time (AOT) compilation might fail unexpectedly for certain models.  (177729331)
- When Metal API Validation is enabled, CoreAI models might fail to execute.  (177991751) **Workaround:** In Xcode, disable Metal API Validation. From the command line, ensure the `MTL_DEBUG_LAYER` environment variable is not set.
- Models with custom Metal kernels will fail to load.  (178056451)

##### Core Bluetooth

###### Known Issues

- The Channel Sounding API in Core Bluetooth is not returning ranging results.  (178333845)

##### Developer Settings

###### Known Issues

- Deep links into Settings > Developer > Paired Macs might silently fail to navigate to the target Mac computer. The Paired Macs pane loads correctly when entered manually.   (178063365) **Workaround:** Navigate to Settings > Developer > Paired Macs manually, then select the desired Mac computer from the list.

##### Dictation

###### New Features

- Dictation can now be powered by a new on-device model that will boost accuracy. To enable this, go to Keyboard settings > Dictation and Toggle on “Advanced Dictation Preview”  (178444388)

###### Known Issues

- Voice Editing commands such as “Change X to Y”, “Delete X”, and “Undo/Redo” might not work reliably.  (173448573)
- The “New Line” and “All Caps” formatting commands might not work reliably in the dictation UI.  (177959708)
- When you explicitly dictate punctuation— such as “Period” or “Colon” — both the spoken command word and the punctuation character might be inserted instead of the punctuation character alone.  (178078177)
- Dictation might not recognize names from your contacts.  (178079519)
- Dictation might insert extra words at the end of a dictated passage that you did not speak.  (178269104)

##### Finder

###### Known Issues

- Suggested names for a file or folder might be more generic than its contents. For example, a folder containing only bird photos might receive suggestions like “Wildlife” or “Animal Photos” rather than bird-specific names.  (178093786)

##### Findmy

###### Known Issues

- Siri might not be able to find some of the people sharing location with you in FindMy.  (178384345)

##### First Party App Search

###### Known Issues

- Search assets might download slowly for languages and regions other than English and the United States, causing degraded search experiences for first-party apps up to a few hours after you install or upgrade to the latest OS, change your device language, or region.  (178186226)

##### Fitness+

###### Known Issues

- On larger iPhones in landscape orientation, the Workout Detail view may display duplicate title text and action buttons when browsing workouts or meditations.  (177964121)

##### Foundation

###### Resolved Issues

- Fixed: `+[NSURL URLWithString:]` no longer double-encodes the `%` of valid percent-escape sequences when encoding other invalid characters.  (161588649) (FB20439045)

##### Foundation Models

###### Known Issues

- Private Cloud Compute might not work when you use simulators.   (177684296) **Workaround:** Use a physical device running OS 27.0.
- When using the on-device Apple Foundation Model for both tool calling and guided generation, some prompts might cause the model to call tools excessively.  (177748926) **Workaround:** Adjust your instructions, prompts, and attachment labels.
- `@Generable` on an `enum` produces a deprecation warning about `GenerationError` that cannot be silenced.  (177899620)
- Truncating transcript history in the `onPrompt` modifier might cause an unexpected runtime error.  (177901494)
- `onPrompt` might not be called when applied to a `Profile` without instructions.   (177902488) **Workaround:** Always specify instructions in a `Profile`.
- `PrivateCloudComputeLanguageModel` always uses greedy decoding.  (178181782)
- Passing an `any LanguageModel` to the `model(_:)` modifier will lead to a compiler error.  (178545978) **Workaround:** Import the [`Foundation Models framework utilities`](https://developer.apple.comhttps://github.com/apple/foundation-models-utilities) package, which contains a built-in workaround that will compile your code.

##### Game Center

###### Resolved Issues

- Fixed: When you trigger the Access Point, it’s completion handler is never invoked.  (172683368)

##### Game Controller

###### New Features

- The PlayStation® Access™ controller is now supported on macOS, iPadOS, and iOS. You can create custom input profiles in game controller settings and save them to your Apple device.  (168071382)

##### Healthkit

###### New Features

- HealthKit adds support for tracking menopausal state and bleeding after menopause; two new sample types are available. HKCategoryTypeIdentifierMenopausalState records a person’s current menopausal state. Values defined by HKCategoryValueMenopausalState are menopause, perimenopause, and none. HKCategoryTypeIdentifierBleedingAfterMenopause records bleeding episodes occurring after menopause. Values use the existing vaginal bleeding flow levels: unspecified, light, medium, and heavy. Both types are read/write, classified under Reproductive Health, and require the standard HealthKit category type authorization.  (178532053)

##### Hearing Test

###### Known Issues

- During a Hearing Test, visual feedback might not appear when you tap the screen to indicate a tone was heard.  (176360906) **Workaround:** End the Hearing Test and start a new one. Note that ending a test in progress will not produce a result, which is the expected behavior. For general guidance on difficulties operating a Hearing Test, refer to the troubleshooting guide in the Instructions for Use.

##### Home Screen

###### Known Issues

- Switching between many different posters with different icon tints may cause system sluggishness.  (178435221) **Workaround:** Reboot the device.
- The Home Screen Customization on a newly setup device might not save.   (178576719) **Workaround:** Reboot the device and try again

##### Homekit

###### New Features

- When Apple Intelligence in the Home app is enabled, your HomeKit Secure Video recordings are processed on-device and through Private Cloud Compute for video descriptions and search.  (178858470)

##### Image Playground

###### Known Issues

- When VoiceOver is enabled and the gallery contains only one image, the prompt input UI might not appear.   (175357842) **Workaround:** Duplicate the image so the gallery contains two or more images.
- When Image Wand encounters an error — such as an unsupported flow or unsafe output — you might see the misleading message “Connect to Wi-Fi to create images” even when your device is already connected to Wi-Fi.  (177710762)
- If required models are downloading, you might see an error message instead of download progress information.  (177833994) **Workaround:** This issue occurs only on first install. Wait for the models to finish downloading, then try again.
- In the Image Playground photo picker, the All and Suggested tabs are missing, which might limit the number of photos available for you to choose from.  (178256174)

##### Ldcm

###### Known Issues

- When your device’s charging port is wet but empty, you might see a dialog instructing you to unplug a charger or accessory even though nothing is connected.  (175484509)

##### Lock Screen

###### Known Issues

- After dismissing Lock Screen, the Lock Screen grabber might appear in the incorrect location or orientation.  (178174745)
- Starting a Vision Pro Guest Mode session might result in two Live Activities on screen at the same time.  (178200601) **Workaround:** Dismiss the Lock Screen and re-lock the device.

##### Mail Banners

###### Known Issues

- Mail banners for early flights will show the flight status as delayed.  (173869986) **Workaround:** Confirm flight status through the track flight action, flight change email communication, or the flight provider website.

##### Media Sharing Extensions

###### New Features

- New frameworks allow you to add media sharing protocols through extension at the system level and enable media apps to use these extensions through a common API framework.  (168722808)

###### Known Issues

- Due to a mismatch in runtime checks with the mandatory entitlement for `MediaSharingExtensions`, extensions using the new `MediaDeviceExtension` framework can build but don’t run on target devices.  (178179521)

##### Messages

###### Resolved Issues

- Fixed: Stickers attached to a message from an unknown sender do not appear.  (177453147)

###### Known Issues

- GIFs and pasted images might render as the incorrect size.   (177657977) **Workaround:** Scroll until that message is offscreen, leave the conversation, or force-quit Messages.

##### Metal

###### New Features

- Metal 4.1 is now supported. See [`Metal`](https://developer.apple.comhttps://developer.apple.com/metal/) for additional details.  (176468465)

###### Known Issues

- When you use a sampler to read from a texture with clamp-to-edge addressing mode, the result might be clamped to zero.  (172520325)
- On devices in the Apple 10 GPU family, using a sampler to read from a texture with clamp-to-edge addressing mode might produce results that are clamped to zero.  (177318505)

##### Metrickit

###### New Features

- `CrashDiagnostic` now includes a `terminationCategory` that maps to the corresponding case in `ForegroundTerminationMetric` and `BackgroundTerminationMetric`.  (96078210) (FB10494149)
- Apps that emit developer-defined states through the `StateReporting` framework now receive metrics and diagnostics in the context of those states.  (159889985)
- `MemoryExceptionDiagnostic` are available when your app or app extension is terminated for exceeding its memory limit.  (159890067)
- A new application-level `MetalFrameRateMetric` is available for Metal frame pacing rendering insights per `CAMetalLayer`.  (159890165)
- A new Swift-first `MetricManager` API enables your app to receive `MetricReport` and `DiagnosticReport` objects through `AsyncStream`. `MetricReport` contains a daily aggregated entry along with interval-based breakdowns that are typically a few hours each.  (164439529)

###### Deprecations

- The original MetricKit APIs — including `MXMetricManager`, `MXMetricManagerSubscriber`, `MXMetricPayload`, and `MXDiagnosticPayload` — are no longer recommended for new adoption. Use `MetricManager` instead.  (174892111)

##### Nearby Interaction

###### Known Issues

- The Channel Sounding API in Nearby Interaction does not return ranging results.  (178073051)

##### Network Security

###### New Features

- Starting in 27.0 operating systems, select system processes now enforce stricter network security (TLS) requirements. These new requirements might cause connections to fail if the server does not meet them. The affected processes are those involved in MDM, DDM, Automated Device Enrollment, configuration profile installation, app installation, and software updates. Servers must support TLS 1.2 at minimum, using cipher suites and certificates that meet App Transport Security (ATS) requirements. For additional details on affected processes, requirements, and how to audit and diagnose failures in managed environments please reference [`Prepare your network environment for stricter security requirements`](https://developer.apple.comhttps://support.apple.com/en-us/126655). For additional details on ATS and the new requirements please reference [`Preventing Insecure Network Connections`](https://developer.apple.comhttps://developer.apple.com/documentation/Security/preventing-insecure-network-connections) and [`NSRequiresNIAPTLSPackageVersion`](https://developer.apple.comhttps://developer.apple.com/documentation/BundleResources/Information-Property-List/NSRequiresNIAPTLSPackageVersion).  (176055825)

##### Networkextension

###### Resolved Issues

- Fixed: When an active VPN configuration sets `includeAllNetworks` to true, `excludeLocalNetworks` fails to exclude wired connections to CarPlay.  (176839377)

##### On Demand Resources

###### Deprecations

- On Demand Resources and the `NSBundleResourceRequest` API are deprecated. Use Background Assets instead.  (170066290)

##### Photos

###### Known Issues

- When opened from a grid of Photos search results in Siri on iPadOS, the single-photo viewer might appear blank.   (169236746) **Workaround:** Close and reopen the viewer.
- You might see a slight shift in color hues after applying Spatial Reframing to photos.  (176384327)
- When sharing a Live Photo from the Photos app, you might not be able to disable the Live Photo effect prior to sending.  (178093956) **Workaround:** Disable Live Photo effect from the Photos app before sharing.
- Photos app might quit unexpectedly when you re-enter the Extend tool on a photo that has already been extended.  (178164434) **Workaround:** From the Photos app or the editor, use “Revert to Original” to remove the existing Extend adjustment before re-entering the Extend tool.

##### Photos Edit

###### Known Issues

- A thin white line might be visible in photos that have had Spatial Reframing applied.  (178183850)

##### Podcasts

###### Known Issues

- On first launch after updating, you might experience longer-than-expected library migration times, which might last several minutes.   (175524004) **Workaround:** Remain in the Podcasts app until the “Updating Library…” screen disappears and your Podcasts content appears, even if this takes several minutes.

##### Realitykit

###### New Features

- The Gaussian Splat Component API in RealityKit will be available in an upcoming release.  (178061856)

###### Resolved Issues

- Fixed: When `OpacityComponent` is applied to an entity with opaque materials, `RealityRenderer` renders the opaque materials with transparency, revealing interior surfaces. Only the frontmost surface should appear with partial transparency.  (177976245)

###### Known Issues

- Some MaterialX 1.39 nodes are not supported.  (172875414)
- `ComputeGraphComponents` stored in a Reality file do not render when loaded.  (177674901)

##### Related Receipts

###### Known Issues

- The disclaimer “Siri found in Mail or Photos. Not shared with card issuer” does not appear below displayed transaction related receipts in Wallet for Apple Pay, Apple Card, and Apple Cash.  (178202101)

##### Safari

###### Known Issues

- The Safari tab bar might enter a state where it does not appear on screen.  (177812052) **Workaround:** Quit and relaunch Safari.
- Safari Intelligence features might appear as available before assets are fully downloaded. If you use the feature before assets are available, it won’t function correctly.  (178099724) **Workaround:** Wait for assets to finish downloading. You can check download progress in Settings > Apple Intelligence & Siri.
- On iPad, the tip prompting users to automatically organize their tabs might not appear in Safari.  (178280800) **Workaround:** In the tab overview, tap the “…” button and choose Organize Tabs > Automatically Create Topics.

##### Sensorkit

###### Known Issues

- PPG sensor reader might return no samples when attempting to fetch data.  (178275291)

##### Shadergraph

###### Known Issues

- The `realitykit_hair_surfaceshader` node does not support `DiffuseLightProbeGroupComponent`. Materials built with this node might not respond to diffuse light probe group lighting.  (177976666)

##### Shortcuts

###### Known Issues

- If an app intent uses Duration or `LPLinkMetadata`, creating a shortcut with that intent and then attempting to edit it with “Describe a change” might fail.   (166068090) **Workaround:** If the model discards the action, press “Undo” to recover the unsupported intent.
- When an app intent defines a `UnionValue` parameter with two number-related types (for example, both Int and Double), the number option appears twice in the parameter picker menu and shows as double-selected.   (168315587) **Workaround:** Define only one number-related type in the `UnionValue` parameter (for example, use only Int or only Double, not both).

##### Siri

###### Known Issues

- After Siri returns photo search results and you select photos, Siri might not detect which photos are selected on screen. Commands like “Send these” might apply to all photos returned from the search rather than only the selected ones.  (171728298) **Workaround:** Open Photos, select the photos you want to act on, then perform the action using Siri — for example, “Send these photos to Bob”.
- Siri ignores custom values for navigation preferences, transport, and incident types in apps that use `maps.startNavigation` or `maps.reportIncident` intent schemas.  (175230813)
- When location data is unavailable or only coarse-accuracy location data is available, Maps searches initiated through Siri might return empty or imprecise results.  (175380461) **Workaround:** Grant Siri access to your location in Settings.
- When you turn off Siri, some photo-related questions might return web search results instead of prompting you to share the photo with ChatGPT.  (175884006)
- When you ask Siri to work with reminder lists, you might need to use the exact list name. Siri might not recognize similar or partial list names.  (176400964) **Workaround:** Use the exact name of your reminder list when speaking or typing to Siri.
- Siri doesn’t support voice commands to interact with specific photos. For example, you can’t refer to photos by number, such as “photo one” or “photo four.”  (176812955) **Workaround:** Use the photo picker to select the photo you want, or tap to select photos directly.
- App Intents with `@UnionValue` types that accept a `PlaceDescriptorEntity` and a `String` always receive `String` values instead of `PlaceDescriptorEntity` entities.  (176844035) **Workaround:** Include a `String` case in your `@UnionValue` enum and manually convert the `String` to a `PlaceDescriptorEntity` when needed.
- When you ask Siri for Maps information, the response snippets might appear incomplete or display formatting issues.  (177116121) **Workaround:** Ask Siri to repeat the information, or open Maps directly for complete details.
- Starting a call with Siri might fail with an error in apps that adopt CallKit and the `phone.startCall` AppSchema.  (177190637)
- When you ask Siri to send a message to a contact that doesn’t exist on your device, Siri might draft a message to an unrelated contact.  (177356158)
- When you ask Siri to add photos to an album, the confirmation prompt and spoken response might report or display more photos than will actually be added.  (177376984) **Workaround:** Add photos to the album manually in the Photos app: tap Select, tap the photos you want to add, tap the Share button, tap Add to Album, then tap the album.
- You might not see names and images of email senders in the Siri email list UI.  (177416168)
- Siri might not resolve some entity types when your app has provided only an `EntityStringQuery` for the entity type.  (177464215) **Workaround:** Index the entity in Spotlight, or provide an `IntentValueQuery` if applicable.
- Siri functionality during software updates is limited, including calls to emergency services.  (177476889)
- Asking Siri to call short phone numbers, such as “Call 17”, might fail.  (177545828) **Workaround:** When calling for emergency services, ask Siri to explicitly “call emergency services.”
- Search results from third-party apps may not be tappable.  (177593534)
- Disabling Siri might not delete your Siri and Dictation interaction history from your device.  (177649865)
- Siri might not find app-specific contacts that are only indexed in Spotlight and do not appear in the Contacts app.  (177679168) **Workaround:** Add the contact to the Contacts app.
- Siri cannot create a recurring reminder or update an existing reminder to be reoccurring.  (177722240)
- With AirPods connected to iPhone and Announce Notifications enabled, responding “yes” by voice or head gesture to a long incoming notification (for example, a message) prompts you to unlock iPhone instead of reading the full message aloud.  (177733317)
- New American English Siri voices 6 and 7 might default to legacy US voices when your device is overheated or in Low Power Mode.   (177742977) **Workaround:** Turn off Low Power Mode or wait for your device to cool down.
- When you use ChatGPT with Apple Intelligence, some responses used in follow-up queries or when you resume a chat might be logged by Apple.  (177755742)
- When you ask Siri to find, search, or read reminders, Siri might list or read the reminders instead of showing a snippet. When reminder lists are displayed, the list color might not appear correctly.  (177762533)
- After enabling Expressive Voices, you are not able to modify Pace or Expressiveness in the Settings pane.  (177969955)
- Non-SF Symbol custom images for entities might not appear in Siri results for third-party apps.  (177984074)
- Siri might run the incorrect `OpenIntent` or `system.open` intent when multiple intents targeting different entity types are available in your app.  (177992979)
- After creating a list through Siri, tapping the list icon might result in an error instead of opening the list in the Reminders app.  (177998395)
- When you tap the Send button in the Siri message confirmation flow, the message might fail to send.  (178025056) **Workaround:** Use your voice to confirm sending the message instead of tapping the Send button.
- When you ask Siri to read your last message, Siri might read an unread message from an unknown sender, such as spam, instead of the most recent message from a known contact.  (178049066) **Workaround:** Name the sender in your request – for example, “Read my last message from .”
- When you ask Siri to open a URL from the Siri App, Safari might launch to a blank screen.  (178163636) **Workaround:** After Safari launches, return to the Siri app to confirm the request.
- On CarPlay with Apple Intelligence and the ChatGPT extension enabled, asking ChatGPT a question through Siri might not produce a spoken answer. The Siri orb appears briefly and the microphone reopens without Siri responding.   (178247289) **Workaround:** When you are done driving, ask the same ChatGPT question using Siri on iPhone directly instead of through CarPlay.
- Siri might respond more slowly than expected in CarPlay, particularly under higher device temperatures or poor network conditions.   (178274714) **Workaround:** Try the request again after the device has cooled down or once you are in an area with better cellular reception.
- You might encounter build failures when attempting to implement a Transferable `IntentValueRepresentation` for `PHAsset`.   (178276448) **Workaround:** Explicitly add `import _Photos_AppIntents` to your source file.
- When asking Siri to call, message, or email a contact, Siri might fail to resolve the correct person — particularly when multiple contacts share the same name, when group names contain emoji or special characters, or when relationship labels (e.g., “my brother”) are ambiguous. In some cases, Siri might pick the wrong contact, fail to present a disambiguation prompt, or freeze during the disambiguation UI.  (178379209) **Workaround:** If Siri selects the wrong contact, try using the person’s full name (first and last) or specifying the contact handle directly.
- For Report a Concern flows started with Siri, the text in attachments might be difficult to read while in Dark Mode.  (178381615) **Workaround:** Switch your device to Light Mode to review the content in those files.
- Businesses with overnight hours might display as “Closed till [next day]” even during open hours.  (178384054)
- In CarPlay, when Apple Intelligence enabled, Siri requests for directions in Maps might fail to start navigation.  (178459481) **Workaround:** Tap the Go button to start navigation.
- Siri might not respond to your voice correctly.  (178489724) **Workaround:** Force quit the Siri app and relaunch it.
- In the Siri app, conversations might be deleted a few minutes after receiving streaming responses.  (178560562)

##### Siri Spotlight and Mail App Search

###### Known Issues

- Mail older than 6 months might not be searchable by body content, but is still searchable by sender and subject.  (177942110)

##### Standby

###### Known Issues

- StandBy Clocks may be missing.  (178061326)

##### Storekit

###### New Features

- Offer code redemption APIs now return a `VerificationResult` when redemption completes. If a redemption succeeds, your app receives a `VerificationResult` that contains a `Transaction` object. If a redemption fails, your app receives an error that describes what caused the redemption to fail.  (141012819)
- StoreKit now includes the `Transaction.OwnershipType.assigned` and `Transaction.RevocationType.assignmentRevoked` enum values to support volume purchases. `Transaction` query methods now additionally return transactions assigned to the Managed Apple Account.  (156749517)
- New `Product.ProductType` APIs represent subscription Bundles and subscription Suites. New APIs in `Product.SubscriptionInfo.BundledSubscription` let you fetch merchandising data about subscriptions contained in a Bundle. Transaction and RenewalInfo contain new fields that provide information about purchases and customer status regarding Bundles and Suites.  (160501742)
- `partnerName` and `partnerId` properties for Advanced Commerce API are available in [`Transaction.AdvancedCommerceInfo`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction/advancedcommerceinfo-swift.struct) and [`RenewalInfo.AdvancedCommerceInfo`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/advancedcommerceinfo-swift.struct).  (167808780)

##### Storekit Testing in Xcode

###### Resolved Issues

- Fixed: The unified app receipt is not updated after forcing a subscription expiration with `SKTestSession`.  (102093015) (FB11767567)
- Fixed: The `SKTestSession` `disableDialogs` setting is not always respected for all system dialogs.  (154390284) (FB18403150)
- Fixed: Subscription upgrades performed with the Xcode Transaction Manager are not reported in `Transaction.updates`.  (160698598) (FB20269723)
- Fixed: The renewal behavior preference is not respected when using the `purchaseDate(_:renewalBehavior:)` purchase option to make purchases using `SKTestSession`.  (162014134) (FB20537538)

###### Known Issues

- When using StoreKit Testing in Xcode, `pricingTerms.commitmentInfo.price` returns an incorrect price for monthly subscriptions billed as a 12-month commitment.  (177942756)

##### Suggestions in Messages

###### Known Issues

- The app icon shown for navigation suggestions is always the Apple Maps icon. If the suggestion is selected, the user’s preferred navigation app is correctly launched.   (178193147)

##### Swift Charts

###### Known Issues

- When your project has a minimum deployment target lower than 27.0, using conditionals inside a `Chart` closure produces the warning “Conformance of ‘_ConditionalContent<TrueContent, FalseContent>’ to ‘ChartContent’ is only available in  27.0 or newer,” and the app might crash at runtime when that content is loaded.  (174168981) **Workaround:** Extract the conditional chart content into a separate function or computed property annotated with `@ChartContentBuilder`. For example, replace: ```None
 Chart(dataPoints, id: \.index) { dataPoint in
   if selectedMetric == "Rate" {
       LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.rate))
           .foregroundStyle(.blue)
   } else {
       LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.signal))
           .foregroundStyle(.green)
   }
 }
``` with: ```None
 Chart(dataPoints, id: \.index) { dataPoint in
   marks(for: dataPoint)
 }
 
 @ChartContentBuilder 
 private func marks(for dataPoint: DataPoint) -> some ChartContent {
   if selectedMetric == "Rate" {
       LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.rate))
           .foregroundStyle(.blue)
   } else {
       LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.signal))
           .foregroundStyle(.green)
   }
 }
```

##### Swiftdata

###### Known Issues

- You might experience a deadlock for `@Query` when saving a `ModelContext` on a background actor while scheduling new async tasks for a `ModelActor`.  (178113288)

##### Swiftui

###### New Features

- You can now use `.toolbarColorScheme(colorScheme, for: .statusBar)` to set a preferred status bar color scheme.  (55162154) (FB7234376)
- `AsyncImage` now automatically caches downloaded images using HTTP caching protocols, allowing servers to control caching behavior via standard headers. You can customize caching for specific images using the new`AsyncImage` initializers that accept `URLRequest` with custom `cachePolicy` settings. Additionally, you can set a custom `URLSession` using the new `View.asyncImageURLSession(_:)` API to control how all child `AsyncImage` views perform data tasks.  (78212597)
- In apps built with the iOS 27.0 and iPadOS 27.0 SDKs, a `Text` view with `.textSelection(.enabled)` applied now supports user-interactive selection using the system text selection UI. Previously, selectable `Text` views on iOS and iPadOS offered selection functionality through a callout menu. When building with the iOS 27.0 and iPadOS 27.0 SDKs, selectable `Text` views might include additional gestures for system text selection interactions. Consider using `.highPriorityGesture()` for custom gestures applied to `Text` views that should supersede system text selection gestures.  (79770704) (FB9208920)
- A `@State` declared with an expression as its initial value used to evaluate the expression each time the view struct re-instantiates. In the case of `@State private var model = Model()`, this means `Model.init()` gets called many times throughout the view’s life time. Xcode 27 introduces a new `@State` implementation that avoids this repeated evaluation. This new behavior back-deploys to iOS 17 aligned OSes. The new `@State` is implemented with a Swift macro. It is largely source compatible with the property wrapper version, with a few exceptions. If you provide an initial value at `@State` declaration, and also try to assign a value to it in an initializer, the initializer value is discarded. This behavior has not changed because of the macro, but some such cases no longer compiles: ```None
 struct StickerPageView: View {
     @State private var page = StickerPage()
     let title: String
 
     init(title: String) {
         // `title` won't have any effect
         // this also won't compile with @State macro
         self.page = StickerPage(title: title)
         self.title = title
     }
 }
``` When assigning initial value via an initializer, do not provide an initial value at the @State declaration. ```None
 struct StickerPageView: View {
     @State private var page: StickerPage // no initial value expression
     let title: String
 
     init(title: String) {
         self.page = StickerPage(title: title) // works!
         self.title = title
     }
 }
``` When all stored member of a struct is private, the compiler synthesizes a private init that can be used in extension of the same type: ```None
 struct StickerPageView: View {
     @State private var page: StickerPage
     private let title: String
     ...
 }
 
 extension StickerPageView {
     init(title: String, _ page: StickerPage) {
         self.init(page: page, title: title) // using the sythesized init
     }
 }
``` The state macro disables this synthesized initializer. So the code above no longer compiles. To mitigate, assign value to members explicitly: ```None
 extension StickerPageView {
     init(title: String, _ page: StickerPage) {
         self.title = title
         self.page = page
     }
 }
``` In rare situations, the automatic inference of generic argument of `@State` is less flexible with the macro implementation. Write the type with more specificity. Composing `@State` with other property wrappers or macros is not supported.  (105893279)
- In apps built with the iOS 27.0 and macOS 27.0 SDKs, selectable `Text` views now support `TextRenderer`.  (158160386) (FB19589465)
- In apps built with the 27.0 SDKs, the new `ReadableDocument` and `WritableDocument` protocols support asynchronous reading and writing, progress reporting, and direct access to document URLs. New `DocumentGroup` initializers that adopt these protocols let you disable document creation for editing-only apps and present custom UI before any document is opened. The initializers expose an `Observable` `URLDocumentConfiguration` and integrate with Swift concurrency and the `Observation` framework. New applications should prefer `ReadableDocument` and `WritableDocument` over `ReferenceFileDocument`, which remains available.  (158441552)
- In apps built with the iOS 27.0 and iPadOS 27.0 SDKs, a `TabView` enforces that its selection is set to a visible tab. `TabView` might crash when its selection is set to a hidden or otherwise unavailable tab.  (164516837)
- You can use `.toolbarVisibility(hideStatusBar ? .hidden : .automatic, for: .statusBar)` to conditionally hide the status bar.  (165329279)
- The menu bar on iPadOS 27.0 and macOS 27.0, as well as context menus on macOS 27.0, present a reduced set of menu item images. By default, SwiftUI now hides all menu item symbol images in most contexts, while non-symbol images remain visible. Review the updated Human Interface Guidelines to determine which menu items in your app should still display images. Use the `labelStyle(_:)` view modifier with the `.titleAndIcon` style to indicate that a menu item `Label`’s icon should always be shown — such as when the menu item represents an object or a concept rather than an action. SwiftUI continues to automatically provide default visible menu item images for certain common system-wide menu items, such as Settings, Share, and Print.  (170480710)
- The `TabsPickerStyle` style is now available for pickers that represent tab-based navigation and content selection. This style is similar to the `.segmented` style, but VoiceOver reads it as “tabs,” and on macOS it has a distinct visual appearance that distinguishes it from pickers that represent value selection — for example, a text alignment picker in an inspector.  (173211711)
- In apps built with the iOS 27.0 SDK, you can display non-interactive content on external display scenes using the `.sceneAccessory` view modifier with an `ExternalNonInteractiveAccessory` type.  (175548901)
- In apps built with the 27.0 SDKs, a `LabeledContent` view used inside a `Menu` maps its value to the platform menu item’s subtitle.  (175594929)

###### Resolved Issues

- Fixed: In apps built with the 2027 SDKs, tapping the status bar to scroll a `ScrollView` to its top correctly updates a bound `scrollPosition`. Previously, the binding could be left holding a stale value because the scroll-to-top transition didn’t drive the scroll-phase updates that propagate to the binding.  (111501113) (FB12477370)
- Fixed: A custom `TextRenderer` applied via `.textRenderer(_:)` now takes effect on a `Text` view that also has `.textSelection(.enabled)` applied. Previously, the custom renderer was dropped on selectable text, falling back to default rendering.  (151015350)
- Fixed: When you apply both `.fileExporter(_:...)` and `.fileMover(_:...)` modifiers to a view, some dialogs might not present correctly.  (154080867)
- Fixed: In apps built with the 27.0 SDKs, `containerRelativeFrame(_:alignment:)` incorrectly accounts for safe-area insets on a `ScrollView`’s non-scrollable axis, causing the calculated scrollable content size to be too small. For example, a view using `containerRelativeFrame(.vertical)` inside a horizontal `ScrollView` extends into vertical safe-area regions, such as the navigation bar and home indicator, because only the scrollable axis insets are applied.  (165913417)
- Fixed: Retroactive conformances of SwiftUI types to Equatable are not consulted when SwiftUI compares their values.  (167443223)
- Fixed: In apps built with the 27.0 SDKs, the `controlSize`, `buttonSizing`, `buttonRepeatBehavior`, `menuIndicatorVisibility`, and `ButtonBorderShape` environment values are not reset to their default values in sheets and popovers.  (167448274)
- Fixed: A Button containing both an icon and a title placed inside a `List` `Section` header or footer has incorrect spacing between its icon and title.  (175681345)
- Fixed: When you present a `fullScreenCover` with a `.navigationTransition(_:)` and set `@FocusState` to `true` via `.onAppear`, the keyboard does not animate concurrently with the zoom transition. Instead, it waits for the entire zoom animation to complete before the keyboard begins animating up, resulting in a visually jarring 2-step animation.  (178421089)

###### Known Issues

- Progress reported in `DocumentReader.read(from:progress:)` and `DocumentWriter.write(snapshot:to:previous:progress:)` might not be presented.  (158441261)

##### System

###### New Features

- System now provides Swift APIs for the C `stat`, `lstat`, `fstat`, and `fstatat` system calls. This includes a new `Stat` type with initializers from `FilePath`, `FileDescriptor`, or a C string; `FilePath.stat()` and `FileDescriptor.stat()` instance methods; and supporting types (`FileType`, `FileMode`, `FileFlags`, `UserID`, `GroupID`, `DeviceID`, and `Inode`). See [`SYS-0006`](https://developer.apple.comhttps://github.com/apple/swift-system/blob/main/Proposals/0006-system-stat.md) for more details.  (160612181)

###### Known Issues

- Custom `FilePath` or `FileDescriptor` extensions that make unqualified calls to `stat()` or `stat(_:_:)` (without the `Darwin.` qualification) might conflict with the new Swift `stat()` instance methods introduced in [`SYS-0006`](https://developer.apple.comhttps://github.com/apple/swift-system/blob/main/Proposals/0006-system-stat.md), causing build errors.   (177911316) **Workaround:** Migrate to the new Swift `stat()` methods, or disambiguate using `Darwin.stat()` and `Darwin.stat(_:_:)`. See [`SYS-0008`](https://developer.apple.comhttps://github.com/apple/swift-system/blob/main/Proposals/0008-backdeploy-cinterop-stat.md) for more details.

##### System Experience

###### Known Issues

- When Siri is off and your iPad is extended to an external display where Spotlight is on screen, disconnecting the display might cause the system to crash.   (176281601) **Workaround:** Dismiss Spotlight before disconnecting the external display, or turn on Siri.
- After using iPhone Mirroring or other non-main display experiences, a black pill may appear on the CarPlay screen.  (177893758) **Workaround:** Reboot.

##### Textkit

###### New Features

- `NSTextTable` and its related objects and types are available to UIKit clients starting with OS 27 releases.  (159870239)

##### Trust Insights

###### New Features

- You can now use the TrustInsights framework in your apps by declaring the TrustInsights capability on your app target in Xcode. The framework requires an entitlement and internet connectivity to return results.  (154949256)

##### Uikit

###### New Features

- When linked on iOS 27, tvOS 27, macCatalyst 27, or visionOS 27 SDKs, you can use `UIScene.extendStateRestoration` and `UIScene.completeStateRestoration` to extend state restoration for `UIScene.ActivationState.background` to `UIScene.ActivationState.foreground` lifecycle transitions.  (161843040)
- iOS and iPadOS apps built with the 27.0 SDK or later are required to include a launch screen. Your app’s `Info.plist` must contain one of the following keys: `UILaunchStoryboardName`, `UILaunchStoryboards`, `UILaunchScreen`, or `UILaunchScreens`. Apps that don’t include a launch screen are rejected when the App Store begins accepting apps built with the 27.0 SDK.  (168247372)
- On iOS 27.0 and iPadOS 27.0, Siri can load resources from drag interactions installed in your app’s interface. For example, when Apple Intelligence is invoked from a context menu, the system calls `UIDragInteractionDelegate` methods to load the content. Because drag sessions might begin without a user-initiated drag gesture, avoid performing animations or presenting modal UI for the drag in `dragInteraction(_:sessionWillBegin:)`. Instead, perform those actions in `dragInteraction(_:sessionDidMove:)`.  (168884200)
- In apps built with the iOS 27.0 SDK, a presented view controller inherits its trait collection by walking up its view’s superview chain through the intermediate views of the presentation, rather than jumping directly to the presentation controller. Custom `UIPresentationController` subclasses or view controllers that depend on receiving traits directly from the presentation controller might need to update how they propagate or override `traitCollection`.  (170005251)
- On iPadOS 27.0 and macOS 27.0, the menu bar and context menus present a reduced set of menu item images and do not display images set on menu elements by default. You can use the new `preferredImageVisibility` property on `UIMenuElement` — including updated initializers on `UIMenu`, `UIAction`, `UICommand`, and `UIKeyCommand` — to customize the visibility of each element’s image in these menus. Review the updated Human Interface Guidelines to determine which menu elements in your app should display images. UIKit automatically provides default visible menu element images for certain common system-wide menu items, such as Settings, Share, and Print.  (170479084)
- In apps built with the iOS 27.0 SDK, when `UISearchController` uses center search-bar placement, the scope bar appears inline on the same row as the search field rather than on a separate row beneath it. When the search field is hosted inside a navigation bar, the scope bar sits inline beside the search field within that navigation bar.  (173860616)
- In apps built with the iOS 27.0 SDK, `windowExternalDisplayNonInteractive` scenes are no longer offered automatically by the system. Use `UIViewController.registerSceneAccessory(_:)` with a `UISceneAccessory.externalNonInteractive` instance to display non-interactive content on external display scenes.  (177015874)

###### Resolved Issues

- Fixed: The `UIMenuLeaf` protocol is missing the subtitle property introduced in iOS 16.0.  (173271862)

###### Known Issues

- In apps built with the iOS 27.0 SDK, the deprecated status bar accessors on `UIApplication`  — including `statusBarFrame`, `statusBarOrientation`, `statusBarStyle`, and `isStatusBarHidden` — might return NaN or null values.   (162044221) **Workaround:** Read current values from `UIWindowScene.statusBarManager` instead.
- On iPad, if your iPad app is built with the iOS 27 SDK and its `UISupportedInterfaceOrientations` doesn’t include all four interface orientations, the app is treated as non-continuously resizable. Beginning with iOS 27, supported interface orientations should no longer be a condition for continuous resizability.  (166422120) **Workaround:** To make your app continuously resizable on iPad, declare support for all four interface orientations in your `Info.plist` with `UISupportedInterfaceOrientations`.
- The `UISceneClosureConfirmation` API does not present a confirmation dialog.  (169108042)
- The background might not appear on a bottom toolbar when you use `UIBarButtonItem.hidesSharedBackground` to hide a toolbar item’s glass background.  (174773785)
- In iPhone Mirroring, if your app is built with the iOS 27 SDK its scene will support all interface orientations regardless of the orientations declared in `UISupportedInterfaceOrientations` or returned by `UIViewController.supportedInterfaceOrientations`. Supported interface orientations should be honored until the user begins resizing the window.  (178555304)
- In iPhone Mirroring, if your app is built with the iOS 27 SDK and sets `UIRequiresFullScreen`, its scene receives continuous resize updates when the user resizes the window. Each resize should instead be delivered as a discrete change to a new `UIScreen` with an updated bounds.  (178558224)
- In iPhone Mirroring if your app is built with the iOS 27 SDK, its scene is initially connected to a `UIScreen` that isn’t `UIScreen.main`. The scene should start on the main screen.  (178558897)
- On iPad, if your iPad app is built with the iOS 27 SDK and sets `UIRequiresFullScreen`, the bounds of `UIScreen.main` changes when the user resizes the window. The bounds of the main screen should remain fixed once the screen connects.  (178559386)
- On iPad, if your iPad app is built with the iOS 27 SDK and sets `UIRequiresFullScreen`, its scene receives continuous resize updates when the user resizes the window. Each resize should instead be delivered as a discrete change to a new `UIScreen` with an updated bounds.  (178560235)
- On iPad, if your iPhone-only app is built with the iOS 27 SDK its scene continues to honor supported interface orientations after the user resizes the window. After the first resize, the scene should ignore supported interface orientations.  (178561952)
- On iPad, if your iPhone-only app is built with the iOS 27 SDK and sets `UIRequiresFullScreen`, its scene receives continuous resize updates when the user resizes the window. Each resize should instead be delivered as a discrete change to a new `UIScreen` with an updated bounds.  (178562971)
- On iPad, if your iPhone-only app is built with the iOS 27 SDK and supports only portrait or only landscape interface orientations, its layout breaks when the iPad is in an orientation the app doesn’t support.  (178573319)

###### Deprecations

- Apps built with the latest SDK must adopt the scene-based life cycle or they fail to launch. For migration guidance, see [`Transitioning to the UIKit scene-based life cycle`](https://developer.apple.comhttps://developer.apple.com/documentation/uikit/transitioning-to-the-uikit-scene-based-life-cycle).  (141837548)

##### Usdkit

###### Known Issues

- Some types of USD attributes cannot be read or modified.  (170653056)
- Array, vector, matrix, and quaternion types cannot be authored using USDKit.  (178071414)

##### Videotoolbox

###### New Features

- `VTLowLatencySuperResolutionScalerConfiguration` now supports a 1.5x scale factor. Call `+supportedScaleFactorsForFrameWidth:frameHeight:` to discover the scale factors available for your source dimensions.  (177635243)
- `VTLowLatencyFrameInterpolationConfiguration` now supports arbitrary source dimensions up to 1080p.  (179040806)

##### Watch Connectivity

###### Resolved Issues

- Fixed: The `WCSession.transferCurrentComplicationUserInfo` method does not work with complications built using WidgetKit on watchOS.  (113202790) (FB12819178)

##### Weather Highlights

###### Known Issues

- Weather Highlights is currently only available in US English.  (164408676)

##### Widgetkit

###### Known Issues

- Your widget extension might not render its timeline when it uses an App Intent with a `@UnionValue` parameter, and content such as images might not appear. This affects `WidgetConfigurationIntent` types that you declare with a `@UnionValue` property.  (177493357) **Workaround:** Use a single `AppEntity` type with a kind property to distinguish the variants.

##### Writing Tools

###### Known Issues

- Writing Tools becomes unresponsive when you interact with the Plus button while Writing Tools is in use.  (177097101) **Workaround:** Force quit Messages to resolve the issue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)*