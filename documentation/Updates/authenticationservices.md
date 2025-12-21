# AuthenticationServices updates

**Framework**: Updates

Learn about important changes to AuthenticationServices.

#### Overview

Browse notable changes in [`Authentication Services`](https://developer.apple.com/documentation/AuthenticationServices).

#### June 2024

##### Passkeys

- Automatically upgrade someone’s password to a passkey after your app supplies a password to AutoFill if they’re eligible, while still retaining their password in case they need it. To do this, call [`createCredentialRegistrationRequest(challenge:name:userID:requestStyle:)`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorizationPlatformPublicKeyCredentialProvider/createCredentialRegistrationRequest(challenge:name:userID:requestStyle:)), passing [`ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest.RequestStyle.conditional`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest/RequestStyle-swift.enum/conditional) for the `requestStyle` parameter.
- Use the `prf` WebAuthentication extension to generate a symmetric key from a passkey, which you use for encrypting and decrypting someone’s data. Each passkey generates its own symmetric keys, which you can retrieve any time a user signs in with that passkey, in apps or on the web.

##### Credential Providers

- Indicate to the system that your credential provider participates in OTP AutoFill by adding the key `ProvidesOneTimeCodes` with the value `true` to the `ASCredentialProviderExtensionCapabilities` dictionary in your app’s information property list. Implement [`provideCredentialWithoutUserInteraction(for:)`](https://developer.apple.com/documentation/AuthenticationServices/ASCredentialProviderViewController/provideCredentialWithoutUserInteraction(for:)-3mo23) and [`prepareInterfaceToProvideCredential(for:)`](https://developer.apple.com/documentation/AuthenticationServices/ASCredentialProviderViewController/prepareInterfaceToProvideCredential(for:)-68qpo) to handle the [`ASOneTimeCodeCredentialRequest`](https://developer.apple.com/documentation/AuthenticationServices/ASOneTimeCodeCredentialRequest) type. Use [`completeOneTimeCodeRequest(using:completionHandler:)`](https://developer.apple.com/documentation/AuthenticationServices/ASCredentialProviderExtensionContext/completeOneTimeCodeRequest(using:completionHandler:)) to return the one time code to the system.
- Supply AutoFill for text in arbitrary text fields, for example to complete information about an account that someone manages in your credential provider, or AutoFill text in secure notes. Indicate to the system that your credential provider supplies AutoFill text by adding the key ProvidesTextToInsert with the value true to the `ASCredentialProviderExtensionCapabilities` dictionary in your app’s information property list, and implement [`prepareInterfaceForUserChoosingTextToInsert()`](https://developer.apple.com/documentation/AuthenticationServices/ASCredentialProviderViewController/prepareInterfaceForUserChoosingTextToInsert()). When the person chooses the text to AutoFill in your UI, call [`completeRequest(withTextToInsert:completionHandler:)`](https://developer.apple.com/documentation/AuthenticationServices/ASCredentialProviderExtensionContext/completeRequest(withTextToInsert:completionHandler:)) to supply the text to the system.
- Use [`ASPasskeyCredentialExtensionInput`](https://developer.apple.com/documentation/AuthenticationServices/ASPasskeyCredentialExtensionInput) to represent `largeBlob` and `prf` extension input data in a passkey credential request. Return output for these WebAuthentication extensions using [`ASPasskeyAssertionCredentialExtensionOutput`](https://developer.apple.com/documentation/AuthenticationServices/ASPasskeyAssertionCredentialExtensionOutput-swift.struct) and [`ASPasskeyRegistrationCredentialExtensionOutput`](https://developer.apple.com/documentation/AuthenticationServices/ASPasskeyRegistrationCredentialExtensionOutput-swift.struct) as part of the [`ASPasskeyAssertionCredential`](https://developer.apple.com/documentation/AuthenticationServices/ASPasskeyAssertionCredential) and [`ASPasskeyRegistrationCredential`](https://developer.apple.com/documentation/AuthenticationServices/ASPasskeyRegistrationCredential) objects you return to the system.

##### Platform Single Sign on

- Support stronger encryption and signing options by specifying [`supportedDeviceEncryptionAlgorithms`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorizationProviderExtensionRegistrationHandler/supportedDeviceEncryptionAlgorithms), [`supportedDeviceSigningAlgorithms`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorizationProviderExtensionRegistrationHandler/supportedDeviceSigningAlgorithms), and [`supportedUserSecureEnclaveKeySigningAlgorithms`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorizationProviderExtensionRegistrationHandler/supportedUserSecureEnclaveKeySigningAlgorithms) in the SSO extension. You can now use Hybrid Public Key Encryption (HPKE) algorithms defined in [`ASAuthorizationProviderExtensionEncryptionAlgorithm`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorizationProviderExtensionEncryptionAlgorithm): `ecdhe_A256GCM`, `hpke_P256_SHA256_AES_GCM_256`, `hpke_P384_SHA384_AES_GCM_256`, and `hpke_Curve25519_SHA256_ChachaPoly`.
- If you use HPKE, receive notifications when the system rotates the encryption key by implementing [`keyWillRotate(for:newKey:loginManager:completion:)`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorizationProviderExtensionRegistrationHandler/keyWillRotate(for:newKey:loginManager:completion:)) in your SSO extension. The system automatically rotates the encryption key about once per week. This lets you register the new key on the server.
- Rotate the keys you use for platform SSO by calling the [`ASAuthorizationProviderExtensionLoginManager`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorizationProviderExtensionLoginManager) methods [`beginKeyRotation(_:)`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorizationProviderExtensionLoginManager/beginKeyRotation(_:)) and [`completeKeyRotation(_:)`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorizationProviderExtensionLoginManager/completeKeyRotation(_:)).

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
- [AVFAudio updates](avfaudio.md)
  Learn about important changes to AVFAudio.
- [AVFoundation updates](avfoundation.md)
  Learn about important changes to AVFoundation.
- [Background Tasks updates](backgroundtasks.md)
  Learn about important changes in Background Tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/authenticationservices)*