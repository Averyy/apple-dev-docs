# outerIdentity

**Framework**: Wi-Fi Infrastructure  
**Kind**: property

A name that hides the user’s actual name.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
let outerIdentity: String?
```

#### Discussion

The user’s actual name appears only inside the encrypted tunnel. For example, the system configuration might set this to `anonymous` or `anon`, or `anon@mycompany.net`. It can increase security because an attacker can’t see the authenticating user’s name in the clear. This key is only relevant to TTLS, PEAP, and EAP-FAST.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/network/credentials-swift.enum/eapcredentials/outeridentity)*