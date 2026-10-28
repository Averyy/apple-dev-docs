# AuthenticationServices updates

**Framework**: Updates  
**Role**: Article

Learn about important changes to AuthenticationServices.

## Overview

Browse notable changes in [Authentication Services](../AuthenticationServices/AuthenticationServices.md).

## June 2024

### Passkeys

- Automatically upgrade someone’s password to a passkey after your app supplies a password to AutoFill if they’re eligible, while still retaining their password in case they need it. To do this, call [`createCredentialRegistrationRequest(challenge:name:userID:requestStyle:)`](../AuthenticationServices/asauthorizationplatformpublickeycredentialprovider/createcredentialregistrationrequest%28challenge,name,userid,requeststyle%29.md), passing [`ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest.RequestStyle.conditional`](../AuthenticationServices/asauthorizationplatformpublickeycredentialregistrationrequest/requeststyle-swift.enum/conditional.md) for the `requestStyle` parameter.
- Use the `prf` WebAuthentication extension to generate a symmetric key from a passkey, which you use for encrypting and decrypting someone’s data. Each passkey generates its own symmetric keys, which you can retrieve any time a user signs in with that passkey, in apps or on the web.

### Credential providers

- Indicate to the system that your credential provider participates in OTP AutoFill by adding the key `ProvidesOneTimeCodes` with the value `true` to the `ASCredentialProviderExtensionCapabilities` dictionary in your app’s information property list. Implement [`provideCredentialWithoutUserInteraction(for:)`](../AuthenticationServices/ascredentialproviderviewcontroller/providecredentialwithoutuserinteraction%28for%29-3mo23.md) and [`prepareInterfaceToProvideCredential(for:)`](../AuthenticationServices/ascredentialproviderviewcontroller/prepareinterfacetoprovidecredential%28for%29-68qpo.md) to handle the [`ASOneTimeCodeCredentialRequest`](../AuthenticationServices/asonetimecodecredentialrequest.md) type. Use [`completeOneTimeCodeRequest(using:completionHandler:)`](../AuthenticationServices/ascredentialproviderextensioncontext/completeonetimecoderequest%28using,completionhandler%29.md) to return the one time code to the system.
- Supply AutoFill for text in arbitrary text fields, for example to complete information about an account that someone manages in your credential provider, or AutoFill text in secure notes. Indicate to the system that your credential provider supplies AutoFill text by adding the key ProvidesTextToInsert with the value true to the `ASCredentialProviderExtensionCapabilities` dictionary in your app’s information property list, and implement [`prepareInterfaceForUserChoosingTextToInsert()`](../AuthenticationServices/ascredentialproviderviewcontroller/prepareinterfaceforuserchoosingtexttoinsert%28%29.md). When the person chooses the text to AutoFill in your UI, call [`completeRequest(withTextToInsert:completionHandler:)`](../AuthenticationServices/ascredentialproviderextensioncontext/completerequest%28withtexttoinsert,completionhandler%29.md) to supply the text to the system.
- Use [`ASPasskeyCredentialExtensionInput`](../AuthenticationServices/aspasskeycredentialextensioninput.md) to represent `largeBlob` and `prf` extension input data in a passkey credential request. Return output for these WebAuthentication extensions using [`ASPasskeyAssertionCredentialExtensionOutput`](../AuthenticationServices/aspasskeyassertioncredentialextensionoutput-swift.struct.md) and [`ASPasskeyRegistrationCredentialExtensionOutput`](../AuthenticationServices/aspasskeyregistrationcredentialextensionoutput-swift.struct.md) as part of the [`ASPasskeyAssertionCredential`](../AuthenticationServices/aspasskeyassertioncredential.md) and [`ASPasskeyRegistrationCredential`](../AuthenticationServices/aspasskeyregistrationcredential.md) objects you return to the system.

### Platform Single Sign-On

- Support stronger encryption and signing options by specifying [`supportedDeviceEncryptionAlgorithms`](../AuthenticationServices/asauthorizationproviderextensionregistrationhandler/supporteddeviceencryptionalgorithms.md), [`supportedDeviceSigningAlgorithms`](../AuthenticationServices/asauthorizationproviderextensionregistrationhandler/supporteddevicesigningalgorithms.md), and [`supportedUserSecureEnclaveKeySigningAlgorithms`](../AuthenticationServices/asauthorizationproviderextensionregistrationhandler/supportedusersecureenclavekeysigningalgorithms.md) in the SSO extension. You can now use Hybrid Public Key Encryption (HPKE) algorithms defined in [`ASAuthorizationProviderExtensionEncryptionAlgorithm`](../AuthenticationServices/asauthorizationproviderextensionencryptionalgorithm.md): `ecdhe_A256GCM`, `hpke_P256_SHA256_AES_GCM_256`, `hpke_P384_SHA384_AES_GCM_256`, and `hpke_Curve25519_SHA256_ChachaPoly`.
- If you use HPKE, receive notifications when the system rotates the encryption key by implementing [`keyWillRotate(for:newKey:loginManager:completion:)`](../AuthenticationServices/asauthorizationproviderextensionregistrationhandler/keywillrotate%28for,newkey,loginmanager,completion%29.md) in your SSO extension. The system automatically rotates the encryption key about once per week. This lets you register the new key on the server.
- Rotate the keys you use for platform SSO by calling the [`ASAuthorizationProviderExtensionLoginManager`](../AuthenticationServices/asauthorizationproviderextensionloginmanager.md) methods [`beginKeyRotation(_:)`](../AuthenticationServices/asauthorizationproviderextensionloginmanager/beginkeyrotation%28_%29.md) and [`completeKeyRotation(_:)`](../AuthenticationServices/asauthorizationproviderextensionloginmanager/completekeyrotation%28_%29.md).

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
- [AVFAudio updates](./avfaudio.md)
  Learn about important changes to AVFAudio.
- [AVFoundation updates](./avfoundation.md)
  Learn about important changes to AVFoundation.
- [AVKit updates](./avkit.md)
  Learn about important changes to AVKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/authenticationservices)*